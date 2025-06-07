## Klingon Trial
A young Klingon warrior seeks to earn a seat on the High Council. As part of his Rite of Ascension, he must face a series of battle trials — each with an assigned honor rating representing its difficulty and prestige.

These trials are presented in a fixed order, dictated by ancient tradition.

The warrior's goal is to select a **strictly increasing sequence** of trials to complete — one that will earn him the **greatest possible respect** among his peers.

He may skip some trials if necessary, but he cannot fight them out of order, and cannot return to an earlier trial once it has passed.

Your task is to help him find the Longest Increasing Sequence of battle trials by their honor ratings — the longest chain of increasingly prestigious battles he can complete in the given order.

### Input
The first line of the input contains $N$ - the number of available trials.  
The second line contains $N$ integers $T_1, T_2, \ldots, T_N$, the difficulty of the trials in the given order. 

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
One possible longest increasing subsequence is: $3, 4, 5, 7, 9$

Another valid one is: $3, 4, 6, 7, 9$

Both have length 5.
