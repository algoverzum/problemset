## Sky Spy
The Rebels have successfully hacked one of the Empire's geostationary spy satellites. This satellite orbits directly above the infamous Mos Eisley spaceport, allowing the Rebels to take photographs of the docked spaceships without the Empire's knowledge.

Rebel intelligence has obtained information that $N$ spaceships will appear, each within a specific time interval. The goal is to take as few pictures as possible with the spy satellite — in such a way that each of the $N$ spaceships appears in at least one photo. The $i$-th spaceship arrives at time $A_i$ and departs at time $B_i$. A photo taken at time $T$ will include the $i$-th spaceship if and only if $A_i \le T < B_i$.

Determine the minimum number of distinct time points when the satellite must be activated to observe the spaceport so that every spaceship is captured at least once while it is actually present.

### Input
The first line of the input contains $N$ — the number of incoming spaceships. Each of the following $N$ lines contains two integers. In the $i$-th line, you are given $A_i$ and $B_i$: $A_i$ is the arrival and $B_i$ is the departure time of the $i$-th spaceship.

### Output
The output should contain a single integer: the number of photographs $K$ to be taken.  
The second line should contain exactly $K$ integers, separated by spaces, representing the time points (in any order) at which the photographs should be taken.
If there are multiple solutions, any of them is acceptable.

### Constraints
* $1 \le N \le 10^5$
* $1 \le A_i < B_i \le 10^9$ for all $i = 1, 2, \ldots, N$

### Example input
    6
    2 4
    1 4
    2 7
    7 13
    5 10
    3 9

### Example output
    2
    3 9

### Explanation of the example
Ships 3 and 4 cannot be photographed at the same time, so at least two photos are required. The task can be completed with two photos, as shown in the figure. (Multiple correct solutions exist.)

![](tex/abra.png)
