
# Class: Measurement




URI: [eg:Measurement](http://w3id.org/ontogpt/environmental-metagenome/Measurement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[Unit]<unit%200..1-%20[Measurement&#124;value:string%20%3F],[Study]++-%20measurements%200..*>[Measurement],[CompoundExpression]^-[Measurement],[Study],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[Unit]<unit%200..1-%20[Measurement&#124;value:string%20%3F],[Study]++-%20measurements%200..*>[Measurement],[CompoundExpression]^-[Measurement],[Study],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞measurements](study__measurements.md)*  <sub>0..\*</sub>  **[Measurement](Measurement.md)**

## Attributes


### Own

 * [➞value](measurement__value.md)  <sub>0..1</sub>
     * Description: the value of the measurement
     * Range: [String](types/String.md)
 * [➞unit](measurement__unit.md)  <sub>0..1</sub>
     * Description: the unit of the measurement
     * Range: [Unit](Unit.md)
