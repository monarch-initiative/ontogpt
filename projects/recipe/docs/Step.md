
# Class: Step




URI: [recipe:Step](http://w3id.org/ontogpt/recipe/Step)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UtensilType],[UtensilType]<utensils%200..*-%20[Step],[FoodItem]<outputs%200..*-++[Step],[FoodItem]<inputs%200..*-++[Step],[Action]<action%200..1-%20[Step],[Recipe]++-%20steps%200..*>[Step],[CompoundExpression]^-[Step],[Recipe],[FoodItem],[CompoundExpression],[Action])](https://yuml.me/diagram/nofunky;dir:TB/class/[UtensilType],[UtensilType]<utensils%200..*-%20[Step],[FoodItem]<outputs%200..*-++[Step],[FoodItem]<inputs%200..*-++[Step],[Action]<action%200..1-%20[Step],[Recipe]++-%20steps%200..*>[Step],[CompoundExpression]^-[Step],[Recipe],[FoodItem],[CompoundExpression],[Action])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞steps](recipe__steps.md)*  <sub>0..\*</sub>  **[Step](Step.md)**

## Attributes


### Own

 * [➞action](step__action.md)  <sub>0..1</sub>
     * Description: the action taken in this step (e.g. mix, add)
     * Range: [Action](Action.md)
 * [➞inputs](step__inputs.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of the inputs of this step
     * Range: [FoodItem](FoodItem.md)
 * [➞outputs](step__outputs.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of the outputs of this step
     * Range: [FoodItem](FoodItem.md)
 * [➞utensils](step__utensils.md)  <sub>0..\*</sub>
     * Description: the kitchen utensil used in this step (e.g. pan, bowl)
     * Range: [UtensilType](UtensilType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | FOODON:00004087 |

