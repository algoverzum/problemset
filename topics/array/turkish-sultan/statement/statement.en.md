## Turkish Sultan
In the Turkish sultan’s prison there are $N$ cells, numbered from 1 to $N$. All cell doors are initially closed.

On his birthday the sultan first felt cheerful, so he sent the 1st servant to open all cell doors (doors $1, 2, 3, \ldots, N$).

Later he changed his mind and ordered the 2nd servant to toggle every 2nd cell door: if it was open, close it; if it was closed, open it (that is, cells $2, 4, 6, \ldots$).

Then the 3rd servant came, who toggled every 3rd cell door ($3, 6, 9, \ldots$).

This process continues up to the $N$-th servant, who toggles only the $N$-th cell door.

Write a program that outputs which doors remain open in the end — that is, which prisoners are released!

### Input
The first line of the input contains $N$ - the number of prison cells.

### Output
Print the numbers of the cells whose doors remain open in the end, i.e., the prisoners who are released.
Print the cell numbers in one line, in increasing order, separated by spaces.

### Constraints
* $1 \le N \le 100$

### Example input
    6

### Example output
    1 4

### Explanation of the example
After the 1st servant: open, open, open, open, open, open

After the 2nd servant: open, closed, open, closed, open, closed

After the 3rd servant: open, closed, closed, closed, open, open

After the 4th servant: open, closed, closed, open, open, open

After the 5th servant: open, closed, closed, open, closed, open

After the 6th servant: open, closed, closed, open, closed, closed

Thus, the 1st and 4th cells remain open.
