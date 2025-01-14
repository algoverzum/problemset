## Second Occurrence
A spacecraft on a remote expedition sends coded messages back to a space station at the regular intervals. These messages consist of a single lower case letter of the English alphabet. Create a program that determines the second occurrence of the code "f" in each message. If there was only one occurrence of "f", the output is -1, and if there was none, the output is -2.

### Input
The first line of the input contains $S$ - the letters of the codes, joined into a single string.

### Output
Print a single number, the position of the second f character if there are at least two. If there is only one then print -1, if there is none then -2.

### Constraints
* $1 \le S$ length $ \le 256$
* S contains only lower case letters of the English alphabet

### Example input
    aqwsfgfd

### Example output
    6

### Explanation of the example
The index of the second f character is 6.
