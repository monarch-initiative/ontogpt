# /Users/cjm/repos/ontogpt/tests/input/cases/recipe-spaghetti.txt

## Input

_SIMPLE SPAGHETTI_

__

_DIRECTIONS_

_On medium heat melt the butter and sautee the onion and bell peppers._

_Add the hamburger meat and cook until meat is well done._

_Add the tomato sauce, salt, pepper and garlic powder._

_Salt, pepper and garlic powder can be adjusted to your own tastes._

_Cook noodles as directed._

_Mix the sauce and noodles if you like, I keep them separated._

__

_INGREDIENTS_

_UNITS: US_

_1_

_small onion (chopped)_

_1_

_bell pepper (chopped)_

_2_

_tablespoons garlic powder_

_3_

_tablespoons butter_

_1_

_teaspoon salt_

_1_

_teaspoon pepper_

_2_

_(15 ounce) cans tomato sauce_

_1_

_(16 ounce) box spaghetti noodles_

_1 - 1 1⁄2_

_lb hamburger meat._

__

## Results



### url


- N/A


### label


- Simple Spaghetti


### description


- An easy to make and delicious spaghetti dish.


### categories


- AUTO:Main%20dishes

- AUTO:Italian%20recipes


### ingredients


- food_item:
  - food:
    - AUTO:small%20onion

  - state:
    - chopped


- amount:
  - value:
    - 1

  - unit:
    - AUTO:%28chopped%29



- food_item:
  - food:
    - bell pepper [FOODON:00003485](https://bioregistry.io/FOODON:00003485)

  - state:
    - chopped


- amount:
  - value:
    - 1

  - unit:
    - AUTO:%28chopped%29



- food_item:
  - food:
    - garlic [FOODON:00003582](https://bioregistry.io/FOODON:00003582)

  - state:
    - powder


- amount:
  - value:
    - 2

  - unit:
    - tablespoons [UO:0010042](https://bioregistry.io/UO:0010042)



- food_item:
  - food:
    - butter [FOODON:03310351](https://bioregistry.io/FOODON:03310351)

  - state:
    - None


- amount:
  - value:
    - 3

  - unit:
    - tablespoons [UO:0010042](https://bioregistry.io/UO:0010042)



- food_item:
  - food:
    - AUTO:salt

  - state:
    - None


- amount:
  - value:
    - 1

  - unit:
    - teaspoon [UO:0010040](https://bioregistry.io/UO:0010040)



- food_item:
  - food:
    - pepper [FOODON:00001649](https://bioregistry.io/FOODON:00001649)

  - state:
    - None


- amount:
  - value:
    - 1

  - unit:
    - teaspoon [UO:0010040](https://bioregistry.io/UO:0010040)



- food_item:
  - food:
    - tomato sauce [FOODON:03301217](https://bioregistry.io/FOODON:03301217)

  - state:
    - canned


- amount:
  - value:
    - 2

  - unit:
    - None



- food_item:
  - food:
    - AUTO:1%20%2816%20ounce%29%20box%20spaghetti%20noodles

  - state:
    - uncooked


- amount:
  - value:
    - 1

  - unit:
    - None



- food_item:
  - food:
    - hamburger meat [FOODON:00001282](https://bioregistry.io/FOODON:00001282)

  - state:
    - chopped/diced


- amount:
  - value:
    - 1 - 1 1⁄2

  - unit:
    - AUTO:lb




### steps


- action:
  - AUTO:melt%3B%20saut%C3%A9

- inputs:
  - food:
    - butter [FOODON:03310351](https://bioregistry.io/FOODON:03310351)

  - state:
    - None


  - food:
    - onion [FOODON:03301704](https://bioregistry.io/FOODON:03301704)

  - state:
    - None


  - food:
    - bell pepper [FOODON:00003485](https://bioregistry.io/FOODON:00003485)

  - state:
    - chopped


- outputs:
- utensils:
  - AUTO:pan


- action:
  - AUTO:add%3B%20cook

- inputs:
  - food:
    - hamburger meat [FOODON:00001282](https://bioregistry.io/FOODON:00001282)

  - state:
    - chopped/diced


- outputs:
  - food:
    - AUTO:meat

  - state:
    - well done


- utensils:
  - AUTO:pan


- action:
  - AUTO:add%3B

- inputs:
  - food:
    - tomato [FOODON:03000227](https://bioregistry.io/FOODON:03000227)

  - state:
    - sauce


  - food:
    - AUTO:salt

  - state:
    - None


  - food:
    - pepper [FOODON:00001649](https://bioregistry.io/FOODON:00001649)

  - state:
    - None


  - food:
    - garlic [FOODON:00003582](https://bioregistry.io/FOODON:00003582)

  - state:
    - powder


- outputs:
  - food:
    - AUTO:none

  - state:
    - None


- utensils:
  - AUTO:none


- action:
  - AUTO:adjust

- inputs:
  - food:
    - AUTO:salt

  - state:
    - None


  - food:
    - pepper [FOODON:00001649](https://bioregistry.io/FOODON:00001649)

  - state:
    - None


  - food:
    - garlic [FOODON:00003582](https://bioregistry.io/FOODON:00003582)

  - state:
    - powder


- outputs:
  - food:
    - AUTO:inputs

  - state:
    - adjusted


- utensils:
  - AUTO:none


- action:
  - AUTO:Cook

- inputs:
  - food:
    - noodles [FOODON:03306944](https://bioregistry.io/FOODON:03306944)

  - state:
    - None


- outputs:
  - food:
    - AUTO:as%20directed

  - state:
    - None


- utensils:

- action:
  - AUTO:mix%3B

- inputs:
  - food:
    - sauce [FOODON:03311146](https://bioregistry.io/FOODON:03311146)

  - state:
    - None


  - food:
    - noodles [FOODON:03306944](https://bioregistry.io/FOODON:03306944)

  - state:
    - None


- outputs:
  - food:
    - noodles [FOODON:03306944](https://bioregistry.io/FOODON:03306944)

  - state:
    - +


- utensils:
  - AUTO:none




YAML:

<details>
```yaml
extracted_object:
  categories:
  - AUTO:Main%20dishes
  - AUTO:Italian%20recipes
  description: An easy to make and delicious spaghetti dish.
  ingredients:
  - amount:
      unit: AUTO:%28chopped%29
      value: '1'
    food_item:
      food: AUTO:small%20onion
      state: chopped
  - amount:
      unit: AUTO:%28chopped%29
      value: '1'
    food_item:
      food: FOODON:00003485
      state: chopped
  - amount:
      unit: UO:0010042
      value: '2'
    food_item:
      food: FOODON:00003582
      state: powder
  - amount:
      unit: UO:0010042
      value: '3'
    food_item:
      food: FOODON:03310351
      state: null
  - amount:
      unit: UO:0010040
      value: '1'
    food_item:
      food: AUTO:salt
      state: null
  - amount:
      unit: UO:0010040
      value: '1'
    food_item:
      food: FOODON:00001649
      state: null
  - amount:
      unit: null
      value: '2'
    food_item:
      food: FOODON:03301217
      state: canned
  - amount:
      unit: null
      value: '1'
    food_item:
      food: AUTO:1%20%2816%20ounce%29%20box%20spaghetti%20noodles
      state: uncooked
  - amount:
      unit: AUTO:lb
      value: "1 - 1 1\u20442"
    food_item:
      food: FOODON:00001282
      state: chopped/diced
  label: Simple Spaghetti
  steps:
  - action: AUTO:melt%3B%20saut%C3%A9
    inputs:
    - food: FOODON:03310351
      state: null
    - food: FOODON:03301704
      state: null
    - food: FOODON:00003485
      state: chopped
    outputs: []
    utensils:
    - AUTO:pan
  - action: AUTO:add%3B%20cook
    inputs:
    - food: FOODON:00001282
      state: chopped/diced
    outputs:
    - food: AUTO:meat
      state: well done
    utensils:
    - AUTO:pan
  - action: AUTO:add%3B
    inputs:
    - food: FOODON:03000227
      state: sauce
    - food: AUTO:salt
      state: null
    - food: FOODON:00001649
      state: null
    - food: FOODON:00003582
      state: powder
    outputs:
    - food: AUTO:none
      state: null
    utensils:
    - AUTO:none
  - action: AUTO:adjust
    inputs:
    - food: AUTO:salt
      state: null
    - food: FOODON:00001649
      state: null
    - food: FOODON:00003582
      state: powder
    outputs:
    - food: AUTO:inputs
      state: adjusted
    utensils:
    - AUTO:none
  - action: AUTO:Cook
    inputs:
    - food: FOODON:03306944
      state: null
    outputs:
    - food: AUTO:as%20directed
      state: null
    utensils: []
  - action: AUTO:mix%3B
    inputs:
    - food: FOODON:03311146
      state: null
    - food: FOODON:03306944
      state: null
    outputs:
    - food: FOODON:03306944
      state: +
    utensils:
    - AUTO:none
  url: N/A
input_id: /Users/cjm/repos/ontogpt/tests/input/cases/recipe-spaghetti.txt
input_text: "SIMPLE SPAGHETTI\n\nDIRECTIONS\nOn medium heat melt the butter and sautee\
  \ the onion and bell peppers.\nAdd the hamburger meat and cook until meat is well\
  \ done.\nAdd the tomato sauce, salt, pepper and garlic powder.\nSalt, pepper and\
  \ garlic powder can be adjusted to your own tastes.\nCook noodles as directed.\n\
  Mix the sauce and noodles if you like, I keep them separated.\n\nINGREDIENTS\nUNITS:\
  \ US\n1\nsmall onion (chopped)\n1\nbell pepper (chopped)\n2\ntablespoons garlic\
  \ powder\n3\ntablespoons butter\n1\nteaspoon salt\n1\nteaspoon pepper\n2\n(15 ounce)\
  \ cans tomato sauce\n1\n(16 ounce) box spaghetti noodles\n1 - 1 1\u20442\nlb hamburger\
  \ meat.\n"
input_title: null
named_entities:
- id: FOODON:00003485
  label: bell pepper
- id: FOODON:00003582
  label: garlic
- id: UO:0010042
  label: tablespoons
- id: FOODON:03310351
  label: butter
- id: UO:0010042
  label: tablespoons
- id: UO:0010040
  label: teaspoon
- id: FOODON:00001649
  label: pepper
- id: UO:0010040
  label: teaspoon
- id: FOODON:03301217
  label: tomato sauce
- id: FOODON:00001282
  label: hamburger meat
- id: FOODON:03310351
  label: butter
- id: FOODON:03301704
  label: onion
- id: FOODON:00003485
  label: bell peppers
- id: FOODON:00001282
  label: hamburger meat
- id: FOODON:03000227
  label: tomato
- id: FOODON:00001649
  label: pepper
- id: FOODON:00003582
  label: garlic
- id: FOODON:00001649
  label: pepper
- id: FOODON:00003582
  label: garlic
- id: FOODON:03306944
  label: noodles
- id: FOODON:03311146
  label: sauce
- id: FOODON:03306944
  label: noodles
- id: FOODON:03306944
  label: noodles
prompt: 'Split the following piece of text into fields in the following format:


  food: <the food item>

  state: <the state of the food item (e.g. chopped, diced)>



  Text:

  sauce + noodles


  ===


  '
raw_completion_output: "\nurl: N/A\nlabel: Simple Spaghetti\ndescription: An easy\
  \ to make and delicious spaghetti dish.\ncategories: Main dishes; Italian recipes\n\
  ingredients: 1 small onion (chopped); 1 bell pepper (chopped); 2 tablespoons garlic\
  \ powder; 3 tablespoons butter; 1 teaspoon salt; 1 teaspoon pepper; 2 (15 ounce)\
  \ cans tomato sauce; 1 (16 ounce) box spaghetti noodles; 1 - 1 1\u20442 lb hamburger\
  \ meat.\nsteps: On medium heat melt the butter and saut\xE9 the onion and bell peppers;\
  \ Add the hamburger meat and cook until meat is well done; Add the tomato sauce,\
  \ salt, pepper and garlic powder; Salt, pepper and garlic powder can be adjusted\
  \ to your own taste; Cook noodles as directed; Mix the sauce and noodles if you\
  \ like, I keep them separated."

```

</details>


Prompt:

<details>
```
Split the following piece of text into fields in the following format:

food: <the food item>
state: <the state of the food item (e.g. chopped, diced)>


Text:
sauce + noodles

===


```

</details>


Completion:

<details>
```

url: N/A
label: Simple Spaghetti
description: An easy to make and delicious spaghetti dish.
categories: Main dishes; Italian recipes
ingredients: 1 small onion (chopped); 1 bell pepper (chopped); 2 tablespoons garlic powder; 3 tablespoons butter; 1 teaspoon salt; 1 teaspoon pepper; 2 (15 ounce) cans tomato sauce; 1 (16 ounce) box spaghetti noodles; 1 - 1 1⁄2 lb hamburger meat.
steps: On medium heat melt the butter and sauté the onion and bell peppers; Add the hamburger meat and cook until meat is well done; Add the tomato sauce, salt, pepper and garlic powder; Salt, pepper and garlic powder can be adjusted to your own taste; Cook noodles as directed; Mix the sauce and noodles if you like, I keep them separated.
```

</details>
