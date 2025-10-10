## Counting Vowels
You are given a string $S$ consisting of lowercase English letters.
You are also given $Q$ queries (intervals), each containing two integers: $i$ and $j$ ($1 \leq i \leq j \leq |S|$).

For each query, determine how many vowels are in the substring of $S$ between the $i$-th and $j$-th characters (inclusive).

The vowels are: a, e, i, o, u.

### Input
The first line contains the string $S$.

The second line contains an integer $Q$, the number of queries.

Each of the next $Q$ lines contains two integers $i$ and $j$ ($1 \leq i \leq j \leq |S|$).

### Output
For each query, print a single line containing the number of vowels in the given interval.

### Constraints
* $1 \le |S| \le 10^5$

* $S$ consists of lowercase English letters

* $1 \le Q \le 10^5$

* $1 \leq i \leq j \leq |S|$ for every query

### Example input
    abrakadabra
    3
    1 3
    2 5
    5 11

### Example output
    1
    1
    3

### Explanation of the example
For the first query (abr), there is one vowel: a.

For the second (brak), there is one vowel: a.

For the third (kadabra), there are three vowels: a, a, a.
