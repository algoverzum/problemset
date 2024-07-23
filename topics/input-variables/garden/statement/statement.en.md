## Garden
My friend, Chitoti has a garden that has a rectangular shape, where the two sides of the rectangle are $A$ and $B$ meters long. She wants to do two things:
 - Put a fence around the garden. For this, she needs to buy new wire fence as long as the total length of the four sides of the garden.
 - Plant a chirimori tree in each 1m by 1m sized square of the garden, if we imagine partitioning the complete garden to squares (see image below).

What is the total length of the wire fence that she needs to buy?

How many chirimori trees will she be able to plant?

### Input
The input contains the integer numbers $A$ and $B$ on two separate lines - the side lengths of the garden.


### Output
In the first line of the output, print the total lengths of the fence to be bought.
In the second line of the output, print the number of trees that she can plant.

### Constraints
* $1 \le A, B \le 100$

### Example input
    3
    5

### Example output
    16
    15

### Explanation of the example
The garden has two sides of length 3m and two sides of length 5m, so the perimeter is $2 \cdot (3 + 5) = 16$.

She can plant 15 trees as the image below shows:

![grid](garden.png)
