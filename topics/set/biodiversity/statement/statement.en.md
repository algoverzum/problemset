## Biodiversity
We want to identify all living things on a planet. To do this, we sent out two teams to search two different parts of the planet. Both teams sent a list of the identifiers of the organisms they found. Your task is to merge the two lists, i.e. print all the identifiers that appear on at least one of the lists.

### Input
In the first line of the input, there are two integers separated by spaces: $N$ and $M$ which are the number of identifiers collected by the teams.
In the second line of the input, there are $N$ integers separated by spaces. These are the identifiers collected by the first team: $A_1, A_2, \ldots A_N$.
In the third line of the input, there are $M$ integers separated by spaces. These are the identifiers collected by the second team: $B_1, B_2, \ldots B_M$.

### Output
In the first line of the output, print the number of identifiers that appear in at least one of the lists.
The second line should contain these identifiers in ascending order, separated by spaces. Each identifier must appear only once.

### Constraints
* $1 \le N,M \le 100\,000$
* $1 \le A_i, B_i \le 10^9$

### Example input
    5 6
    9 3 6 7 1
    2 2 3 6 6 5

### Example output
    7
    1 2 3 5 6 7 9


