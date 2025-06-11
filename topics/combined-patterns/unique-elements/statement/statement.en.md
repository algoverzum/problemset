## Unique Elements
We want to identify which items in a warehouse have only one unit remaining, so we can offer them to customers at a discount.
Write a program that determines, from a list of $N$ item codes, which ones appear **exactly once**, and prints them **in the order they appear in the input**.

### Input
The first line of the input contains a single integer $N$ — the number of items.
The second line of the input contains $N$ integers, the codes of each item: $A_1, A_2, \ldots, A_N$.

### Output
In the first line of the output, you must print the codes of the items that appear only once in the list of codes. You must print them in the order of occurrence, separated by spaces.

### Constraints
* $1 \le N \le 1\,000$
* $1 \le A_i \le 10\,000$

### Example input
    7
    4 2 1 3 3 2 3

### Example output
    4 1

### Explanation of the example
The item codes `4` and `1` each appear only once in the list, so they are printed.
Item codes `2` and `3` appear multiple times and are therefore excluded.
