## Plates
Dr. Patel has $N$ stacks of plates. Each stack contains $K$ plates. Every plate has a **beauty value** (a positive integer) that describes how beautiful it is.

Dr. Patel would like to select exactly $P$ plates for dinner such that the total sum of the beauty values of the selected plates is as large as possible.

**Important rule:**
If he wants to take a plate from a stack, he must also take all plates above it in that stack. In other words, plates can only be selected from the top of a stack downward.

### Input
The first line contains the number of test cases: $T$.  
The first line of each test case contains three integers:

* $N$ – the number of stacks,
* $K$ – the number of plates in each stack,
* $P$ – the number of plates to be selected.

Then $N$ lines follow.

* The $i$-th line contains $K$ integers representing the beauty values of the plates in the given stack, listed **from top to bottom**.

### Output
For each test case, output the maximum possible total beauty value on a separate line.

### Constraints
* $1 \le T \le 10$
* $1 \le K \le 30$
* $1 \le N \le 50$
* $1 \le P \le N\cdot K$
* The beauty values are between 1 and 100, inclusive.

### Example Input
    2
    2 4 5
    10 10 100 30
    80 50 10 50
    3 2 3
    80 80
    15 50
    20 10

### Example Output
    250
    180

### Explanation of the example
**Test case 1:** We need to select 5 plates. From the first stack, take the top 3 plates: $10 + 10 + 100 = 120$. From the second stack, take the top 2 plates: $80 + 50 = 130$. Total: $120 + 130 = 250$.

**Test case 2:** We need to select 3 plates. From the first stack, take the top 2 plates: $80 + 80 = 160$. Take no plates from the second stack. From the third stack, take the top plate: $20$. Total: $160 + 20 = 180$.
