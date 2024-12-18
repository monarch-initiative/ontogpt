# Custom Schemas

## Build a custom schema

Define a schema (using a subset of [LinkML](https://linkml.io)) that describes the structure in which you want to extract knowledge from your text.

There are a number of pre-defined LinkML data models already developed here - [src/ontogpt/templates/](src/ontogpt/templates/) which you can use as reference when creating your own data models.

### The header

The header of the schema defines metadata, parameters instructing LinkML to interpret prefixes in specific ways, and names of imports.

You will find these fields in the schema header:

* `id`: A unique identifier for the schema. These may take the form of W3IDs like `http://w3id.org/ontogpt/schemaname`.
* `name`: Name of the schema. Should resemble the filename.
* `title`: Title of the schema for human readability.
* `description`: A human readable description of the schema. Detail is welcome!
* `license`: A license indicating reusability of the schema. We prefer a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/).
* `prefixes`: This is a list (actually a dictionary, as each item contains a key and a value) of short prefixes for the identifier namespaces used in the schema along with their corresponding identifier prefixes. At minimum, this shoulc include `linkml: https://w3id.org/linkml/` and the prefix for your schema itself. If the schema is named `salmon`, this will be something like `salmon: http://w3id.org/ontogpt/salmon/`. If you're using Gene Ontology identifiers, specify their prefixes as `GO: http://purl.obolibrary.org/obo/GO_`, because each Gene Ontology term has an identifier prefixed with `GO:`.
* `default_prefix`: This is the prefix for your schema. It should match what you used in the `prefixes` list, so following the above example, that would be `salmon`.
* `default_range`: This is the default data type LinkML will assume each class should be unless specified otherwise. Using `string` is usually safe.

* `imports`: A list of other schemas to import types from. These may be any schemas in the same directory (e.g., if you have another schema named `francine` then you may simply include `francine` in the list of imports) but note that LinkML will raise an error if multiple classes have the same name across the imports. Minimally, this list should include `linkml:types` and `core` to import the base LinkML data types and the generic OntoGPT classes, respectively.

An example:

```yaml
id: http://w3id.org/ontogpt/gocam
name: gocam-template
title: GO-CAM Template
description: >-
  A template for GO-CAMs
license: https://creativecommons.org/publicdomain/zero/1.0/
prefixes:
  linkml: https://w3id.org/linkml/
  gocam: http://w3id.org/ontogpt/gocam/
  GO: http://purl.obolibrary.org/obo/GO_
  CL: http://purl.obolibrary.org/obo/CL_

default_prefix: gocam
default_range: string

imports:
  - linkml:types
  - core
```

### The classes

The classes in the schema define the "things" you are interested in extracting. LinkML doesn't make many assumptions about the difference between a class and a relationship, a node and an edge, or a relation and a property. It's designed to be flexibile enough to handle a variety of data models.

The start of this section is indicated by `classes:`.

A minimal class may look like this:

```yaml
  ClassName:
    is_a: NamedEntity
    attributes:
      entity:
        range: string
        description: >- 
          A named entity.
```

In practice, this class won't do much, as it doesn't contain much for OntoGPT to work with or many instructions to form an LLM prompt out of. And that's fine, because we can do more.

These fields may be used in classes:

* `is_a`: This describes a hierarchical structure, so the value of this slot is the name of a LinkML class. `NamedEntity` is defined in OntoGPT's core schema and is will ensure extracted objects of this class have both unique identifiers and human readable labels.
* `tree_root`: If `true`, this class will be treated as the root of the data hierarchy. If you're planning to extract specific objects from a full text document, for example, it may be useful to define a class for the document to contain its metadata. This parent class could then be the `tree_root`.
* `attributes`: This slot defines all class attributes, and in OntoGPT, that means each will be included in a prompt for the LLM. Each attribute should have a unique, lowercased name. Attributes have their own slots:
  * `description`: The attribute description to be *passed as part of the prompt*. This should describe the attribute and how it should be formatted in the generated output. Do not include references to specific identifiers here.
  * `multivalued`: If `true`, any value for this attribute will be interpreted as a list. This is cruical if you expect multiple values in the extracted output and should be reflected in the description by indicating how each value should be separated. OntoGPT prefers semicolons.
  * `range`: The class to restrict the object to. This may be an abstract data type like `string` or another class defined elsewhere in your schema, like `Gene` in the example below.
* `id_prefixes`: A list of identifiers to ground values of this class to. Usually specific to a class rather than an attribute. Use capitalized forms and omit the colon. If you want to ground to MeSH terms, for example, include the prefix `MESH`.
* `annotations`: This slot contains specific instructions for OntoGPT in its annotation and grounding operations. The heading `annotators`, placed under this slot, must contain a comma separated list of value annotators provided by the Ontology Access Kit (OAK). [In OAK these are called *implementations* or *adapters* and there are many of them available.](https://incatools.github.io/ontology-access-kit/packages/implementations/index.html). Annotators are responsible for bridging the gap between raw text and unique identifier, though that process may involve searching a combination of term lists along with their synonyms and equivalents.
  * OBO Foundry ontologies make great annotators. To use CHEBI for chemical names, for example, use the annotator `sqlite:obo:chebi` and include `CHEBI` in the `id_prefixes` list.
  * Ontologies in BioPortal work well, too. They may be specified with the BioPortal ID. To use the EnvThes ecological thesaurus, for example, use the annotator `bioportal:ENVTHES` and the prefix `ENVTHES`.
* `slot_usage`: This slot can contain rules about how another slot may be restricted. In the example below, `GeneLocation` has values for its `id` slot restricted to values within two different *enums*. See the next section for more information on how to use enums.

An example, continuing from where the header left off:

```yaml
classes:
  GoCamAnnotations:
    tree_root: true
    attributes:
      genes:
        description: semicolon-separated list of genes
        multivalued: true
        range: Gene
      organisms:
        description: semicolon-separated list of organism taxons
        multivalued: true
        range: Organism
      gene_organisms:
        annotations:
          prompt: semicolon-separated list of asterisk separated gene to organism relationships
        multivalued: true
        range: GeneOrganismRelationship
      activities:
        description: semicolon-separated list of molecular activities
        multivalued: true
        range: MolecularActivity
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
      cellular_processes:
        description: semicolon-separated list of cellular processes
        multivalued: true
        range: CellularProcess
      pathways:
        description: semicolon-separated list of pathways
        multivalued: true
        range: Pathway
      gene_gene_interactions:
        description: semicolon-separated list of gene to gene interactions
        multivalued: true
        range: GeneGeneInteraction
      gene_localizations:
        description: >-
          semicolon-separated list of genes plus their location in the cell;
          for example, "gene1 / cytoplasm; gene2 / mitochondrion"
        multivalued: true
        range: GeneSubcellularLocalizationRelationship

  Gene:
    is_a: NamedEntity
    id_prefixes:
      - HGNC
      - PR
      - UniProtKB
    annotations:
      annotators: gilda:, bioportal:hgnc-nr
  Pathway:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - PW
    annotations:
      annotators: sqlite:obo:go, sqlite:obo:pw
  CellularProcess:
    is_a: NamedEntity
    id_prefixes:
      - GO
    annotations:
      annotators: sqlite:obo:go
  MolecularActivity:
    is_a: NamedEntity
    id_prefixes:
      - GO
    annotations:
      annotators: sqlite:obo:go
  GeneLocation:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - CL
      - UBERON
    annotations:
      annotators: "sqlite:obo:go, sqlite:obo:cl"
    slot_usage:
      id:
        values_from:
          - GOCellComponentType
          - CellType
  Organism:
    is_a: NamedEntity
    id_prefixes:
      - NCBITaxon
      - EFO
    annotations:
      annotators: gilda:, sqlite:obo:ncbitaxon
  Molecule:
    is_a: NamedEntity
    id_prefixes:
      - CHEBI
      - PR
    annotations:
      annotators: gilda:, sqlite:obo:chebi

  GeneOrganismRelationship:
    is_a: CompoundExpression
    attributes:
      gene:
        range: Gene
      organism:
        range: Organism

  GeneMolecularActivityRelationship:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
        annotations:
          prompt: the name of the gene in the pair. This comes first.
      molecular_activity:
        range: MolecularActivity
        annotations:
          prompt: the name of the molecular function in the pair. This comes second. May be a GO term.

  GeneMolecularActivityRelationship2:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
        annotations:
          prompt: the name of the gene.
      molecular_activity:
        range: MolecularActivity
        annotations:
          prompt: the name of the molecular activity, for example, ubiquitination. May be a GO term.
      target:
        range: Molecule
        annotations:
          prompt: the name of the molecular entity that is the target of the molecular activity.

  GeneSubcellularLocalizationRelationship:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
      location:
        range: GeneLocation

  GeneGeneInteraction:
    is_a:   CompoundExpression
    attributes:
      gene1:
        range: Gene
      gene2:
        range: Gene
```

### Enums

LinkML supports defining *enums*, or sets of values. In OntoGPT this allows schemas to work with subsets of identifiers. Enums have their own hierarchy. In the example below, the `reachable_from` slot is used to define sets of values: in `GOCellComponentType` these are all children of the GO term with the ID `GO:0005575` (cellular component), so restricting a set of identifiers based on this enum will ensure they all correspond to cellular components.

Example, starting where the classes left off above:

```yaml
enums:

  GeneLocationEnum:
    inherits:
      - GOCellComponent
      - CellType

  GOCellComponentType:
    reachable_from:
      source_ontology: obo:go
      source_nodes:
        - GO:0005575 ## cellular_component
  CellType:
    reachable_from:
      source_ontology: obo:cl
      source_nodes:
        - CL:0000000 ## cell
```

### Schema design tips

It helps to have an understanding of the [LinkML](https://linkml.io) schema language, but it should be possible to define your own schemas using the examples in [src/ontogpt/templates](src/ontogpt/templates/) as a guide.

* Prompt hints can be specified using the `prompt` annotation (otherwise description is used)
* Multivalued fields are supported
* The default range is string — these are not grounded. Ex.: disease name, synonyms
* Define a class for each `NamedEntity`
* For any `NamedEntity`, you can specify a preferred annotator using the `annotators` annotation

We recommend following an established schema like [BioLink Model](https://github.com/biolink/biolink-model), but you can define your own.

Once you have defined your own schema / data model and placed in the correct directory, you can run the `extract` command.

Ex.:

```bash
ontogpt extract -t mendelian_disease.MendelianDisease -i marfan-wikipedia.txt
```

OntoGPT-specific extensions are specified as *annotations*.

You can specify a set of annotators for a field using the `annotators` annotation.

Ex.:

```yaml
  Gene:
    is_a: NamedThing
    id_prefixes:
      - HGNC
    annotations:
      annotators: gilda:, bioportal:hgnc-nr, obo:pr
```

The annotators are applied in order.

Additionally, when performing grounding, the following measures can be taken to improve accuracy:

* Specify the valid set of ID prefixes using `id_prefixes`
* Some vocabularies have structural IDs that are amenable to regexes, you can specify these using `pattern`
* You can make use of `values_from` slot to specify a [Dynamic Value Set](https://linkml.io/linkml/schemas/enums.html#dynamic-enums)
  * For example, you can constrain the set of valid locations for a gene product to be subclasses of `cellular_component` in GO or `cell` in CL

Ex.:

```yaml
classes:
  ...
  GeneLocation:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - CL
    annotations:
      annotators: "sqlite:obo:go, sqlite:obo:cl"
    slot_usage:
      id:
        values_from:
          - GOCellComponentType
          - CellType

enums:
  GOCellComponentType:
    reachable_from:
      source_ontology: obo:go
      source_nodes:
        - GO:0005575 ## cellular_component
  CellType:
    reachable_from:
      source_ontology: obo:cl
      source_nodes:
        - CL:0000000 ## cell
```

#### Multiple levels of nesting

Currently no more than two levels of nesting are recommended.

If a field has a range which is itself a class and not a primitive, it will attempt to nest.

Ex. the `gocam` schema has an attribute:

```yaml
  attributes:
      ...
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
```

The range `GeneMolecularActivityRelationship` has been specified *inline*, so it will nest.

The generated prompt is:

```bash
gene_functions : <semicolon-separated list of gene to molecular activities relationships>
```

The output of this is then passed through further SPIRES iterations.

#### Text length limit

LLMs have context sizes limiting the combined length of their inputs and outputs. 

To see the token limit for each model, use `ontogpt list-models`. The Max Tokens value will be in the fourth column.

## Advanced functionality with linkml-owl

A LinkML schema used in OntoGPT may include annotations describing how each component relates to OWL syntax.

This level of detail may be necessary if your data model includes complex logic beyond simple hierarchical relationships.

For example, if you are extracting details of chemical reactions, it may be necessary to keep track of details like stoichiometry or charge. [See a relevant example here](https://linkml.io/linkml-owl/templates/).

Incorporating OWL annotations into the custom schema (remember to export using the `-O owl` option) also supports importing the results into an ontology editor like Protege, at which point it may be reasoned over.

The `recipe` template in OntoGPT incorporates several OWL annotations:

```yaml
classes:
  Recipe:
    tree_root: true
    close_mappings:
      - FOODON:00004081
    attributes:
      url:
        identifier: true
        range: uriorcurie
        slot_uri: rdf:Resource
        annotations:
          prompt.skip: true
      label:
        description: the name of the recipe
        slot_uri: rdfs:label
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
      description:
        description: a brief textual description of the recipe
        slot_uri: dcterms:description
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
      categories:
        description: a semicolon separated list of the categories to which this recipe belongs
        range: RecipeCategory
        multivalued: true
        slot_uri: dcterms:subject
        annotations:
          owl: AnnotationAssertion
      ingredients:
        description: a semicolon separated list of the ingredients plus quantities of the recipe
        multivalued: true
        range: Ingredient
        slot_uri: FOODON:00002420
        annotations:
          owl: ObjectProperty, ObjectSomeValuesFrom
      steps:
        description: a semicolon separated list of the individual steps involved in this recipe
        multivalued: true
        range: Step
        annotations:
          owl: ObjectProperty, ObjectSomeValuesFrom
    annotations:
      owl: Class
      owl.template: |
        EquivalentClasses(
          {{url}}
          ObjectIntersectionOf(
            recipe:Recipe
            
            {% for step in steps %}
            ObjectSomeValuesFrom(
              recipe:steps
              {{tr(step)}}
            )
            {% endfor %}
            {% for ingredient in ingredients %}
            ObjectSomeValuesFrom(
              FOODON:00002420
              {{tr(ingredient)}}
            )
            {% endfor %}
          )
        )
...
```

Several of the slots above, like `close_mappings` and `slot_uri`, aren't exclusive to OWL but define the parts of this data model in terms of existing vocabularies, so the schema and any extracted results will be more compatible with other models and methods. Here, `close_mappings` is used to show that the `Recipe` class is close but not necessarily identical to `FOODON:00004081`, or "food recipe".

The `owl` slot under `annotations` for these attributes defines one or more corresponding OWL axiom types. Because the `label` attribute may be `AnnotationProperty, AnnotationAssertion` in OWL ([see the OWL2 syntax on Annotations](https://www.w3.org/TR/owl2-syntax/#Annotations)) we know it can be applied as a property for something else, like an axiom or a specific entity with an IRI. This is how the `rdfs:label` annotation property usually works so this isn't surprising.

The `owl.template` slot defines template logic relating a Recipe to its component objects: steps and ingredients. It begins with an `EquivalentClasses` axiom to define the identifier of the recipe, which we assume to be a URL, as identical to the class expression in subsequent lines. Specifically, that `Recipe` must include both a series of steps (e.g., "fry", "chop", etc.) and a series of ingredients. The ingredients relate to the recipe through the property `FOODON:00002420`, or "has ingredient".

Note that everything in {curly brackets} is a template of some kind. The Jinja template system is used in the example in lines like `{% for step in steps %}` where a loop is used. Template slots like `{{url}}` may be accessed directly with their names. So what makes `{{tr(step)}}` different from `{{step}}`? The `tr()` function used here translates its input into an OWL entity so it may be used to generate valid OWL axioms.

See also: the [documentation page on OWL exports](owl_exports.md) and the [linkml-owl documentation](https://linkml.io/linkml-owl/).

## Using a custom schema

You may then use the schema like any other. Pass the path to your schema to the `--template/-t` option.

For example, if your schema is named `albatross.yaml`, then an extract command is:

```bash
ontogpt extract -t albatross.yaml -i input.txt
```

Running this (or any other command including your custom schema) will install it for future use with OntoGPT, so in subsequent commands it can be referred to by its name (e.g., `albatross`, without the file extension or a full filepath).
