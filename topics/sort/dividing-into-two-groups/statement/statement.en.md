## Dividing Into Two Groups
The challenge facing Starfleet Academy is to divide $N$ officers into two non-empty groups based on their performance (score) in previous missions. The first group will be the Elite Officers, while the second group will be the Basic Officers.
The groups shall be defined so that the performance gap between the two groups, i.e. the score difference between the weakest member of the Elite group and the strongest member of the Basic group, is as large as possible.
The Academy's main computer, the Starfleet Analytical Core, has just broken down, so we are asking you to write an algorithm to determine the maximum power gap between the two groups, thus helping the success of the Fleet's missions.

### Input
The first line of input is a single integer: $N$, the number of officers.
The second line contains $N$: $T_0, T_1, \ldots, T_{N-1}$, the number of performance points of the officers.

### Output
You have to print one number, the maximum performance distance between the two groups.

### Constraints
* $2 \le N \le 10^5$
* $0 \le T_i \le 10^6$ for each $i$.

### Example input
    8
    15 8 17 22 5 7 25 27

### Example output
    7

### Explanation of the example
If the two groups are $\{8,5,7\}$ and $\{15,17,22,25,27\}$ respectively, the difference is 7. It is obvious that no more than this can be obtained.
