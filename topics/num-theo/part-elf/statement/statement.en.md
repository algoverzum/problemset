## Part Elf
Vida claims that she is part Elf, meaning that at least one of her ancestors was a full Elf. However, she does not know whether it was a parent, a grandparent, or an even more distant ancestor.

If one parent is $A/B$ Elf and the other parent is $C/D$ Elf, then their child will be:

$$\frac{A/B+C/D}{2}$$

Elf.

For example, the child of a Human ($0/1$) and a half-Elf ($1/2$) is $1/4$ Elf.

We know that 40 generations ago, every one of Vida's ancestors was either a full Elf ($1/1$) or a full Human ($0/1$).

Task: Given Vida's Elf ratio $P/Q$ (not necessarily in reduced form), determine the minimum number of generations ago a full Elf ancestor could have existed in her family.

If such ancestry is impossible, print "impossible".

### Input
The first line contains a single integer: $P$.  
The second line contains a single integer: $Q$.

### Output
Print a single value: the minimum number of generations ago a full Elf ancestor could have existed, or "impossible" if the given ratio cannot occur.

### Constraints
* $1 \le P < Q \le 10^{12}$

### Example 1 input
    1
    2

### Example 1 output
    1

### Example 1 explanation
Vida could be the child of a full Elf ($1/1$) and a Human ($0/1$). In this case, she had a full Elf ancestor 1 generation ago, so the answer is 1.

### Example 2 input
    3
    4

### Example 2 output
    1

### Example 2 explanation
Vida could be the child of a full Elf ($1/1$) and a half-Elf ($1/2$). Therefore, she also had a full Elf ancestor 1 generation ago, so the answer is 1.

### Example 3 input
    1
    4

### Example 3 output
    2

### Example 3 explanation
Vida could be the child of a Human ($0/1$) and a half-Elf ($1/2$). The half-Elf parent could be the child of a full Elf ($1/1$) and a Human ($0/1$). Therefore, the closest full Elf ancestor lived 2 generations ago, so the answer is 2.

### Example 4 input
    2
    23

### Example 4 output
    impossible

### Example 4 explanation
It is impossible to be exactly $2/23$ Elf. Therefore, the answer is "impossible".

### Example 5 input
    123
    31488

### Example 5 output
    8
