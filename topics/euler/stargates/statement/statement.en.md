## Stargates
In a remote star system, an eager team of researchers has stumbled upon an ancient network of stargates. These gates allow two-way travel, but close for an extended period after each use. The team's goal was simple: to make sure that all the gates were working properly, they decided to travel through the entire network, meaning that they should use each stargate exactly once (in one of the two directions). At the same time, they knew that to avoid getting trapped, they had to end their journey on the planet from which they had started. Luckily, they have a list of which stargates connect which two planets in the system. Help the research team use this list to decide whether it is possible to travel through the stargate network safely.

### Input
The first line of the input contains two integers: $N$ is the number of planets in the system and $R$ is the number of stargates. <br>
The planets are denoted by $1, \ldots, N$.<br>
This is followed by $R$ lines , each line has two distinct numbers $V_i$ and $V_j$ the two planets connected by the edge.

### Output
Print a single word. **YES** if there is such a traversal. **NO** if there isn't.

### Constraints
* $1 \le N \le 200$
* $1 \le R \le 10000$
* $1 \le V_i,V_j \le N$, $V_i \not= V_j$ 

### Example input
    5 6
    2 1
    1 3
    2 5
    1 4
    3 4
    5 1

### Example output
    YES

### Explanation of the example
A possible traversal for example:<br>
$1 \to 2 \to 5 \to 1 \to 4 \to 3 \to 1$

![example](tex/abra.pdf)