## Space Trading
Two spaceships met in deep space and decided to trade. The on-board computers will automatically unpack the cargoes that are suitable for exchange, but those that are in the warehouses of both ships will be left in the warehouse. Create a program that decides which type of cargoes will stay in the warehouse based on the contents of the warehouses of the two ships in question!

### Input
The first line of the input contains two integers, the number of cargoes in the warehouses of the first and the second ships: $N$, $M$.
The second line of the input contains $N$ integers, the codes of the cargoes in the warehouse of the first ship: $A_1, A_2, \dots, A_N$.
The second line of the input contains $M$ integers, the codes of the cargoes in the warehouse of the second ship: $B_1, B_2, \dots, B_N$.

### Output
In the first line of the output, write the codes of the cargoes that are in the warehouses of both ships.

### Constraints
* $1 \le N, M \le 100$
* $1 \le A_i, B_i \le 1000$

### Example input
    5 6
    1 4 6 12 23
    4 6 7 8 9 12

### Example output
    4 6 12

### Explanation of the example
The codes 4, 6 and 12 are the codes that appear in both the first and second sequence of numbers.
