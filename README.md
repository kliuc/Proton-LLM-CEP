# proton/LLM CEP
 
First create a random stream "rand_abc":

```
CREATE RANDOM STREAM rand_abc(
  character string default ['a','b','c'][1+rand()%3]
) SETTINGS eps=0.05
```
