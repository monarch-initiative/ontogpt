"""Tests for identifier validation and normalization without network access.

Regression tests for https://github.com/monarch-initiative/ontogpt/issues/566: a grounded
id whose prefix is right but which a ``values_from`` enum (or the id ``pattern``) rejects
must not be sent to the Translator node normalizer. Only ids with a foreign prefix go there.
"""

import unittest
from unittest.mock import MagicMock

from linkml_runtime import SchemaView
from oaklib.datamodels.text_annotator import TextAnnotation
from oaklib.interfaces import MappingProviderInterface

from ontogpt.engines.knowledge_engine import (
    REJECT_PATTERN,
    REJECT_PREFIX,
    REJECT_VALUE_SET,
    KnowledgeEngine,
)

SCHEMA = """
id: http://example.org/breeds
name: breeds
prefixes:
  linkml: https://w3id.org/linkml/
  breeds: http://example.org/breeds/
  VBO: http://purl.obolibrary.org/obo/VBO_
  NCBITaxon: http://purl.obolibrary.org/obo/NCBITaxon_
default_prefix: breeds
default_range: string
imports:
  - linkml:types
enums:
  CatBreedIdentifier:
    permissible_values:
      VBO:0100000: {}
      VBO:0100001: {}
classes:
  Breed:
    id_prefixes:
      - VBO
    attributes:
      id:
        identifier: true
        pattern: "^VBO:[0-9]{7}$"
        values_from:
          - CatBreedIdentifier
      label:
        range: string
"""

ABYSSINIAN_CAT = "VBO:0100000"
ABYSSINIAN_ASS = "VBO:0001830"
ABYSSINIAN_HORSE = "VBO:0011418"


def annotation(object_id: str, object_label: str) -> TextAnnotation:
    return TextAnnotation(object_id=object_id, object_label=object_label)


class TestIdentifierNormalization(unittest.TestCase):
    """Rejected ids are explained, and only prefix rejections reach the mapper."""

    def setUp(self):
        self.sv = SchemaView(SCHEMA)
        self.cls = self.sv.get_class("Breed")
        self.mapper = MagicMock(spec=MappingProviderInterface)
        self.mapper.sssom_mappings.return_value = []
        self.ke = KnowledgeEngine(
            template_details=(self.cls, None, None, self.sv),
            model="fake/model",
            mappers=[self.mapper],
        )

    def test_rejection_reasons(self):
        cases = [
            (ABYSSINIAN_CAT, None),
            ("NCBITaxon:9685", REJECT_PREFIX),
            ("not a curie", REJECT_PREFIX),
            ("VBO:12", REJECT_PATTERN),
            (ABYSSINIAN_ASS, REJECT_VALUE_SET),
        ]
        for curie, reason in cases:
            rejection = self.ke.identifier_rejection(curie, self.cls)
            if reason is None:
                self.assertIsNone(rejection, curie)
                self.assertTrue(self.ke.is_valid_identifier(curie, self.cls))
            else:
                self.assertIsNotNone(rejection, curie)
                self.assertEqual(rejection.reason, reason, curie)
                self.assertFalse(self.ke.is_valid_identifier(curie, self.cls))
        self.assertIn(
            "CatBreedIdentifier", self.ke.identifier_rejection(ABYSSINIAN_ASS, self.cls).message
        )

    def test_valid_id_is_yielded_without_mapping(self):
        self.assertEqual(
            [ABYSSINIAN_CAT], list(self.ke.normalize_identifier(ABYSSINIAN_CAT, self.cls))
        )
        self.mapper.sssom_mappings.assert_not_called()

    def test_enum_rejected_id_skips_mapper(self):
        self.ke.grounding_labels[ABYSSINIAN_ASS] = "Abyssinian, Ethiopia (Ass)"
        with self.assertLogs("ontogpt.engines.knowledge_engine", level="INFO") as logs:
            result = list(self.ke.normalize_identifier(ABYSSINIAN_ASS, self.cls))
        self.assertEqual([], result)
        self.mapper.sssom_mappings.assert_not_called()
        rejected = [line for line in logs.output if "Rejected" in line]
        self.assertEqual(1, len(rejected))
        self.assertIn(
            "VBO:0001830 (Abyssinian, Ethiopia (Ass)): not in enum CatBreedIdentifier", rejected[0]
        )

    def test_pattern_rejected_id_skips_mapper(self):
        self.assertEqual([], list(self.ke.normalize_identifier("VBO:12", self.cls)))
        self.mapper.sssom_mappings.assert_not_called()

    def test_foreign_prefix_goes_to_mapper(self):
        mapping = MagicMock()
        mapping.object_id = ABYSSINIAN_CAT
        self.mapper.sssom_mappings.return_value = [mapping]
        self.assertEqual(
            [ABYSSINIAN_CAT], list(self.ke.normalize_identifier("NCBITaxon:9685", self.cls))
        )
        self.mapper.sssom_mappings.assert_called_once_with(["NCBITaxon:9685"])

    def test_foreign_prefix_mapped_to_enum_rejected_id_yields_nothing(self):
        mapping = MagicMock()
        mapping.object_id = ABYSSINIAN_ASS
        self.mapper.sssom_mappings.return_value = [mapping]
        self.assertEqual([], list(self.ke.normalize_identifier("NCBITaxon:9685", self.cls)))


class TestGroundingLabelPreference(unittest.TestCase):
    """Among whole-text hits, one whose own label is the text comes first."""

    def setUp(self):
        self.sv = SchemaView(SCHEMA)
        self.cls = self.sv.get_class("Breed")
        self.annotator = MagicMock()
        self.ke = KnowledgeEngine(
            template_details=(self.cls, None, None, self.sv),
            model="fake/model",
            mappers=[],
            annotators={"Breed": [self.annotator]},
        )

    def test_label_match_outranks_synonym_match(self):
        hits = [
            annotation(ABYSSINIAN_ASS, "Abyssinian, Ethiopia (Ass)"),
            annotation(ABYSSINIAN_HORSE, "Abyssinian (Horse)"),
            annotation(ABYSSINIAN_CAT, "Abyssinian (Cat)"),
        ]
        # groundings also tries the parenthetical parts; only the whole text has hits here
        self.annotator.annotate_text.side_effect = lambda text, config: (
            list(hits) if text == "Abyssinian (Cat)" else []
        )
        self.assertEqual(
            [ABYSSINIAN_CAT, ABYSSINIAN_ASS, ABYSSINIAN_HORSE],
            list(self.ke.groundings("Abyssinian (Cat)", self.cls)),
        )
        self.assertEqual("Abyssinian (Cat)", self.ke.grounding_labels[ABYSSINIAN_CAT])
        self.assertEqual("Abyssinian (Horse)", self.ke.grounding_labels[ABYSSINIAN_HORSE])

    def test_order_kept_when_no_label_matches(self):
        self.annotator.annotate_text.return_value = [
            annotation(ABYSSINIAN_ASS, "Abyssinian, Ethiopia (Ass)"),
            annotation(ABYSSINIAN_CAT, "Abyssinian (Cat)"),
        ]
        self.assertEqual(
            [ABYSSINIAN_ASS, ABYSSINIAN_CAT],
            list(self.ke.groundings("Abyssinian", self.cls)),
        )

    def test_enum_rejected_hits_never_reach_the_mapper(self):
        mapper = MagicMock(spec=MappingProviderInterface)
        self.ke.mappers = [mapper]
        self.annotator.annotate_text.return_value = [
            annotation(ABYSSINIAN_ASS, "Abyssinian, Ethiopia (Ass)"),
            annotation(ABYSSINIAN_HORSE, "Abyssinian (Horse)"),
            annotation(ABYSSINIAN_CAT, "Abyssinian (Cat)"),
        ]
        self.assertEqual(ABYSSINIAN_CAT, self.ke.normalize_named_entity("Abyssinian", "Breed"))
        mapper.sssom_mappings.assert_not_called()


if __name__ == "__main__":
    unittest.main()
