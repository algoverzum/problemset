## Pouring
In a distant galaxy, on the planet of Zog, the wise and benevolent King Zorg challenges his people to a task of great ingenuity. The task is to measure exactly $N$ units of Zognium, a rare and precious fluid, using only two cans. These cans have volumes of $A$ and $B$ units, the king's two favorite numbers.

The winner of the challenge is the one who can measure exactly $N$ units of Zognium into can $B$ with the minimum number of pours. The six possible actions you can take with the cans are:

1. Fill the first can completely.
2. Fill the second can completely.
3. Empty the first can.
4. Empty the second can.
5. Pour from the first can into the second can until the second can is full or the first can is empty.
6. Pour from the second can into the first can until the first can is full or the second can is empty.

Initially, both cans are empty.

### Input
The first line of the input contains $N$ - the number of units of Zognium to be measured. The second line contains two integers $A$ and $B$ - the volumes of the two cans.

### Output
Print a single number, the minimum number of pours required to measure exactly $N$ units of Zognium in can $B$, or $-1$ if it is impossible.

### Constraints
* $1 \le N \le 1000$
* $1 \le A, B \le 1000$

### Example input
    2
    3 7

### Example output
    8

### Explanation of the example
1. Fill the first can (3 units).
2. Pour from the first can into the second can (3 units in the second can, 0 units in the first can).
3. Fill the first can again (3 units).
4. Pour from the first can into the second can (6 units in the second can, 0 units in the first can).
5. Fill the first can (3 units).
6. Pour from the first can into the second can (7 units in the second can, 2 units remain in the first can).
7. Empty the second can (0 units).
8. Pour from the first can into the second can (2 units in the second can, 0 units in the first can).

It can be proven that the minimum number of pours required is 8.
