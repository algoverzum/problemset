## Fleet Formation
You are leading a Fleet into battle, before the battle starts you want to arrange your ships so that you have your strongest ships in the middle and your weakest ships at the sides. You do this by putting your strongest ship in the middle, then your second strongest to the left of it, then your third strongest to the right of them, and so on. Print the strength of your ships after sorting, from left to right.


### Input
The first line of the input contains a single odd integer: $N$.<br>
The second line of the input contains $N$ numbers, $H_1,H_2,\ldots,H_N$, the power of your ships.

### Output
Print $N$ numbers, the power of your ships

### Constraints
* $1 \le N \le 999$
* $1 \le H_i \le 10000$

### Example input
    7
    33 32 3 40 4 35 2

### Example output
    3 32 35 40 33 4 2

### Explanation of the example
The strongest ship is 40, because there are odd number of ships it will be placed 4th. The second strongest ship (35) gets the 3rd place. The third strongest (33) goes to the 5th place, the fourth strongest (32) to the 2nd place, the fifth strongest (4) to the 6th place, the 6th strongest (3) to the 1st place and the 7th strongest (2) to the 7th place.
