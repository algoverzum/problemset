## Large Digits
For an integer $n$, let $S(n)$ be the sum of the digits of $n$. For example, $S(123)=1+2+3=6$.

Given two three-digit integers, $A$ and $B$, determine the larger of $S(A)$ and $S(B)$.

### Input
The first line of the input contains an integer: $A$.

The second line of the input contains an integer: $B$.

### Output
Print the larger of $S(A)$ and $S(B)$. If they are equal, print $S(A)$.

### Constraints
* $100 \le A,B \le 999$

### Example input 1
    123
    234

### Example output 1
    9

### Explanation of example 1
$S(123)=1+2+3=6$ and $S(234)=2+3+4=9$, so we need to print the larger value: 9.

### Example input 2
    593
    953

### Example output 2
    17

### Example input 3
    100
    999

### Example output 3
    27
