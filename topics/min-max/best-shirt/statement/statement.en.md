## Best Shirt
My friend Nena wants to buy a shirt for her friend's birthday. In the store, you can choose from $N$ shirts whose prices are $P_1, P_2, \ldots, P_N$ liards. Nena has $K$ liards, she wants to buy the most expensive shirt possible, for which she still has enough money, because she knows that the better a shirt is, the more expensive it is. Which shirt should you choose and how many liards will it cost?

### Input
The first line of the input contains two integers: $N$ and $K$ - the number of shirts and Nena's pocket money in liards. The second line contains $N$ integers separated by spaces, the prices of the shirts ($P_1, P_2, \ldots, P_N$).

### Output
Print two numbers in separate lines, the first number should be the index of the selected shirt, and the second should be the price. If there are several shirts with this price, then the smallest index must be printed. If Nena cannot buy a shirt, then write a 0 in both lines of the output.

### Constraints
* $1 \le N \le 100$
* $1 \le K \le 1000$
* $1 \le P_i \le 1000$

### Example input
    7 333
    95 760 130 299 334 299 42

### Example output
    4
    299

### Explanation of the example
Nena can buy shirts 1, 3, 4, 6 and 7 with her 333 liards (their prices are 95, 130, 299, 299, 42). The most expensive of these is the 4th, which costs 299 liards (the 6th is also 299 liards, but the smaller index must be printed).

### Example 2 input
    4 42
    150 50 900 299

### Example 2 output
    0
    0

### Explanation of the example 2
Unfortunately, Nena can't buy any shirt.
