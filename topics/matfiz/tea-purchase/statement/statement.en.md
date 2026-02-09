## Most Tea Purchased
In a discount grocery store, records are kept of tea purchases. For every purchase, they record which company's tea was bought and in what quantity.

The task: Create a program that **gives the index of the purchase with the largest quantity**!

If multiple purchases have the largest quantity, the **smallest index** must be printed.

### Input
The first line of the input contains the value of $N$, the number of sales records, followed by $N$ **pairs of lines**, each containing:

1. the name of the tea type (text)
2. the quantity purchased $M$

### Output
Print the index of the purchase with the largest quantity to the **first line** of the standard output!
In case of multiple maximums, print the **smallest index** among them.

### Constraints

- $1 \le N \le 100$
- $1 \le M \le 20000$

### Example Input
    6
    Lipton
    200
    Teekanne
    100
    Lipton
    600
    Lipton
    800
    Pickwick
    200
    Greenfield
    800

### Example Output
    4

### Explanation
There are two 800s, but the 4th comes earlier (Lipton), not the 6th (Greenfield).
