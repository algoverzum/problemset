## Sort
For geological research on our planet, we have taken rock samples and broken them down into elements, which we would like to sort into order based on their periodic table numbers for two groups of researchers. One group of researchers would like to receive them in ascending order and the other in descending order. Write a program that will print both types of ordering.

### Input
The first line of the input contains a single integer, the number of elements $N$.
The second line of the input contains $N$ integers, the periodic table numbers of the elements: $A_1, A_2, \ldots, A_N$.

### Output
In the first line of the output, print $N$ numbers, the periodic table numbers of the elements in ascending order.
In the second line of the output, you must print $N$ numbers, the periodic table numbers of the elements in descending order.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 103$

### Example input
    8
    3 12 5 7 9 9 10 1

### Example output
    1 3 5 7 9 9 10 12
    12 10 9 9 7 5 3 1

### Explanation of the example
The numbers in the input are sorted first in ascending order and then in descending order.
