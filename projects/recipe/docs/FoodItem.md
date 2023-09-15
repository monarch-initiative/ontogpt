
# Class: FoodItem




URI: [recipe:FoodItem](http://w3id.org/ontogpt/recipe/FoodItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[FoodType],[FoodType]<food%200..1-%20[FoodItem&#124;state:string%20%3F],[Ingredient]++-%20food_item%200..1>[FoodItem],[Step]++-%20inputs%200..*>[FoodItem],[Step]++-%20outputs%200..*>[FoodItem],[CompoundExpression]^-[FoodItem],[Step],[Ingredient],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[FoodType],[FoodType]<food%200..1-%20[FoodItem&#124;state:string%20%3F],[Ingredient]++-%20food_item%200..1>[FoodItem],[Step]++-%20inputs%200..*>[FoodItem],[Step]++-%20outputs%200..*>[FoodItem],[CompoundExpression]^-[FoodItem],[Step],[Ingredient],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞food_item](ingredient__food_item.md)*  <sub>0..1</sub>  **[FoodItem](FoodItem.md)**
 *  **None** *[➞inputs](step__inputs.md)*  <sub>0..\*</sub>  **[FoodItem](FoodItem.md)**
 *  **None** *[➞outputs](step__outputs.md)*  <sub>0..\*</sub>  **[FoodItem](FoodItem.md)**

## Attributes


### Own

 * [➞food](foodItem__food.md)  <sub>0..1</sub>
     * Description: the food item
     * Range: [FoodType](FoodType.md)
 * [➞state](foodItem__state.md)  <sub>0..1</sub>
     * Description: the state of the food item (e.g. chopped, diced)
     * Range: [String](types/String.md)
