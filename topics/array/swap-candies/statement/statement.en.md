## Swap Candies
There are $N$ children in a class. Their tradition is to pair up the students and in each pair, two children give their candy to each other. This year, the teacher didn't feel like pairing the students so she just lined them up and paired them starting from the front of the line. If there are an odd number of students, the last one in the row will not have a pair and will not swap with anyone. Given the number of candies of the students before the swaps, can you tell how many candies each student will have after the swaps?

### Input
The first line of the input is the number of students: $N$.
The second line contains the number of candies of the students: $C_1, C_2, \ldots, C_N$.

### Output
You need to print the number of candies of all students on one line, separated by a space.

### Limits
* $2 \le N \le 1000$
* $1 \le C_i \le 1000$

### Example input
    5
    9 4 5 2 3

### Example output
    4 9 2 5 3

### Explanation of the example
    Student 1 has 9 candies, student 2 has 4. Swap first 4 for second 9.
    Student 3 has 5, student 4 has 2, student 3 has 5, student 4 has 2, student 3 has 2, student 4 has 5.
    Student 5 has no partner so he doesn't swap with anyone, leaving him with 5 candies.