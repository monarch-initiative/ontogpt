
# Class: Recipe




URI: [recipe:Recipe](http://w3id.org/ontogpt/recipe/Recipe)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Step],[RecipeCategory],[Step]<steps%200..*-++[Recipe&#124;url:uriorcurie;label:string%20%3F;description:string%20%3F],[Ingredient]<ingredients%200..*-++[Recipe],[RecipeCategory]<categories%200..*-%20[Recipe],[Ingredient])](https://yuml.me/diagram/nofunky;dir:TB/class/[Step],[RecipeCategory],[Step]<steps%200..*-++[Recipe&#124;url:uriorcurie;label:string%20%3F;description:string%20%3F],[Ingredient]<ingredients%200..*-++[Recipe],[RecipeCategory]<categories%200..*-%20[Recipe],[Ingredient])

## Attributes


### Own

 * [➞url](recipe__url.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞label](recipe__label.md)  <sub>0..1</sub>
     * Description: the name of the recipe
     * Range: [String](types/String.md)
 * [➞description](recipe__description.md)  <sub>0..1</sub>
     * Description: a brief textual description of the recipe
     * Range: [String](types/String.md)
 * [➞categories](recipe__categories.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of the categories to which this recipe belongs
     * Range: [RecipeCategory](RecipeCategory.md)
 * [➞ingredients](recipe__ingredients.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of the ingredients plus quantities of the recipe
     * Range: [Ingredient](Ingredient.md)
 * [➞steps](recipe__steps.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of the individual steps involved in this recipe
     * Range: [Step](Step.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Close Mappings:** | | FOODON:00004081 |

