## More Oxygen
An alien planet is being terraformed by space travellers to make it habitable for humans. An important step is to ensure that the planet's oxygen levels are consistently at the right level. To check this, the scientists on the mission have set up a series of measuring stations that read out the oxygen levels in their environment every day, represented as an integer. The scientists want to know when in the last few days each measuring station measured a higher value than the day before. Such days are called *nice* days. Your job is to help them find all the nice days. Note: the first day cannot be nice because there is no previous day.

### Input
The first line of the input contains two integers, the number of measuring stations $N$ and the number of days $M$.
The following $N$ lines contains $M$ numbers each, corresponding to the oxygen level measured at the $i$-th measuring station on the $j$-th day: $A_{i,j}$.  

### Output
In the first line of the output, you should write the count of *nice* days, and in the second line, the indicies of all such days in increasing order, separated by spaces. 

### Constraints
* $1 \le N \le 100$
* $2 \le M \le 100$
* $1 \le A_{i,j} \le 1000$

### Example input
    3 5
    2 10 4 5 7 8
    11 12 13 14 15 15
    1 20 42 1 13 13

### Example output
    2
    2 5

### Explanation of the example
On the second day, the results of the three measuring stations are: 1. 10>2, 2. 12>11, 3. 20>1. The results of the fifth day are: 1. 7>5, 2. 15>14, 3. 13>1. Apart from these two days, there are no other days when the condition is fulfilled.
