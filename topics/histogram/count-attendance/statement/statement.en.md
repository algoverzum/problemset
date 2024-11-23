## Count Attendance
Moo Seis Lee has 10 children enrolled in a small school. For each of the past $N$ days, the number of children who attended school was recorded. From this, we want to calculate that how many days attended the school exactly $0,1,\ldots,9$ or $10$ children.

### Input
The first line of the input contains an integer $N$ - the number of days under consideration.
The second line contains $N$ space-separated numbers $A_1,A_2,\ldots,\A_N$ - where $A_i$ is the number of children attending school on the $i$-th day.

### Output
You need to print 11 space-separated integers $H_0,H_1,\ldots,\A_{10}$ - where $H_i$ is the number of days when exactly $i$ children attended the school.

### Constraints
* $1 \le N \le 400$
* $0 \le A_i \le 10$

### Example input
    15
    8 9 10 0 0 1 3 5 7 9 7 3 1 10 9

### Example output
    2 2 0 2 0 1 0 2 1 3 2

### Explanation of the example
On the fourth and fifth days, no one went to school because of a sandstorm, so the first number is 2. The answer also shows that there were 2 days when everyone was present, and on 3 days only 1 child was absent, etc.
