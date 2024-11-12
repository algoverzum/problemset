## Swap Candies
There are $N$ children in a class. Their tradition is to pair up the students and in each pair, two children give their candy to each other. This year, the teacher didn't feel like pairing the students so she just lined them up and paired them starting from the front of the line.

### Input
The first line of the input is the number of students $N$.
The second line in the input is the number of candies of the students. $A_1, A_2, \ldots, A_{N}$.

### Output
You need to print the number of candies of all students on one line, separated by a space.

### Limits
* $1 \le N \le 1000$
* $1 \le A \le 1000$

### Example input
    5
    9 4 5 2 3

### Example output
    4 9 2 5 3

### Explanation of the example
    Student 1 has 9 candies, student 2 has 4. Swap first 4 for second 9.
    Student 3 has 5, student 4 has 2, student 3 has 5, student 4 has 2, student 3 has 2, student 4 has 5.
    Student 5 has no partner so he doesn't swap with anyone, leaving him with 5 candies.