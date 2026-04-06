# None

## Input

_According to the American Psychiatric Association, second-generation (atypical) antipsychotics (SGAs)—with the exception of clozapine—are the agents of choice for first-line treatment of schizophrenia.16,25 Clozapine is not recommended because of its risk of agranulocytosis.2 SGAs are usually preferred over first-generation (typical) antipsychotics (FGAs) because they are associated with fewer extrapyramidal symptoms.2 However, SGAs tend to have metabolic side effects, such as weight gain, hyperlipidemia, and diabetes mellitus.26 These adverse effects can contribute to the increased risk of cardiovascular mortality observed in schizophrenia patients.26_

__

_The Texas Medication Algorithm Project (TMAP) has provided a six-stage pharmacotherapeutic algorithm for the treatment of schizophrenia. Stage 1 is first-line monotherapy with an SGA. If the patient shows little or no response, he or she should proceed to stage 2, which consists of monotherapy with either another SGA or an FGA. If there is still no response, the patient should move to stage 3, which consists of clozapine monotherapy with monitoring of the white blood cell (WBC) count.24 If agranulocytosis occurs, clozapine should be discontinued. If stage-3 therapy fails to elicit a response, the patient should proceed to stage 4, which combines clozapine with an FGA, an SGA, or electroconvulsive therapy (ECT).24 If the patient still shows no response to treatment, stage 5 calls for monotherapy with an FGA or an SGA that has not been tried.24 Finally, if stage 5 treatment is unsuccessful, stage 6 consists of combination therapy with an SGA, an FGA, ECT, and/or a mood stabilizer._

## Results



### disease


- schizophrenia [MONDO:0005090](https://bioregistry.io/MONDO:0005090)


### drugs


- clozapine [CHEBI:3766](https://bioregistry.io/CHEBI:3766)


### treatments


- second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- first-generation antipsychotics (FGAs) [NCIT:C150227](https://bioregistry.io/NCIT:C150227)

- electroconvulsive therapy (ECT) [NCIT:C100422](https://bioregistry.io/NCIT:C100422)

- mood stabilizer [AUTO:mood%20stabilizer](https://bioregistry.io/AUTO:mood%20stabilizer)


### contraindications


- clozapine [NCIT:C28936](https://bioregistry.io/NCIT:C28936)


### treatment_mechanisms


- treatment:
  - second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- mechanism:
  - fewer extrapyramidal symptoms [AUTO:fewer%20extrapyramidal%20symptoms](https://bioregistry.io/AUTO:fewer%20extrapyramidal%20symptoms)


- treatment:
  - first-generation antipsychotics (FGAs) [NCIT:C150227](https://bioregistry.io/NCIT:C150227)

- mechanism:
  - not specified [NCIT:C149701](https://bioregistry.io/NCIT:C149701)


- treatment:
  - clozapine [NCIT:C28936](https://bioregistry.io/NCIT:C28936)

- mechanism:
  - not specified [NCIT:C149701](https://bioregistry.io/NCIT:C149701)


- treatment:
  - electroconvulsive therapy (ECT) [NCIT:C100422](https://bioregistry.io/NCIT:C100422)

- mechanism:
  - not specified [NCIT:C149701](https://bioregistry.io/NCIT:C149701)


- treatment:
  - mood stabilizer [AUTO:mood%20stabilizer](https://bioregistry.io/AUTO:mood%20stabilizer)

- mechanism:
  - not specified [NCIT:C149701](https://bioregistry.io/NCIT:C149701)



### treatment_efficacies


- treatment:
  - second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- efficacy:
  - first-line treatment


- treatment:
  - clozapine [NCIT:C28936](https://bioregistry.io/NCIT:C28936)

- efficacy:
  - effective at stage 3


- treatment:
  - electroconvulsive therapy (ECT) [NCIT:C100422](https://bioregistry.io/NCIT:C100422)

- efficacy:
  - effective at stage 4 and 6


- treatment:
  - first-generation antipsychotics (FGAs) [NCIT:C150227](https://bioregistry.io/NCIT:C150227)

- efficacy:
  - effective at stage 5 and 6


- treatment:
  - mood stabilizer [AUTO:mood%20stabilizer](https://bioregistry.io/AUTO:mood%20stabilizer)

- efficacy:
  - effective at stage 6



### treatment_adverse_effects


- treatment:
  - second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- adverse_effects:
  - weight gain [HP:0004324](https://bioregistry.io/HP:0004324)


- treatment:
  - second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- adverse_effects:
  - hyperlipidemia [HP:0003077](https://bioregistry.io/HP:0003077)


- treatment:
  - second-generation antipsychotics (SGAs) [NCIT:C210849](https://bioregistry.io/NCIT:C210849)

- adverse_effects:
  - diabetes mellitus [HP:0000819](https://bioregistry.io/HP:0000819)


- treatment:
  - clozapine [NCIT:C28936](https://bioregistry.io/NCIT:C28936)

- adverse_effects:
  - agranulocytosis [HP:0012234](https://bioregistry.io/HP:0012234)




YAML:

<details>
```yaml
extracted_object:
  contraindications:
  - NCIT:C28936
  disease: MONDO:0005090
  drugs:
  - CHEBI:3766
  treatment_adverse_effects:
  - adverse_effects:
    - HP:0004324
    treatment: NCIT:C210849
  - adverse_effects:
    - HP:0003077
    treatment: NCIT:C210849
  - adverse_effects:
    - HP:0000819
    treatment: NCIT:C210849
  - adverse_effects:
    - HP:0012234
    treatment: NCIT:C28936
  treatment_efficacies:
  - efficacy: first-line treatment
    treatment: NCIT:C210849
  - efficacy: effective at stage 3
    treatment: NCIT:C28936
  - efficacy: effective at stage 4 and 6
    treatment: NCIT:C100422
  - efficacy: effective at stage 5 and 6
    treatment: NCIT:C150227
  - efficacy: effective at stage 6
    treatment: AUTO:mood%20stabilizer
  treatment_mechanisms:
  - mechanism: AUTO:fewer%20extrapyramidal%20symptoms
    treatment: NCIT:C210849
  - mechanism: NCIT:C149701
    treatment: NCIT:C150227
  - mechanism: NCIT:C149701
    treatment: NCIT:C28936
  - mechanism: NCIT:C149701
    treatment: NCIT:C100422
  - mechanism: NCIT:C149701
    treatment: AUTO:mood%20stabilizer
  treatments:
  - NCIT:C210849
  - NCIT:C150227
  - NCIT:C100422
  - AUTO:mood%20stabilizer
input_id: null
input_text: "According to the American Psychiatric Association, second-generation\
  \ (atypical) antipsychotics (SGAs)\u2014with the exception of clozapine\u2014are\
  \ the agents of choice for first-line treatment of schizophrenia.16,25 Clozapine\
  \ is not recommended because of its risk of agranulocytosis.2 SGAs are usually preferred\
  \ over first-generation (typical) antipsychotics (FGAs) because they are associated\
  \ with fewer extrapyramidal symptoms.2 However, SGAs tend to have metabolic side\
  \ effects, such as weight gain, hyperlipidemia, and diabetes mellitus.26 These adverse\
  \ effects can contribute to the increased risk of cardiovascular mortality observed\
  \ in schizophrenia patients.26\n\nThe Texas Medication Algorithm Project (TMAP)\
  \ has provided a six-stage pharmacotherapeutic algorithm for the treatment of schizophrenia.\
  \ Stage 1 is first-line monotherapy with an SGA. If the patient shows little or\
  \ no response, he or she should proceed to stage 2, which consists of monotherapy\
  \ with either another SGA or an FGA. If there is still no response, the patient\
  \ should move to stage 3, which consists of clozapine monotherapy with monitoring\
  \ of the white blood cell (WBC) count.24 If agranulocytosis occurs, clozapine should\
  \ be discontinued. If stage-3 therapy fails to elicit a response, the patient should\
  \ proceed to stage 4, which combines clozapine with an FGA, an SGA, or electroconvulsive\
  \ therapy (ECT).24 If the patient still shows no response to treatment, stage 5\
  \ calls for monotherapy with an FGA or an SGA that has not been tried.24 Finally,\
  \ if stage 5 treatment is unsuccessful, stage 6 consists of combination therapy\
  \ with an SGA, an FGA, ECT, and/or a mood stabilizer."
input_title: null
named_entities:
- id: MONDO:0005090
  label: schizophrenia
  original_spans:
  - 187:199
  - 635:647
  - 784:796
- id: CHEBI:3766
  label: clozapine
  original_spans:
  - 124:132
  - 207:215
  - 1077:1085
  - 1181:1189
  - 1316:1324
- id: NCIT:C210849
  label: second-generation antipsychotics (SGAs)
  original_spans: []
- id: NCIT:C150227
  label: first-generation antipsychotics (FGAs)
  original_spans: []
- id: NCIT:C100422
  label: electroconvulsive therapy (ECT)
  original_spans:
  - 1350:1380
- id: AUTO:mood%20stabilizer
  label: mood stabilizer
  original_spans:
  - 1639:1653
- id: NCIT:C28936
  label: clozapine
  original_spans:
  - 124:132
  - 207:215
  - 1077:1085
  - 1181:1189
  - 1316:1324
- id: AUTO:fewer%20extrapyramidal%20symptoms
  label: fewer extrapyramidal symptoms
  original_spans:
  - 391:419
- id: NCIT:C149701
  label: not specified
  original_spans: []
- id: HP:0004324
  label: weight gain
  original_spans:
  - 482:492
- id: HP:0003077
  label: hyperlipidemia
  original_spans:
  - 495:508
- id: HP:0000819
  label: diabetes mellitus
  original_spans:
  - 515:531
- id: HP:0012234
  label: agranulocytosis
  original_spans:
  - 259:273
  - 1157:1171
prompt: 'Split the following piece of text into fields in the following format:


  treatment: <the value for treatment>

  adverse_effects: <semicolon-separated list of adverse_effectss>



  Text:

  clozapineagranulocytosis


  ===


  '
raw_completion_output: "disease: schizophrenia  \ndrugs: clozapine  \ntreatments:\
  \ second-generation antipsychotics (SGAs); first-generation antipsychotics (FGAs);\
  \ electroconvulsive therapy (ECT); mood stabilizer  \ncontraindications: clozapine\
  \  \ntreatment_mechanisms: second-generation antipsychotics (SGAs)*fewer extrapyramidal\
  \ symptoms; first-generation antipsychotics (FGAs)*not specified; clozapine*not\
  \ specified; electroconvulsive therapy (ECT)*not specified; mood stabilizer*not\
  \ specified  \ntreatment_efficacies: second-generation antipsychotics (SGAs)*first-line\
  \ treatment; clozapine*effective at stage 3; electroconvulsive therapy (ECT)*effective\
  \ at stage 4 and 6; first-generation antipsychotics (FGAs)*effective at stage 5\
  \ and 6; mood stabilizer*effective at stage 6  \ntreatment_adverse_effects: second-generation\
  \ antipsychotics (SGAs)*weight gain; second-generation antipsychotics (SGAs)*hyperlipidemia;\
  \ second-generation antipsychotics (SGAs)*diabetes mellitus; clozapine*agranulocytosis\
  \  "

```

</details>


Prompt:

<details>
```
Split the following piece of text into fields in the following format:

treatment: <the value for treatment>
adverse_effects: <semicolon-separated list of adverse_effectss>


Text:
clozapineagranulocytosis

===


```

</details>


Completion:

<details>
```
disease: schizophrenia  
drugs: clozapine  
treatments: second-generation antipsychotics (SGAs); first-generation antipsychotics (FGAs); electroconvulsive therapy (ECT); mood stabilizer  
contraindications: clozapine  
treatment_mechanisms: second-generation antipsychotics (SGAs)*fewer extrapyramidal symptoms; first-generation antipsychotics (FGAs)*not specified; clozapine*not specified; electroconvulsive therapy (ECT)*not specified; mood stabilizer*not specified  
treatment_efficacies: second-generation antipsychotics (SGAs)*first-line treatment; clozapine*effective at stage 3; electroconvulsive therapy (ECT)*effective at stage 4 and 6; first-generation antipsychotics (FGAs)*effective at stage 5 and 6; mood stabilizer*effective at stage 6  
treatment_adverse_effects: second-generation antipsychotics (SGAs)*weight gain; second-generation antipsychotics (SGAs)*hyperlipidemia; second-generation antipsychotics (SGAs)*diabetes mellitus; clozapine*agranulocytosis  
```

</details>
