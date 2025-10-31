## Chinese remainder
We want to decipher a secret numeric code that consists of at most 4 digits, it is a positive integer. We only know the remainders when the code is divided by 5 ($A$), by 7 ($B$), and by 11 ($C$).

Write a program that reads the values of $A$, $B$, and $C$, and determines the smallest positive integer code that satisfies these remainder conditions.

If no such number exists, print -1.

### Input
The input consists of three lines:

The first line contains an integer $A$, the remainder when the code is divided by 5.

The second line contains an integer $B$, the remainder when the code is divided by 7.

The third line contains an integer $C$, the remainder when the code is divided by 11.

### Output
Print the smallest positive integer code that satisfies the given remainder conditions, or -1 if no such code exists.

### Constraints
* $0 \le A \le 4$
* $0 \le B \le 6$
* $0 \le C \le 10$

### Example input 1
    3
    4
    0

### Example output 1
    88

### Explanation of the example 1
88 % 5 = 3, because $88 = 17 \cdot 5 + 3$.
88 % 7 = 4, because $88 = 12 \cdot 7 + 4$.
88 % 11 = 0, because $88 = 8 \cdot 11 + 0$.
It can be verified that this is the smallest positive solution.

### Example input 2
    2
    1
    1

### Example output 2
    232

### Example input 3
    1
    5
    2

### Example output 3
    376
