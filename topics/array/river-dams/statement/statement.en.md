## River Dams
We want to build new hydropower plants as our energy use has increased. We already know which river we want to build on, but we haven't found the perfect place on this river yet. We know the width of the water in each section of the river, and we want to know each possible location out of the sections. A section is suitable if it is wider than the two sections before and after it. Since the first and last sections have only one neighbour, they cannot be possible sites. Your task is to select suitable points for a dam from a river of N sections.

### Input
The first line of the input contains an integer, the number of sections: $N$
The second line contains $N$ numbers, the width of each section: $A_i$

### Output
Print a single number, the number of corresponding sections that are suitable

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 10000$

### Example input
    5
    5 1 5 1 5

### Example output
    1

### Explanation of the example
The third section is wider than the second and fourth. Although the first and fifth are also wider than their neighbours, because they are on the edge, they are not considered to be suitable locations.
