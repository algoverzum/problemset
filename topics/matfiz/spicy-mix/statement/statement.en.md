## Spicy Mix
Rudolf is preparing a new, special spicy dish. According to the recipe, he must mix exactly two spices:

* one from box $A$,
* one from box $B$.

Each spice has a spiciness value, indicating how hot it is.

* Box $A$ contains $n$ spices with spiciness values $a_1, a_2, \ldots, a_n$.
* Box $B$ contains $m$ spices with spiciness values $b_1, b_2, \ldots, b_m$.

Rudolf wants the total spiciness of the dish to not exceed the allowed limit $k$, otherwise the dish would be unbearably hot.

This means that the $i$-th spice from box $A$ and the $j$-th spice from box $B$ can only be mixed if $a_i + b_j \le k$.

Your task is to count how many pairs $(i,j)$ of spices exist such that their total spiciness does not exceed $k$.

### Input
The first line contains three integers $n, m, k$.  
The second line contains $n$ integers - the spiciness values of the spices in box $A$.  
The third line contains $m$ integers - the spiciness values of the spices in box $B$.

### Output
Print a single integer, the number of pairs $(i,j)$ such that $a_i + b_j \le k$.

### Constraints
* $1 \le n,m \le 1000$
* $1 \le a_i \le 1000$ for all $i = 1,2,\ldots,n$
* $1 \le b_j \le 1000$ for all $j = 1,2,\ldots,m$
* $1 \le k \le 2000$

### Example input 1
    4 4 8
    1 5 10 14
    2 1 8 1

### Example output 1
    6

### Explanation of the example 1
Rudolf can choose the following index pairs: [1,1], [1,2], [1,4], [2,1], [2,2], [2,4].

### Example input 2
    2 3 4
    4 8
    1 2 3

### Example output 2
    0    

### Explanation of the example 2
No matter which two spices Rudolf chooses, their total spiciness exceeds $k=4$.

### Example input 3
    3 4 2000
    1 1 1
    1 1 1 1

### Example output 3
    12

### Explanation of the example 3
Rudolf can choose any spice from box $A$ and any spice from box $B$.
