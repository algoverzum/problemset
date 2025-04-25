## Pyrate Loot
The feared space pirate, Captain Korg, has spotted a cargo ship transporting mysterious crates to the edge of the galaxy. Unfortunately, he wasn't able to fully hack into the ship's systems: he could only query the total weight of the cargo but couldn't determine exactly what crates are in the ship's hold.

What is certain: from the black market database, he knows what types of crates this ship may be carrying. Each crate has a known value (how much it can be sold for) and a weight (how many kilograms it weighs). There can be multiple crates of the same type in the cargo.

Captain Korg considers the worst-case scenario – he wants to know the minimum value the entire cargo could have, given that it contains some combination of the known crate types.

### Input
The first line of the input contains two numbers $N, S$: the number of possible crate types ($1 \le N \le 500$), and the total weight of the cargo on the ship ($1 \le S \le 10\,000$).

The next $N$ lines each contain two integers $T_i, W_i$: the value and weight of the $i$-th crate type (both up to $1000$).

### Output
Print a single number, the minimum total value that the cargo definitely has.

### Constraints
* $1 \le N \le 500$
* $1 \le S \le 10\,000$
* $1 \le T_i, W_i \le 1000$

### Example input
    4 15
    1 2
    2 3
    5 6
    10 4

### Example output
    8

### Explanation of the example
It is possible that the weights of the crates in the cargo sum up to $2+2+2+2+2+2+3=15$, and in this case, their values would sum up to $1+1+1+1+1+1+2=8$. This is the minimum possible value for the cargo.
