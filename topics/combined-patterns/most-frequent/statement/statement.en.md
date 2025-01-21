## Most Frequent
The Galactic Council has recovered an ancient data packet containing the wisdom of the Jedi. The data packet holds a sequence of numbers, but to decode the message, you must identify the key element in the sequence: the number that appears most frequently.
If there is a tie and multiple numbers occur with the same frequency, the smallest of these numbers must be chosen, as the ancient Jedi valued humility and simplicity.
Your mission: determine the most frequent (and, if needed, the smallest) number in the sequence to unlock the secrets of the data packet. May the Force guide you!

### Input
The first line of the input contains an integer $N$, the length of the sequence.
The second line of the input contains exactly $N$ integers separated by spaces: $A_1, A_2, \ldots, A_{N}$, the elements of the sequence.

### Output
Print a single number, the most common number in the data packet. If there are more than one such numbers, you should print the smallest among them.

### Constraints
* $1 \le N \le 100$
* $0 \le A_{i} \le 100$

### Example input
    9
    5 2 2 8 5 3 5 2 8

### Example output
    2

### Explanation of the example
5 and 2 are both triples, the smaller is required.
