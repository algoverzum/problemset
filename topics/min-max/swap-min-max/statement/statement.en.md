## Swap Most and Least Candies
There are $N$ students in a class. The teacher plays a game with his students where there is a pile of candy on the teacher's desk, each student can take as much as he wants, but they are not allowed to take the same amount as another student has taken. At the end, the student who took the most candy must trade with the student who took the least.

### Input
The first line of the input contains the number of students: $N$.
The second line contains the number of candies taken by the students, in order: $C_1, C_2, \ldots, C_N$.

### Output
You need to print how many candies each student will have after the swap, separated by spaces.

### Constraints
* $1 \le N \le 1000$
* $1 \le C_i \le 1000$

### Example input
    5
    3 4 5 2 1

### Example output
    3 4 1 2 5

### Explanation of the example
The third student took the most candies, five. The fifth student took the least, one. They have to exchange, so the third student will have one and the fifth student will ahve five.
