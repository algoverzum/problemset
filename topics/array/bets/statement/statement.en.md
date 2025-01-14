## Bets
My friend Akiko likes to bet on space races. At the end of every day for the last $N$ days, he recorded how much money he had. He is curious to see how much money he won each day, i.e. how much his money changed from the previous day (if his money decreased, it's a negative win). He also wants to know how much more or less he won on each day compared to the previous day, so he also wants to calculate the change between winnings (same as before, so if his winnings have decreased, the change is negative). Can you help him with this?

### Input
The first line of the input is the number of days: $N$.
The next line contains $N$ numbers, Akiko's money at the end of each day: $A_1, A_2, \ldots, A_{N}$.

### Output
Print two lines, both with the numbers separated by spaces.
In the first line, print $N-1$ numbers, Akiko's winnings for each day starting from the second day (there is no information about his money before the first day).
In the second line, print $N-2$ numbers, the changes between adjacent winnings.


### Constraints
* $3 \le N \le 100$
* $1 \le A \le 10000$

### Example input
    6
    4 9 2 5 13 10

### Example output
    5 -7 3 8 -3
    -12 10 5 -11

### Explanation of the example
On the second day he had 9 money and on the first day only 4, so on the second day his winnings were $9 - 4 = 5$. On the third day his money went down to 2, so he lost 7, so his winnings are -7, etc.

The changes between winnings are in the second row, for example the first number is the change between 5 and -7, which is -12.
