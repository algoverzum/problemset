## Cheap Space Travels
My friend Akiko can choose between $N$ space trips. For each trip, the distance to the destination in light years and the price of the trip in Galleons are known. Akiko is interested in trips in which the price per light-year distance is no more than 100 Galleons. Can you tell him which trips to choose from?

### Input
The first line of the input contains $N$ - the number of trips. After that, two integers characterizing each trip are listed in $N$ line: $D_i$ and $P_i$, its distance and price ($i = 1, 2, \ldots, N$).

### Output
In the first line print the number of trips for which the price per light-year is no more than 100 Galleons. In the second line, list the indeces of these trips, separated by a space.

### Constraints
* $1 \le N \le 100$
* $1 \le D_i \le 100$ for all $i=1 \dots N$
* $1 \le P_i \le 100\,000$ for all $i=1 \dots N$

### Example input
    5
    6 600
    30 2001
    2 500
    100 4242
    10 1001

### Example output
    3
    1 2 4

### Explanation of the example
There are 3 good trips. For the first trip the price per light-year is exactly 100 Galleons, for the second trip the price is 66.7 Galleons, and for the fourth trip the price is 42.42 Galleons.

### Example 2 input
    2
    5 600
    13 1337

### Example 2 output
    0

### Explanation of the example
If there is no good trip, there is no need to write anything in the second line.
