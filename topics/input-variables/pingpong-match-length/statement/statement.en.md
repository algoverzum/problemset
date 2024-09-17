## Ping-pong Match Length
Ping-pong matches can take very long on our planet, especially if creatures with multiple hands play with multiple bats. You are given the start and end time of a ping-pong match in the following format:

    H
    M

Here $H$ and $M$ are integer numbers denoting the hour and the minute in a 24-hour time format. There are no leading zeroes in the numbers, for example, if the starting time is 13:05, you would get `13` and `5` in the input.

Determine the length of the ping-pong match in minutes. You can assume that the match ended the same day as it started, and it lasted at least one minute, so the end time is bigger than the start time. One hour is 60 minutes.

### Input
The input contains four integer numbers on separate lines: $SH, SM, EH, EM$ - the starting hour, starting minute, ending hour, and ending minute of the ping-pong match.


### Output
Print a single number, the length of the ping-pong match in minutes.

### Constraints
* $0 \le SH, EH \le 23$
* $0 \le SM, EM \le 59$

### Example input
    9
    59
    13
    5

### Example output
    186

### Explanation of the example
The ping-pong match starts at 9:59 and ends at 13:05, so it lasts 3 hours and 6 minutes, which is 186 minutes.
