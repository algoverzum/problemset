## Equality
In Goldenburg, the Day of Balance has arrived. On this occasion, the ruler of the realm decided to use the royal treasury to bring the well-being of all subjects to the same level.

There are a total of $n$ residents in the realm. The well-being of the $i$-th resident is described by an integer $a_i$, measured in gold coins (the official currency of Goldenburg).

You are the royal accountant, whose task is to calculate the minimum number of gold coins the ruler must distribute so that everyone’s well-being becomes equal. It is important to note that the ruler can only give coins; taking wealth away from anyone is not possible.


### Input
The first line contains a single integer $n$ – the number of residents in the realm.

The second line contains $n$ integers: $a_1, a_2, \ldots, a_n$, where $a_i$ is the well-being of the $i$-th resident.

### Output
Print the single integer $S$, which represents the minimum number of gold coins the ruler has to distribute.

### Constraints
* $1 \le N \le 100$
* $0 \le a_i \le 10^6$ for all $i = 1, 2, \ldots, n$

### Example Input 1
    5
    0 1 2 3 4

### Example Output 1
    10

### Explanation of Example 1
If we give 4 gold coins to the first resident, 3 to the second, 2 to the third, and 1 to the fourth, then the well-being of all residents will be 4.

### Example Input 2
    5
    1 1 0 1 1

### Example Output 2
    1

### Explanation of Example 2
It is sufficient to give one gold coin to the third resident.

### Example Input 3
    3
    1 3 1

### Example Output 3
    4

### Explanation of Example 3
Two gold coins must be given to the first and the third residents so that everyone’s well-being becomes 3.

### Example Input 4
    1
    12

### Example Output 4
    0

### Explanation of Example 4
Nothing needs to be given, since the only resident already has 12 gold coins.
