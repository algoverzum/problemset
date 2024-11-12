## Unique Elements
We want to find out which of the items in a warehouse only have one item left, because we want to sell them to customers at a discount. Create a program that can determine from the code of $N$ items which ones are only in the sequence once and write them in the order that they appear in.

### Input
The first line of the input is a single integer, the number of items: $N$
The second line of the input contains $N$ integers, the codes of each item: $A_1, A_2, \ldots, A_N$

### Output
In the first line of the output, you must print the codes of the items that appear only once in the list of codes. You must print them in the order of occurrence, separated by spaces.

### Constraints
* $1 \le N \le 1000$
* $1 \le A_i \le 10000$

### Example input
    6
    1 2 2 3 3 3

### Example output
    1

### Explanation of the example
The item code 1 appears only once in the sequence, so it is printed, while the item codes 2 and 3 appear several times in the sequence, so they are not printed.
