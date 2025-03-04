## Lower Count
We run safety tests on spacecraft reactors. In one phase, the on-board computer tests how many reactors will operate under a certain load. Write a function that can count how many are below a given limit among a list of load levels.

### Template
Start from the predefined template code! Do not change anything in the main program, otherwise it will not be accepted. You need to write the `count_lower` function, which takes as parameters the sequence of numbers and the limit and returns the number of items below the limit.

### Constraints
* $1 \le N \le 100$, where $N$ is the size of the number sequence.
* $1 \le M \le 10000$, where $M$ is the specified limit
* All elements of the sequence are between $1$ and $10000$.

### Example
In the sequence (6 3 4 1 2), 1, 2 and 3 are less than the given limit of 4, so the answer is 3.
