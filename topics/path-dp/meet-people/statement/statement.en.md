## Meet People
In our culture, festivals often group participants according to a square grid. In each of these squares you can meet a given number of participants. You start from the left edge of the grid and aim to reach the right edge. At each step, you can choose to move from the current field (i,j) to the right (i,j+1), up to the right (i-1,j+1) or down to the right (i+1,j+1). Each field you enter will be met by all the fields you are in. Create a program that tells you the maximum number of participants you can meet and which field you have to start from.

### Input
In the input, the first line contains two integers, the number of rows and columns: $N$, $M$.
The subsequent $N$ row has $M$ integers, the number of people in each grid field: $P_i$.

### Output
In the first line of the output, you need to print an integer: how many participants we can meet.
In the second line of the output you have to print an integer: from which line we have to start for this. (The indexing starts from 1)

### Constraints
* $1 \le N,M \le 100$
* $0 \le P_i \le 1000$

### Example input
    4 4
    6 1 7 1
    1 6 1 7
    2 2 2 2
    9 1 1 9

### Example output
    26
    1

### Explanation of the example
We visit the following spaces:
<b>6</b> 1 <b>7</b> 1
1 <b>6</b> 1 <b>7</b>
2 2 2 2
9 1 1 9
