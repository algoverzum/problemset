## Second Occurrence
A spacecraft on a remote expedition sends coded messages back to a space station at the regular intervals. These messages consist of a single lowercase letter of the English alphabet, and they are numbered starting from 0. Create a program that determines which message was the second occurrence of the code `x`. If there was only one occurrence of `x`, print -1, and if there was none, print -2.

### Input
The first line of the input contains $S$ - the letters of the messages, joined into a single string.

### Output
Print a single number, the position of the second `x` character if there are at least two. If there is only one then print -1, if there is none then -2.

### Constraints
* $1 \le S$ length $ \le 256$
* $S$ contains only lower case letters of the English alphabet

### Example input
    aqwaxgxd

### Example output
    6

### Explanation of the example
The index of the second `x` character is 6.
