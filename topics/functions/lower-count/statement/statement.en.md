## Lower Count
A spaceship's reactors must generate enough power for safe travel. Before launch, the system analyzes their performance, identifying those that generate power below a critical threshold.

Write a function to count how many reactors fall below a given limit in a list of power levels.

### Template
Start from the predefined template code! Do not change anything in the main program, otherwise it will not be accepted. You need to write the `count_lower` function, which takes a sequence of numbers and a limit as parameters and returns the count of values below the limit.

### Constraints
* $1 \le N \le 100$, where $N$ is the length of the sequence.
* $1 \le K \le 10\,000$, where $K$ is the specified limit.
* Each element of the sequence is between $1$ and $10\,000$.

### Example
In the sequence (6 3 4 1 2), 1, 2 and 3 are less than the given limit of 4, so the function should return 3.
