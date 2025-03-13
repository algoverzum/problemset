## Ship Rental
In the space port of Mo-Seis-Ley, adventurers, smugglers and bounty hunters from all over the galaxy can rent $N$ spaceships. For the next $M$ days, the rental periods are known: which spaceship was rented, from which day to which day. Write a program that determines the day on which the most spaceships are rented.

### Input
The first line of the input contains the number of available spaceships ($1 \le N \le 100$), the number of days ($1 \le M \le 1000$) and the number of rentals ($1 \le K \le 1000$).

The next $K$ lines contains the charter data: the spacecraft ID ($1 \le S_i \le N$) and the first and last day ($1 \le A_i \le B_i \le M$) when the spacecraft was rented. There is no conflict or overlap between the data.

### Output
In the first and only line of the output, write the number of the day on which the highest number of spaceships were rented (if there are more than one such day, the earliest day shall be selected).

### Constraints
* $1 \le N \le 100$
* $1 \le M \le 1000$
* $1 \le K \le 1000$
* $1 \le S_i \le N$
* $1 \le A_i \le B_i \le M$

### Example input
    3 10 5
    1 4 8
    2 3 5
    3 8 8
    2 6 9
    3 1 4

### Example output
    4

### Explanation of the example
Three ships were rented on the fourth day. It can be verified that this is the maximum.
