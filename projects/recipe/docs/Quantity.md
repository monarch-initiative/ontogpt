
# Class: Quantity




URI: [recipe:Quantity](http://w3id.org/ontogpt/recipe/Quantity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[Unit]<unit%200..1-%20[Quantity&#124;value:string%20%3F],[Ingredient]++-%20amount%200..1>[Quantity],[CompoundExpression]^-[Quantity],[Ingredient],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[Unit]<unit%200..1-%20[Quantity&#124;value:string%20%3F],[Ingredient]++-%20amount%200..1>[Quantity],[CompoundExpression]^-[Quantity],[Ingredient],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞amount](ingredient__amount.md)*  <sub>0..1</sub>  **[Quantity](Quantity.md)**

## Attributes


### Own

 * [➞value](quantity__value.md)  <sub>0..1</sub>
     * Description: the value of the quantity
     * Range: [String](types/String.md)
 * [➞unit](quantity__unit.md)  <sub>0..1</sub>
     * Description: the unit of the quantity, e.g. grams, cups, etc.
     * Range: [Unit](Unit.md)
