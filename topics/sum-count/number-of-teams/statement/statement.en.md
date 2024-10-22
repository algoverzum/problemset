## Number Of Teams
On the Planetary Youth Programming Contest (PYPC), teams of 3 young adults can participate. A young adult is a person whose age is at least 18 and at most 21 years. I will list the ages of people living in my settlement. We would like to create as many teams as possible from people living here (but a person can only belong to one team). What is the maximum number of teams we can make?

### Input
The first line of the input contains $N$ - the number of people in my settlement. Each of the next $N$ lines contains a person's age, which is an integer number $A_i$ ($i=1, 2, \ldots, N$).

### Output
Print a single number, the maximum number of teams we can make.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 100$

### Example input
    6
    3
    19
    21
    18
    42
    18

### Example output
    1

### Explanation of the example
There are 4 persons who are eligible for the competition (ages: 19, 21, 18, 18). We can form 1 team with 3 persons out of the 4 of them, but we cannot form 2 teams because that would require 6 persons.
