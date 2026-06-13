## Workout
Tambourine has $N$ training sessions, where each session duration is given in minutes ($M_i$). The values are strictly increasing.

The **difficulty** of the training program is defined as the maximum difference between consecutive sessions (in minutes).

Tambourine may insert up to $K$ additional training sessions anywhere in the sequence. Each inserted session must have a positive integer duration, and the resulting sequence must remain strictly increasing.  
The goal is to add sessions in such a way that the maximum difference between consecutive sessions in the final sequence is minimized. In other words, we want to make the program as easy as possible by inserting at most $K$ sessions.

### Input
The first line of the input contains $N$ and $K$ (the number of sessions and the maximum number of insertions).

The second line contains $N$ integers: $M_1, M_2, \ldots, M_N$, where $M_i$ is the duration of the $i$-th session in minutes. The values are strictly increasing.

### Output
Print a single integer: the minimum possible difficulty after inserting at most $K$ additional sessions.

### Constraints
* $2 \le N \le 10^5$
* $1 \le K \le 10^5$
* $1 \le M_i \le 10^9$
* $M_i < M_{i+1}$ for all $i = 1, 2, \ldots, N-1$

### 1. Example Input
    3 1
    100 200 230

### 1. Example Output
    50

### Explanation of Example 1
Only one insertion is allowed ($K = 1$). We insert a new session at 150 minutes:

$100 \to 150 \to 200 \to 230$

The consecutive differences are:

$100 \to 150 = 50$

$150 \to 200 = 50$

$200 \to 230 = 30$

The maximum difference is 50, which is the minimum achievable.

### 2. Example Input
    5 2
    10 13 15 16 17

### 2. Example Output
    2

### Explanation of Example 2
Tambourine may add up to two sessions. The inserted sessions are shown in bold:
$10, \mathbf{12}, 13, \mathbf{14}, 15, 16, 17$. 
The resulting difficulty is 2.

### 3. Example Input
    5 6
    9 10 20 26 30

### 3. Example Output
    3

### Explanation of Example 3
Tambourine may add up to six sessions. The inserted sessions are shown in bold:
$9, 10, \mathbf{12}, \mathbf{14}, \mathbf{16}, \mathbf{18}, 20, \mathbf{23}, 26, \mathbf{29}, 30$.
The resulting difficulty is 3.

### 4. Example Input
    8 3
    1 2 3 4 5 6 7 10

### 4. Example Output
    1

### Explanation of Example 4
Tambourine may add up to three sessions. The inserted sessions are shown in bold: $1, 2, 3, 4, 5, 6, 7, \mathbf{8}, \mathbf{9}, 10$.
The resulting difficulty is 1. (In fact, Tambourine only inserted **two** sessions.)
