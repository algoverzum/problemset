## Balanced Loading
Han Solo and Chewbacca have been tasked by Jabba to load containers onto the Millennium Falcon in such a way that the difference between the total weight in the left and right cargo holds is minimized. Each container's weight is given in kilograms.

### Input
The first line of the input contains the number of containers, $N$, where $2 \le N \le 1000$.

The second line contains $N$ integers, representing the weights of the containers in kilograms (each between 1 and 50).

### Output
The first line should contain the minimum possible difference between the total weight of the two cargo holds.

The second line should list the number of containers placed in the left cargo hold, followed by their original indices.

The third line should list the number of containers placed in the right cargo hold, followed by their original indices.

If there are multiple optimal solutions, any of them may be given.

### Constraints
* $2 \le N \le 1000$
* $1 \le A_i \le 50$, where $A_i$ is the weight of the $i$-th container ($i = 1, 2, \ldots, N$)

### Example input
    5
    10 20 15 5 25

### Example output
    5
    3 1 4 5
    2 2 3

### Explanation of the example
The 1st, 4th, and 5th containers are placed in the left cargo hold, with a total weight of $10+5+25=40$.
The 2nd and 3rd containers are placed in the right cargo hold, with a total weight of $20+15=35$.
The absolute difference $|40-35|=5$, which is minimal.
