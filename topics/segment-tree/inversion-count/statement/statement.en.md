## Inversion Count
Given an array $A$ consisting of $n$ distinct positive integers, a pair of indices $(i,j)$ is called an inversion if $i<j$ and $A[i]>A[j]$.

Your task is to determine the number of inversions in the given array.

### Input
The first line contains an integer $T$, the number of test cases.

Each test case begins with an integer $n$, the size of the array. The second line contains $n$ space-separated integers, where the $i$-th integer denotes $A[i]$.

### Output
For each test case, print a single line containing the number of inversions in the corresponding array.

### Constraints
* $1 \le T \le 100$
* $1 \le n \le 200,000$
* $1 \le A[i] \le 10^6$ for all $i$
* All elements of the array are distinct.
* The sum of $n$ over all test cases does not exceed 200000.

### Example input
    3    
    3
    3 1 2
    5
    2 3 8 6 1
    1
    10

### Example output
    2
    5
    0
