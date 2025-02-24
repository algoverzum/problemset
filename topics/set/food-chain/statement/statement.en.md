## Food Chain
On an alien planet, we conducted a biological survey, identifying so-called feeding pairs (what
eats what?). The number of these pairs is up to 30.
Plants do not eat any living organisms, animals
eat either plants or other animals. The meaning of a food pair is: the first eats the second, e.g. "fox eats partridge", "snail eats grass".
Write a program that gives the names of the animals in the food pairs that
eat an animal (and possibly a plant)! Note: something that eats nothing is a plant.


### Input
The first row of the standard input contains the number of feeding pairs (1≤N≤30). Each of the following N rows contains one feeding pair, two words
separated by a space. The organism given in the first word eats the one given in the second. The feeding
in the feeding pairs can only contain letters without accents.

### Output
The first line of the standard output contains the number of animals that eat an animal (and
possibly plants)! In the following rows, print out these animals line by line, in any order! If there is no such animal in the given food chain, only 0 should be printed out.

### Constraints
* $1 \le N \le 30$<br>
The names of living things are in lower case in the English alphabet and are up to 100 characters long.

### Example input
    7
    fox partridge 
    fox blackbird
    partridge  worm
    snail grass
    blackbird snail
    worm roots 
    blackbird seeds

### Example output
    3
    fox
    partridge 
    blackbird


### Explanation of the example

