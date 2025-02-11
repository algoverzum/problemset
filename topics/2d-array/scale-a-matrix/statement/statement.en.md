## Vulcan Tea Prices
Spock wants to organize a gathering where he invites $K$ fellow officers and provides each of them with a serving of Vulcan tea. He only needs to choose the meeting location and time. From the United Federation database, $N$ possible space stations are available, and Spock knows the price of the drinks at each location for the next $M$ stardates in advance.

These prices are stored in a table $T$, where the element in the $i$-th row and $j$-th column, $T_{i,j}$, represents the cost of one serving of Vulcan tea at the $i$-th location on the $j$-th stardate.

Spock wants to see the total cost of $K$ servings at each location and time to make the most logical decision. Can you create a table $S$ for him, where $S_{i,j}$ represents the total cost of $K$ servings of tea at the $i$-th location on the $j$-th stardate?

### Input
The first line contains two integers, $N$ (the number of space stations) and $M$ (the number of stardates).
This is followed by the $T$ table: the next $N$ lines each contain $M$ integers representing the price of one serving of Vulcan tea at different locations and times.
The last line contains a single integer: $K$, the number of Spock’s fellow officers.

### Output
Print the $S$ table as described above, representing the total price of $K$ servings of tea at each location and time.

### Constraints
* $1 \le N, M \le 10$
* $1 \le K \le 100$
* $1 \le T_{i,j} \le 100$

### Example input
    3 4
    1 3 2 5
    7 6 4 8
    2 9 1 4
    2

### Example output
    2 6 4 10
    14 12 8 16
    4 18 2 8
