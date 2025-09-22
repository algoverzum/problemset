## Dices
While the most typical type of dice have 6 sides, each of which shows a different integer 1 through 6, there are many games that use other types. In particular, a $D_K$ is a die with $K$ sides, each of which shows a different integer 1 through $K$. A $D_6$ is a typical die, a $D_4$ has four sides, and a $D_{1000000}$ has one million sides.

![](dices.png)

In this problem, we start with a collection of $N$ dice. The $i$-th die is a $D_{S_i}$, that is, it has $S_i$ sides showing integers 1 through $S_i$.

A straight of length $M$ is the list of integers $1, 2, \ldots, M$. We want to choose some of the dice (possibly all) and pick one number from each to form a straight. What is the longest straight we can form in this way?

### Input
The first line of the input contains $N$ - the number of dice in the game.

The second line contains $N$ integers $S_1, S_2, \ldots, S_N$, each representing the number of sides of a different die.

### Output
Print a single number, the maximum number of input dice that can be put in a straight.

### Constraints
* $1 \le N \le 10^5$
* $4 \le S_i \le 10^6$, for all $i$

### Example input 1
    4
    6 10 12 8

### Example output 1
    4

### Explanation of the example 1
We can use all dice to create $1,2,3,4$

### Example input 2
    6
    5 4 5 4 4 4

### Example output 2
    5

### Explanation of the example 2
Since none of the dice can show an integer greater than 5, there is no way to have a straight with more than 5 dice. There are multiple ways to form a straight with exactly 5 dice. For example, pick the integers 4 and 5 for both $D_5$'s and then integers $1,2$ and $3$ for three of the $D_4$'s to form $1,2,3,4,5$.

### Example input 3
    10
    10 10 7 6 7 4 4 5 7 4

### Example output 3
    9

### Explanation of the example 3
It is possible to form the straight $1,2,3,4,5,6,7,8,9$ by discarding one $D_4$ and using the $D_4$'s, $D_5$, and $D_6$ to get 1 through 4; the $D_7$'s to get 4 through 7; and the $D_{10}$'s to get 8 and 9. There is no way to form a straight of length 10, so this is the best that can be done

### Example input 4
    1
    10

### Example output 4
    1

### Explanation of the example 4
We can only form a straight of length 1.
