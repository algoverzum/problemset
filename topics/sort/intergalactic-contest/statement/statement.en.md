## Intergalactic Contest
The ICPC (Intergalactic Creatures' Programming Contest) is the most prestigious programming contest in the universe. Many teams of creatures attend it every year, so it is important to calculate the result of the contest efficiently.

You are given the data from the contest, for every team the number of problems they solved and the corresponding penalty score (calculated from the time they needed to solve the problems and the previous wrong solutions). Your task is to calculate the final standing of the contest. Team A finished before team B, if they solved more problems, or if they solved the same number of problems with a lower penalty score.

### Input
The first line of the input contains $N$ - the number of teams.  
The following $N$ lines each contain two numbers $A_i$ and $B_i$, the number of problems solved by the $i$-th team and the penalty score of the team. Any two rows are different (in at least one of the numbers).

### Output
Print a single line with $N$ numbers, the IDs of the teams in their final order (starting with the winning team).

### Constraints
* $1 \le N \le 100\,000$
* $0 \le A_i, B_i \le 10^9$ for all $i=1 \dots N$

### Example input
    5
    2 10
    2 20
    3 40
    1 20
    0 0

### Example output
    3 1 2 4 5

### Explanation of the example
Team 3 wins with 3 solved problems. Team 1 finishes second place before team 2 with a lower penalty score, and equal number of solved problems.
