## Balanced Numbers
Stargate Command has discovered a strange series of numbers in a message from an alien planet. This does not appear to be a random code, certain numbers are in equilibrium: their values are equal to the average of their immediate neighbors.

Could you sort out these balanced numbers? Do not change their order!

### Input
The first line of the input is $N$, which is the length of the message.
The next line contains the numbers in the message: $A_1, A_2, \ldots, A_{N}$.

### Output
You should print out the numbers separated by spaces that are equal to the average of their neighbors.

### Constraints
* $1 \le N \le 10000$
* $1 \le A_i \le 1000$

### Example input
    8
    1 4 7 11 10 8 6 10

### Example output
    4 8

### Explanation of the example
Since $\frac{1+7}{2}=4$ and $\frac{10+8}{2}=8$, the condition is satisfied for these two numbers. Not for the others, for example, $\frac{4+11}{2}\not=7$.
