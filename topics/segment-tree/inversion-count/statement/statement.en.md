## Inversion Count
Given an array $A$ consisting of $n$ distinct positive integers, a pair of indices $(i,j)$ is called an inversion if $i<j$ and $A[i]>A[j]$.

Your task is to determine the number of inversions in the given array.

### Input
The first line contains an integer $T$, the number of test cases.

Each test case begins with an integer $n$, the size of the array. The next $n$ lines contain the elements of the array, where the $i$-th of these lines contains $A[i]$.

Consecutive test cases are separated by a blank line.

### Output
For each test case, print a single line containing the number of inversions in the corresponding array.

### Constraints
* $1 \le n \le 200,000$
* $1 \le A[i] \le 10^6$ for all $i$
* All elements of the array are distinct.
* The sum of $n$ over all test cases does not exceed 200000.

### Example input
    2
    
    3
    3
    1
    2
    
    5
    2
    3
    8
    6
    1

### Example output
    2
    5
