## Triple
Given an array $a$ containing $n$ numbers, output the smallest number that appears at least three times in the array, or output $-1$ if no such number exists.

### Input
The first line of the input contains a single integer: $n$ - the length of the array.  
The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1\le a_i\le n$ - the elements of the array.

### Output
Print a single number: the smallest number that appears at least three times, or print -1 if no such number exists.

### Constraints
* $1 \le N \le 10^5$
* $1 \le a_i \le n$ for every $i=1, 2,\ldots, n$.

### Example input 1
    5
    1 5 2 4 3

### Example output 1
    -1

### Explanation of the example
All numbers are distinct, so none appears at least three times; therefore, the answer is -1.

### Example input 2
    8
    2 2 3 3 4 4 2 2

### Example output 2
    2

### Explanation of the example
The number 2 appears four times, so the answer is 2.

### Example input 3
    10
    3 1 2 3 1 2 3 1 2 3

### Example output 3
    1

### Explanation of the example
The numbers 1, 2, and 3 each appear at least three times, and the smallest among them is 1, which is the correct answer.
