## Not Too Many Hands
Our planet is home to a variety of intelligent beings with a diverse number of hands. Wrestling is a very popular sport and $N$ creatures want to compete in the World Wrestling Championship. They are numbered from 1 to $N$, and each of them has a known hand number: $H_1, H_2, \ldots, H_N$. For the sake of fairness, the competition committee decided that only wrestlers with 4 hands or less could compete. Can you tell me how many and who can start?

### Input
In the first line of the input, there is an integer: $N$ - the number of creatures who want to compete. The second line contains $N$ integers separated by spaces, the number of hands of each creature ($H_1, H_2, \ldots, H_N$).

### Output
In the first line print the number of competitors who can participate the contest. In the second line print their indices, in ascending order, separated by a space.

### Constraints
* $1 \le N \le 100$
* $0 \le H_i \le 10$

### Example input
    9
    4 7 3 5 5 7 2 0 10

### Example output
    4
    1 3 7 8

### Explanation of the example
There are 4 contestants with at most 4 hands, contestants 1, 3, 7 and 8 (they have 4, 3, 2, 0 hands).
