# OWL Exports

The `extract` command will let you export the results as OWL axioms, utilizing [linkml-owl](https://linkml.io/linkml-owl) mappings in the schema.

Ex.:

```bash
ontogpt extract -t recipe -i recipe-spaghetti.txt -o recipe-spaghetti.owl -O owl
```

[src/ontogpt/templates/recipe.yaml](src/ontogpt/templates/recipe.yaml) is an example schema that uses linkml-owl mappings.

See the [Makefile](Makefile) for a full pipeline that involves using robot to extract a subset of FOODON
and merge in the extracted results. This uses [recipe-scrapers](https://github.com/hhursev/recipe-scrapers).

OWL output: [recipe-all-merged.owl](tests/output/owl/merged/recipe-all-merged.owl)

Classification:

![OWL in the Protege editor](https://user-images.githubusercontent.com/50745/230427663-20d845e9-f1d5-490e-b1ad-cdccdd0dca70.png "OWL in the Protege editor")
