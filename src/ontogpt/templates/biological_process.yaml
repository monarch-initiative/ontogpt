id: https://w3id.org/ontogpt/biological_process
name: biological-process-template
title: Biological Process Template
description: >-
  A template for GO-CAMs
license: https://creativecommons.org/publicdomain/zero/1.0/
prefixes:
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  CHEBI: http://purl.obolibrary.org/obo/CHEBI_
  CL: http://purl.obolibrary.org/obo/CL_
  GO: http://purl.obolibrary.org/obo/GO_
  HGNC: http://identifiers.org/hgnc/
  bp: http://w3id.org/ontogpt/biological-process-template
  linkml: https://w3id.org/linkml/

default_prefix: bp
default_range: string

imports:
  - linkml:types
  - core

classes:
  BiologicalProcess:
    tree_root: true
    is_a: NamedEntity
    attributes:
      label:
        description: the name of the biological process
      description:
        description: a textual description of the biological process
      synonyms:
        description: alternative names of the biological process
        multivalued: true
      subclass_of:
        description: the category to which this biological process belongs
        range: BiologicalProcess
      inputs:
        description: the inputs of the biological process
        multivalued: true
        range: ChemicalEntity
      outputs:
        description: the outputs of the biological process
        multivalued: true
        range: ChemicalEntity
      steps:
        description: the steps involved in this biological process
        multivalued: true
        range: MolecularActivity
      genes:
        range: Gene
        multivalued: true
      gene_activities:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship

  Gene:
    is_a: NamedEntity
    id_prefixes:
      - HGNC
    annotations:
      annotators: sqlite:obo:hgnc

  CellType:
    is_a: NamedEntity
    id_prefixes:
      - CL
    annotations:
      annotators: sqlite:obo:cl

  MolecularActivity:
    is_a: NamedEntity
    id_prefixes:
      - GO
    annotations:
      annotators: sqlite:obo:go

  ChemicalEntity:
    is_a: NamedEntity
    id_prefixes:
      - CHEBI
    annotations:
      annotators: sqlite:obo:chebi

  GeneMolecularActivityRelationship:
    attributes:
      gene:
        range: Gene
      molecular_activity:
        range: MolecularActivity
