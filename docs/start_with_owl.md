# Starting with OWL

OWL, or Web Ontology Language, is a popular format for ontologies, so what is the best way to start working with OntoGPT if you have an OWL ontology already?

OWL is a data model for expressing ontologies, oriented around set-theoretic logical Axioms. OWL is not strictly an ontology format, but it may be represented in the RDF language, among others. [Much, much more detail here](https://oboacademy.github.io/obook/explanation/owl-format-variants/).

OWL *may* encode a data schema, or it may encode something else. In the latter case, think very carefully about what data you wish to extract and how it relates to what is present in your OWL.

The crucial question is this: does your OWL literally contain a set of terms you wish to ground extractions to, or does it define a set of concepts and their relationships you would like to extract?

For example, let's use this very simple example ontology:

```xml
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:fruits="http://example.org/fruits#">

  <!-- Classes -->
  <owl:Class rdf:about="#Fruit"/>
  <owl:Class rdf:about="#CitrusFruit">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdfs:subClassOf rdf:resource="#Fruit"/>
  </owl:Class>

  <!-- Individuals -->
  <owl:NamedIndividual rdf:about="#Apple">
    <rdf:type rdf:resource="#Fruit"/>
    <rdfs:label>Apple</rdfs:label>
  </owl:NamedIndividual>
  <owl:NamedIndividual rdf:about="#Orange">
    <rdf:type rdf:resource="#CitrusFruit"/>
    <rdfs:label>Orange</rdfs:label>
  </owl:NamedIndividual>

</rdf:RDF>
```

If you want to extract entities from text (and they may be anything - foods, flavors, etc.) and then ground them to individuals in the ontology, then continue to Option 1.

If you want to extract *all* Fruit entities from input text while also recognizing that some of them may be CitrusFruit, then continue to Option 2.

## Option 1 - grounding to a set of terms

You may use an OWL file the same way as any other annotator.

Note that the example ontology above doesn't use prefixes, so let us imagine that each named individual has an identifier like `FRUIT:12345`.

If your input text contains the word "orange", then it will be grounded based on the provided OWL, but any terms *not* in the OWL, like ["snakeskin fruit"](https://en.wikipedia.org/wiki/Salak) will not be grounded unless you provide additional annotators capable of grounding the term.

If your ontology is in `fruit.owl`, then your schema may define a class like this:

```yaml
  Fruit:
    is_a: NamedEntity
    id_prefixes:
      - FRUIT   
    annotations:
      annotators: fruit.owl
```

The OWL file should be in the same path as where you will run `ontogpt` from.

If your ontology is already in the [OBO Foundry](http://obofoundry.org/), then you may also specify the annotator as something like `sqlite:obo:fruit` (that's just an example, but try something like the Food Ontology with `sqlite:obo:foodon` for an equivalent).

## Option 2 - transforming an OWL into OntoGPT schema

This path is a bit more complicated.

If you'd rather use the OWL more like a schema to develop a corresponding extraction schema for OntoGPT, you may be able to do so with the [schema-automator tool](https://github.com/linkml/schema-automator).

After installing the tool, try something like this:

```bash
$ schemauto import-owl fruit.owl
... schema-automator attempts to transform the OWL ...
```

This process may encounter some errors along the way. One frequent issue is that the input ontology may not be in *functional syntax*, but may be converted using the [robot tool](http://robot.obolibrary.org/) like this:

```bash
$ robot convert -i fruit.owl -o fruit.ofn
... a magical transformation happens ...
$ schemauto import-owl fruit.ofn
```

The process may still go poorly if the input ontology is heavily dependent on imports.

If everything goes well, however, you should get a LinkML YAML version of the ontology. It will still require addition of `description` and `annotation` slots to each class before it will be useful for extraction operations.

Overall, you may find that it is easier to modify an existing OntoGPT schema to fit your schema.
