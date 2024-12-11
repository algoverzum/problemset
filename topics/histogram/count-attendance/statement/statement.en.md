## Count Attendance
Moo Seis Lee has 10 children enrolled in a small school. For each of the past $N$ days, tthe number of children attending school each day was recorded. sing this data, we want to determine how many days exactly $0,1,\ldots,9$ or $10$ children attended school.

### Input
The first line of the input contains an integer $N$ - the number of days under consideration.
The second line contains $N$ space-separated numbers $C_1,C_2,\ldots,C_N$ - where $C_i$ is the number of children attending school on the $i$-th day.

### Output
You need to print 11 space-separated integers $H_0,H_1,\ldots,H_{10}$ - where $H_i$ is the number of days when exactly $i$ children attended the school.

### Constraints
* $1 \le N \le 400$
* $0 \le C_i \le 10$

### Example input
    15
    8 9 1 0 0 1 3 5 7 9 7 3 1 10 9

### Example output
    2 3 0 2 0 1 0 2 1 3 2

### Explanation of the example
On the fourth and fifth days, no one went to school because of a sandstorm, so the first number is 2. The answer also shows that there were 3 days when only one child was present, and there were no such days when exactly two kids attended school, etc.
