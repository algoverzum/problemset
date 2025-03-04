## Food Chain
On an alien planet, we conducted a biological survey, identifying so-called feeding pairs (what eats what?). The number of these pairs is up to 30.
Plants do not eat any living organisms, animals eat either plants or other animals. The meaning of a feeding pair is: the first eats the second, e.g. "fox eats partridge", "snail eats grass".
Write a program that gives the names of the animals in the food pairs that eat an animal (and possibly a plant). Note: something that eats nothing is a plant.

### Input
The first row of the standard input contains the number of feeding pairs ($1 \le N \le 30$). Each of the following $N$ lines contains one feeding pair, two words separated by a space.
The organism given in the first word eats the one given in the second.

### Output
The first line of the standard output contains the number of animals that eat an animal (and possibly plants). In the following rows, print out these animals line by line, in **alphabetical** order! If there is no such animal in the given food chain, only 0 should be printed.

### Constraints
* $1 \le N \le 30$<br>
The names of the organisms are lower case letters of the English alphabet and are up to 100 characters long.

### Example input
    7
    fox partridge
    fox blackbird
    partridge worm
    snail grass
    blackbird snail
    worm roots
    blackbird seeds

### Example output
    3
    blackbird
    fox
    partridge


### Explanation of the example
A blackbird eats snails, but snails are animals because they eat grass. So a blackbird is an animal that eats animals.

The partridge eats worms, they eat roots. So a partridge is also an animal that eats animals.

The fox eats the partridge and the blackbird, which are both animals. So the fox is also an animal that eats animals.

It can be seen that there are no further solutions.
