## Same Two Times
On an alien planet, various animals are captured for examination and then released. We capture animals at random, but we don't want to study the same animal twice in a row. Your task is to find the first instance where, out of $N$ captured animals, we caught the same animal two times in a row. The animals are represented by an integer code. If there is no such case, print a number 0.

### Input
The first line of the input contains a single integer, the number of animals captured: $N$.
The second line of input contains $N$ integers, the integer codes of the animals caught: $A_1, A_2, \dots, A_N$.

### Output
You have to print a single number, the index of the first instance where the animal code is equal to the directly subsequent animal code. If there is no such instance, print a number 0.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Example input
    5
    98 95 92 92 100

### Example output
    3

### Explanation of the example
    The third and fourth numbers are the same, so 3 is the right answer.
