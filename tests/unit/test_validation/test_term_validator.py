"""Tests for the term validator, using the bundled go-nucleus SQLite ontology."""

import io
import unittest

from oaklib import get_adapter

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.markdown_exporter import MarkdownExporter
from ontogpt.io.template_loader import get_template_details
from ontogpt.templates.core import ExtractionResult, NamedEntity
from ontogpt.templates.go_simple import OntologyTermSet
from ontogpt.validation import TermValidator
from tests import INPUT_DIR, OUTPUT_DIR

GO_DB = f"sqlite:{INPUT_DIR / 'go-nucleus.db'}"
CACHE_DIR = OUTPUT_DIR / "term-validator-cache"

NUCLEUS = "GO:0005634"  # label "nucleus", synonym "cell nucleus"
MEMBRANE = "GO:0016020"  # label "membrane"
OBSOLETE_ENVELOPE = "GO:0005636"  # obsolete; replaced by GO:0005635
NUCLEAR_ENVELOPE = "GO:0005635"


def make_engine() -> SPIRESEngine:
    adapter = get_adapter(GO_DB)
    engine = SPIRESEngine(
        template_details=get_template_details("go_simple"),
        model="fake/model",
        auto_prefix="AUTO",
        term_validation_adapters={"GO": adapter},
        term_validation_cache_dir=str(CACHE_DIR),
    )
    # Ground and search against the local database rather than sqlite:obo:go.
    engine.annotators = {"OntologyTerm": [adapter]}
    return engine


def make_result(pairs):
    obj = OntologyTermSet(id="doc1", terms=[curie for curie, _ in pairs])
    entities = [NamedEntity(id=curie, label=label) for curie, label in pairs]
    return ExtractionResult(input_text="text", extracted_object=obj, named_entities=entities)


class TestTermValidator(unittest.TestCase):
    """Validation outcomes and in-place repair."""

    @classmethod
    def setUpClass(cls):
        cls.engine = make_engine()

    def validate(self, pairs):
        result = make_result(pairs)
        self.engine.validate_extraction_result(result)
        return result

    def by_id(self, result, curie):
        return next(r for r in result.validation.results if r.original_id == curie)

    def test_valid_label_and_synonym(self):
        result = self.validate([(NUCLEUS, "nucleus"), (MEMBRANE, "membrane")])
        self.assertEqual(result.validation.total_terms, 2)
        self.assertEqual(result.validation.valid_terms, 2)
        self.assertEqual(self.by_id(result, NUCLEUS).status, "VALID")

        result = self.validate([(NUCLEUS, "cell nucleus")])
        outcome = self.by_id(result, NUCLEUS)
        self.assertEqual(outcome.status, "VALID")
        self.assertEqual(outcome.ontology_label, "nucleus")
        self.assertIn("synonym", outcome.message)
        self.assertEqual(result.extracted_object.terms, [NUCLEUS])

    def test_label_differs_is_kept_when_no_exact_match(self):
        result = self.validate([(MEMBRANE, "mitochondrion")])
        outcome = self.by_id(result, MEMBRANE)
        self.assertEqual(outcome.status, "LABEL_DIFFERS")
        self.assertIsNone(outcome.replacement_id)
        self.assertEqual(result.validation.label_mismatches, 1)
        self.assertEqual(result.extracted_object.terms, [MEMBRANE])

    def test_label_differs_is_replaced_by_exact_match(self):
        # The label names a different term that exists; swap to it.
        result = self.validate([(MEMBRANE, "nuclear envelope")])
        outcome = self.by_id(result, MEMBRANE)
        self.assertEqual(outcome.status, "REPLACED")
        self.assertEqual(outcome.replacement_id, NUCLEAR_ENVELOPE)
        self.assertEqual(result.extracted_object.terms, [NUCLEAR_ENVELOPE])
        self.assertEqual(result.named_entities[0].id, NUCLEAR_ENVELOPE)

    def test_obsolete_term_follows_replacement(self):
        result = self.validate([(OBSOLETE_ENVELOPE, "nuclear envelope lumen")])
        outcome = self.by_id(result, OBSOLETE_ENVELOPE)
        self.assertEqual(outcome.status, "REPLACED")
        self.assertEqual(outcome.replacement_id, NUCLEAR_ENVELOPE)
        self.assertEqual(outcome.replacement_label, "nuclear envelope")
        self.assertEqual(result.extracted_object.terms, [NUCLEAR_ENVELOPE])

    def test_missing_term_is_regrounded_from_label(self):
        result = self.validate([("GO:9999999", "nuclear envelope")])
        outcome = self.by_id(result, "GO:9999999")
        self.assertEqual(outcome.status, "REPLACED")
        self.assertEqual(outcome.replacement_id, NUCLEAR_ENVELOPE)
        self.assertIn(NUCLEAR_ENVELOPE, outcome.attempts)

    def test_missing_term_without_match_becomes_auto(self):
        result = self.validate([("GO:8888888", "flux capacitor")])
        outcome = self.by_id(result, "GO:8888888")
        self.assertEqual(outcome.status, "UNRESOLVED")
        self.assertEqual(outcome.replacement_id, "AUTO:flux%20capacitor")
        self.assertEqual(result.extracted_object.terms, ["AUTO:flux%20capacitor"])
        self.assertEqual(result.named_entities[0].id, "AUTO:flux%20capacitor")
        self.assertEqual(result.validation.unresolved_terms, 1)

    def test_unknown_prefix_and_auto_values(self):
        result = self.validate([("FOO:123", "foo"), ("AUTO:junk", "junk")])
        outcome = self.by_id(result, "FOO:123")
        self.assertEqual(outcome.status, "SKIPPED")
        self.assertEqual(result.validation.skipped_terms, 1)
        # AUTO values are not grounded terms and are not examined at all.
        self.assertEqual(result.validation.total_terms, 1)
        self.assertEqual(result.extracted_object.terms, ["FOO:123", "AUTO:junk"])

    def test_report_names_validator(self):
        result = self.validate([(NUCLEUS, "nucleus")])
        self.assertTrue(result.validation.validator.startswith("linkml-term-validator"))

    def test_validation_can_be_disabled(self):
        engine = make_engine()
        engine.validate_terms = False
        result = make_result([("GO:8888888", "flux capacitor")])
        # The engine only validates through extract_from_text; simulate the guard.
        engine._extraction_depth = 0
        if engine.validate_terms:
            engine.validate_extraction_result(result)
        self.assertIsNone(result.validation)
        self.assertEqual(result.extracted_object.terms, ["GO:8888888"])

    def test_exporters_render_validation_section(self):
        result = self.validate([(NUCLEUS, "cell nucleus"), ("GO:8888888", "flux capacitor")])
        md = io.StringIO()
        MarkdownExporter().export(result, md)
        text = md.getvalue()
        self.assertIn("## Validation", text)
        self.assertIn("UNRESOLVED", text)
        self.assertIn("bioregistry.io/GO:0005634", text)
        html = io.StringIO()
        HTMLExporter(output=html).export(result, html)
        self.assertIn("Validation", html.getvalue())
        self.assertIn("flux capacitor", html.getvalue())

    def test_validator_prefix_map_from_template(self):
        validator = TermValidator(engine=self.engine, cache_dir=CACHE_DIR)
        validator._ensure_validator()
        self.assertIn("GO", validator._prefix_map)
