"""Tests for building KGX edges from YAML extraction output.

Regression tests for https://github.com/monarch-initiative/ontogpt/issues/498.
"""

import tempfile
import unittest
from pathlib import Path

from ontogpt.io.csv_wrapper import parse_yaml_predictions
from ontogpt.io.template_loader import get_template_path

MIC_OUTPUT = """
---
extracted_object:
  id: AUTO:doc1
  nutrient_to_feature_relationships:
    - nutrient: CHEBI:12777
      relationship: RO:0002606
      feature: HP:0000662
      negated: "False"
      context: Vitamin A treats night blindness (5).
      references:
        - "5"
named_entities:
  - id: CHEBI:12777
    label: Vitamin A
  - id: RO:0002606
    label: treats
  - id: HP:0000662
    label: Nyctalopia
"""

GOCAM_OUTPUT = """
---
extracted_object:
  gene_organisms:
    - gene: HGNC:1
      organism: NCBITaxon:9606
named_entities:
  - id: HGNC:1
    label: GENE1
---
extracted_object:
  gene_organisms:
    - gene: HGNC:2
      organism: NCBITaxon:10090
named_entities:
  - id: HGNC:2
    label: GENE2
"""


def edges_for(output: str, template: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "output.yaml"
        path.write_text(output, encoding="utf-8")
        _, edges = parse_yaml_predictions(str(path), str(get_template_path(template)))
    return edges.to_dict(orient="records")


class TestKGXRelations(unittest.TestCase):
    def test_relationship_slot_is_predicate(self):
        """The relationship value goes in the predicate column, the feature in object."""
        edges = edges_for(MIC_OUTPUT, "mic")
        self.assertEqual(1, len(edges))
        edge = edges[0]
        self.assertEqual("CHEBI:12777", edge["subject"])
        self.assertEqual("RO:0002606", edge["predicate"])
        self.assertEqual("HP:0000662", edge["object"])
        self.assertEqual("NutrientToFeatureRelationship", edge["category"])
        self.assertEqual("AUTO:doc1", edge["provided_by"])

    def test_two_entity_relation(self):
        """A relation with two entity slots and no predicate keeps the class as predicate."""
        edges = edges_for(GOCAM_OUTPUT, "gocam")
        self.assertEqual(
            [
                ("HGNC:1", "GeneOrganismRelationship", "NCBITaxon:9606", "0"),
                ("HGNC:2", "GeneOrganismRelationship", "NCBITaxon:10090", "1"),
            ],
            [(e["subject"], e["predicate"], e["object"], e["provided_by"]) for e in edges],
        )
