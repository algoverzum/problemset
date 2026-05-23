## Osmos
Armin has a mote of size $A$, and there are also $N$ other motes.

* A mote can only absorb another mote that is smaller than itself.
* If it absorbs a mote of size $X$, then its size increases by $X$.
* The motes may be absorbed in any order.

In one operation, you may perform one of the following actions:

* add a new mote of any positive integer size;
* remove an existing mote.

Determine the minimum number of operations required so that Armin's mote can eventually absorb all other remaining motes.

### Input
The first line of the input contains two integers: the size of Armin's mote ($A$) and the number of other motes ($N$).  
The second line contains $N$ integers $M_1, M_2, \ldots, M_N$, representing the sizes of the other motes.  
All given sizes are integers.

### Output
Print a single number, the minimum number of operations required so that Armin's mote can eventually absorb all other motes.

### Constraints
* $1 \le N \le 100$
* $1 \le A \le 10^6$
* $1 \le M_i \le 10^6$ for every $i = 1, 2, \ldots, N$.

### Example input 1
    2 2
    2 1

### Example output 1
    0

### Explanation of example 1
The mote initially has size 2. It can first absorb the mote of size 1, becoming size 3. It can then absorb the mote of size 2 as well. Therefore, no operations are needed.

### Example input 2
    2 4
    2 1 1 6

### Example output 2
    1

### Explanation of example 2
If the mote of size 6 is removed, Armin's mote can absorb all remaining motes.  
Alternatively, it is also possible to add for example a mote of size 3.

### Example input 3
    10 4
    25 20 9 100

### Example output 3
    2

### Example input 4
    1 4
    1 1 1 1

### Example output 4
    4
