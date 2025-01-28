## Fleet Formation
You are leading a Fleet into battle, before the battle starts you want to arrange your ships so that you have your strongest ships in the middle and your weakest ships at the sides. You do this by putting your strongest ship in the middle, then your second strongest to the left of it, then your third strongest to the right of them, and so on. Print the strength of your ships after sorting, from left to right.


### Input
The first line of the input contains a single odd integer: $N$<br>
The second line of the input contains $N$ amount of $H$ numbers, the power of your ships 

### Output
Print $N$ numbers, the power of your ships

### Constraints
* $1 \le N \le 999$
* $1 \le H \le 10000$

### Example input
    7
    33 32 3 40 4 35 2

### Example output
    3 32 35 40 33 4 2

### Explanation of the example
strongest ship is 40, because there are even number of ships it will be placed 4th, because it will have the largest force in the middle, because the second strongest ship will be placed to the left of it.<br>
second strongest ship 3rd place<br>
third strongest 5th place<br>
fourth strongest 2nd place<br>
fifth strongest 6th place<br>
6th strongest 1st place<br>
7th strongest 7th place<br>