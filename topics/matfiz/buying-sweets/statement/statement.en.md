## Buying Sweets
I set out to buy cake and doughnuts with $X$ euros.

First, I bought a cake for $A$ euros at a pastry shop. Then I went to a doughnut shop and bought as many doughnuts as I could. One doughnut costs $B$ euros.

How much money did I have left after shopping?

### Input
The input contains the integers $X, A, B$ on three separate lines:

$X$

$A$

$B$

### Output
Print how much money is left after shopping.

### Constraints
* $1 \le A,B \le 1000$
* $A + B \le X \le 10,000$
* $X, A$ and $B$ are integers

### Example input 1
    1234
    150
    100

### Example output 1
    84

### Explanation of example 1
After buying a cake, $1234-150=1084$ euros remained. With this amount, 10 doughnuts can be bought, leaving 84 euros.

### Example input 2
    1000
    108
    108

### Example output 2
    28
    
### Example input 3
    579
    123
    456

### Example output 3
    0

### Example input 4
    7477
    549
    593

### Example output 4
    405
