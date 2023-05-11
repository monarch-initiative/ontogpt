
# Class: Link




URI: [diag:Link](http://w3id.org/ontogpt/diagnostic_procedure/Link)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Predicate],[LinkedElement],[LinkedElement]<object%200..1-%20[Link],[Predicate]<predicate%200..1-%20[Link],[LinkedElement]<subject%200..1-%20[Link],[DiagnosticProcedure]++-%20links%200..*>[Link],[CompoundExpression]^-[Link],[DiagnosticProcedure],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Predicate],[LinkedElement],[LinkedElement]<object%200..1-%20[Link],[Predicate]<predicate%200..1-%20[Link],[LinkedElement]<subject%200..1-%20[Link],[DiagnosticProcedure]++-%20links%200..*>[Link],[CompoundExpression]^-[Link],[DiagnosticProcedure],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞links](diagnosticProcedure__links.md)*  <sub>0..\*</sub>  **[Link](Link.md)**

## Attributes


### Own

 * [➞subject](link__subject.md)  <sub>0..1</sub>
     * Range: [LinkedElement](LinkedElement.md)
 * [➞predicate](link__predicate.md)  <sub>0..1</sub>
     * Range: [Predicate](Predicate.md)
 * [➞object](link__object.md)  <sub>0..1</sub>
     * Range: [LinkedElement](LinkedElement.md)
