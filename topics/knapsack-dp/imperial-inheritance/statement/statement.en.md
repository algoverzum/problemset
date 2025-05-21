## Imperial Inheritance
The ruler of the Galactic Empire has unexpectedly vanished during a diplomatic mission near the edge of a black hole. With no heir to the throne, the Imperial Council has decided that the Empire’s two rightful successors, Seran and Kaela, will share the Empire’s most valuable resources: its planets.<br>
Each planet has a known value, represented by a positive integer. The siblings strive for a fair inheritance — that is, a division in which both receive planets with the same total value.<br>
However, they soon realize that this is not always possible, so they are willing to leave some planets under joint supervision for the time being. Help the heirs divide the planets fairly so that the total value of the jointly held planets is minimized.

### Input
The first line of the standard input contains an integer $N$, the number of planets.
The second line contains exactly $N$ positive integers: $B_i$.
The total value of all planets is at most 10,000.

### Output
Print the total value of the planets left under joint control on the first line of standard output.
Print the indices (starting from 1) of the planets assigned to the first and second heir on the second and third lines, respectively.
Multiple valid solutions may exist — any of them is acceptable.

### Constraints
* $1 \le N \le 300$
* $\sum B_i \le 10,000$
### Example input
    7  
    16 3 11 38 1 4 2

### Example output
    39
    1 7
    3 2 6

### Explanation of the example
<span style="color:red">16 </span><span style="color:aqua">3 11 </span>38 1 <span style="color:aqua">4 </span> <span style="color:red">2 </span><br>
The planets with values 38 and 1 couldn't be fairly divided, totaling 39.<br>
Each heir receives planets with a total value of 18.
