
# Class: Ingredient




URI: [recipe:Ingredient](http://w3id.org/ontogpt/recipe/Ingredient)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Quantity],[Quantity]<amount%200..1-++[Ingredient],[FoodItem]<food_item%200..1-++[Ingredient],[Recipe]++-%20ingredients%200..*>[Ingredient],[CompoundExpression]^-[Ingredient],[Recipe],[FoodItem],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Quantity],[Quantity]<amount%200..1-++[Ingredient],[FoodItem]<food_item%200..1-++[Ingredient],[Recipe]++-%20ingredients%200..*>[Ingredient],[CompoundExpression]^-[Ingredient],[Recipe],[FoodItem],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞ingredients](recipe__ingredients.md)*  <sub>0..\*</sub>  **[Ingredient](Ingredient.md)**

## Attributes


### Own

 * [➞food_item](ingredient__food_item.md)  <sub>0..1</sub>
     * Description: the food item
     * Range: [FoodItem](FoodItem.md)
 * [➞amount](ingredient__amount.md)  <sub>0..1</sub>
     * Description: the quantity of the ingredient, e.g. 2 lbs
     * Range: [Quantity](Quantity.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | FOODON:00004085 |

