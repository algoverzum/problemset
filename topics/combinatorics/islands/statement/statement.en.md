## Islands
Archaeologists recently discovered a record describing how a Polynesian tribe populated a previously uninhabited archipelago in the Pacific Ocean.
At first, the tribe lived on only one island, but as the population grew, explorers would occasionally set out from the crowded islands in search of new, unknown lands.
The elders of the tribe kept notes for each island, listing the newly discovered islands that were found from there.

In how many different orders could the tribe have discovered the islands, if we know that every island was discovered exactly once and that no two discoveries happened at the same time?

### Input
The first line of the input contains the number of islands, $1\le N\le 20\,000$. Each of the following $N$ lines describes the islands discovered from island $i$:

the line starts with the number of newly discovered islands, followed by their indices. It is known that island 1 is the tribe's homeland, and it was discovered first.

### Output
Print the number of possible discovery orders. Since the answer can be very large, output it modulo $10^9+7$.

### Constraints
* $1 \le N \le 20\,000$

### Example input 1
    5
    2 2 3
    2 4 5
    0
    0
    0    

### Example output 1
    8

### Explanation of the example
The possible discovery orders are:

1 2 3 4 5

1 2 3 5 4

1 2 4 3 5

1 2 4 5 3

1 2 5 3 4

1 2 5 4 3

1 3 2 4 5

1 3 2 5 4
    
### Example input 2
    13
    4 2 3 4 6
    0
    1 5
    0
    2 7 12
    1 9
    1 8
    1 13
    2 10 11
    0
    0
    0
    0

### Example output 2
    221760
