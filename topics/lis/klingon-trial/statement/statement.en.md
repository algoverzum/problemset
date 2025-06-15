## Klingon Trial
A young Klingon warrior seeks to earn a seat on the High Council. As part of his Rite of Ascension, he must face a series of battle trials — each with an assigned honor rating representing its difficulty.

The trials are given in a fixed order. He may skip some, but must fight in order without going back. His goal is to complete a strictly increasing sequence of trials — choosing battles with rising honor ratings — to gain the greatest respect.

Your task is to find the length of the longest increasing subsequence of trial difficulties.

### Input
The first line of the input contains $N$ — the number of trials.  
The second line contains $N$ integers $T_1, T_2, \ldots, T_N$ — the difficulty of the trials in the given order. 

### Output
Print a single number, the length of the longest chain of increasingly difficult trials available.

### Constraints
* $1 \le N \le 1000$
* $1 \le T_i \le 10^9$ for each $i=1,2,\ldots,N$

### Example input
    11
    8 3 4 6 5 2 1 7 9 1 9

### Example output
    5

### Explanation of the example
One possible longest increasing subsequence is: $3, 4, 5, 7, 9$.

Another valid one is: $3, 4, 6, 7, 9$.

Both have length 5.
