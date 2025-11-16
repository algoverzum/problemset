## Icecubes
A restaurant has a fridge with $N$ compartments, and for each compartment, you know how many ice cubes it contains.

A waiter comes and takes one ice cube from every compartment that has at least one.

After this operation, how many ice cubes remain in total in the fridge?

### Input
The first line of the input contains $N$ - the the number of compartments.

The next line contains $N$ integers $C_{0}, \, \ldots, \, C_{N-1}$, the number of ice cubes in each compartment.

### Output
Print a single number, the total amount of ice cubes left in the fridge after the waiter took the ice cubes.

### Constraints
* $1 \le N \le 10^5$
* $0 \le C_i \le 1000$ for each $i=0\ldots N-1$.

### Example input 1
    5
    0 3 1 0 5

### Example output 1
    6

### Explanation of example 1
In the first example, after the waiter's action, we have $0, 2, 0, 0, 4$ ice cubes in the containers, for a total of $2 + 4 = 6$ cubes.

### Example input 2
    3
    1 1 1

### Example output 2
    0

### Explanation of example 2
In the second example, after the waiter's action, we have $0, 0, 0$ ice cubes in the containers, for a total of $0$ cubes.
