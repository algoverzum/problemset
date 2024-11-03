## Astronaut Pairs
We want to send two astronauts of equal weight on a space mission in order for the spacecraft to be balanced. We want to test to find the best pair, so we want to test all possible astronaut pairs. The order of the pairs is not important, so two astronauts of the same weight should only count once. Find the number of tests we need to do, that is, the number of different pairs of equal weights we can make.

### Input
The first line of the input is a number, the number of astronauts: $N$ 
The second line of input is $N$, the weights of each astronaut: $A_1, A_2, \ldots, A_N$

### Output
You need to output a single number, the number of possible pairs.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Example input
    5
    1 2 3 2 3

### Example output
    2

### Explanation of the example
The two possible pairs are the pair of weight two and the pair of weight three astronauts.
