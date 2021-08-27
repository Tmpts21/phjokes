## Phjokes 
python package that generates a list of Filipino(pinoy) jokes. 

My inspiration in creating this package is that i love funny jokes and those really cool existing api's like dad jokes api https://icanhazdadjoke.com/api. So i said to myself why not create my first python package that  generates this funny jokes in my own native language and learn packaging in python at the same time . I also created a joke api way before i decided to this project https://github.com/Tmpts21/filipino_jokes_api built with node and express js .

Documentation :  https://github.com/Tmpts21/phjokes/

## Installation 🛠
via pypi 

``` pip install phjokes ``` 

or just clone the repo

``` git clone https://github.com/Tmpts21/phjokes.git``` 

## Usage ✨

```
# get a simple joke 
import phjokes 
joke = phjokes.get_joke() 

// returns {'dialect': 'tagalog', 'joke': ['Question: Sinong cartoon charcater ang sumisigaw ng yabba dabba doo?', 'Answer: Si scooby dooby doo? XD']}



#get a joke based on dialect 
tagalog_joke = phjokes.get_joke('tagalog')
bisaya_joke = phjokes.get_joke('bisaya')

# you can also get a joke based on count 
five_tagalog_jokes = phjokes.get_joke('tagalog' , 5 ) 
seven_bisaya_jokes = phjokes.get_joke('bisaya' , 7 ) 

# get a randomjoke 
random_joke = phjokes.random()

# get a random joke based on count 
five_random_jokes = phjokes.random(5)

for text in joke['joke'] : 
  print(text)
  
""" 
Question : Sinong cartoon charcater ang sumisigaw ng yabba dabba doo?
Answer: Si scooby dooby doo? XD 
"""


```

Contribute your funny Pinoy joke by adding jokes in ```phjokes/jokes/jokes.py``` file and just copy the format and create a pull request or directly email me at mivatampos@tip.edu.ph. ~~adios 🙋‍♂️

Notes:
The package right now only supports two dialects (Tagalog and bisaya)

Todos:
- add more dialects and jokes
