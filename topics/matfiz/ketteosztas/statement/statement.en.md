## Split in Two
You are given $n$ integers. The task is to divide the numbers into two non-empty parts such that:

* Each part contains at least one element.
* The sums of the elements in the two parts have the same parity.

For example, if the given numbers are [1, 2, 4, 3, 2, 3, 5, 4], then the two parts can be: [1, 2, 3] and [4, 2, 3, 5, 4], where the sum of the elements in the first part is 6 and in the second part is 18.


### Input
The first line contains an integer, $n$ - the number of given integers.  
The next line contains $n$ integers, $a_1, a_2, \ldots, a_n$ - the given $n$ numbers.

### Output
Print "YES" (without quotes) if it is possible to divide the numbers into two parts such that the parity of the sums of the elements in both parts is the same and each part contains at least one element; otherwise print "NO".

### Constraints
* $2 \le n \le 50$
* $1 \le a_i \le 50$ for all $i=1, 2, \ldots, n$.

### Example Input 1
    8
    1 2 4 3 2 3 5 4

### Example Output 1
    YES

### Explanation of Example 1
The first example is described in the problem statement.

### Example Input 2
    2
    4 7

### Example Output 2
    NO

### Explanation of Example 2
There are only two possible partitions: [4], [7] and [7], [4], but in both cases the parity of the sums is different.
