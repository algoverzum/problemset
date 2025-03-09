## Museum
A museum has $M$ guards on duty for $N$ days. The $i$-th guard was on duty from the $F_i$-th day to the $L_i$-th day (inclusive).

Write a program that returns the first and last days of the longest series of days when fewer than two guards were on duty!

### Input
The first line of the input contains two numbers: $N, M$ - the number of days and guards.
The next line $M$ contains two numbers: $F_i, L_i$ - where the $i$-th guard was on duty from the $F_i$-th day to the $L_i$-th day (inclusive).

### Output
The first and last days of the longest series when fewer than two guards were on duty should be printed in a single line (separated by space)! If there is more than one solution, then print the one with the smallest first day. If there are no solutions, then print only a single 0.

### Constraints
* $1 \le N \le 1000$
* $1 \le M \le 1000$
* $1 \le F_i \le U_i \le M$ for all $1 \le i \le M$.

### Example 1 Input
    6 5
    1 3
    6 6
    1 2
    2 3
    3 4

### Example 1 Output
    4 6

### Explanation of Example 1
During the first day there were 2, on the second day there were 3, on the third day there were 3, on the fourth day there were 1, on the fifth day there were 0, and finally on the sixth day there were 1 guard on duty. So between the fourth and sixth days, there were less than 2 guards on duty.

### Example 2 Input
    10 10
    8 10
    4 5
    2 3
    7 10
    1 8
    5 9
    1 3
    6 7
    5 6
    6 10

### Example 2 Output
    0
