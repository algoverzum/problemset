## Coldest Day
We have a magical animal, the josi, that can tell $N$ days in advance what the daily average temperature will be on each day. It gives the temperature as an integer (it cannot make a more accurate prediction than that). For one of the next $N$ days, we are organizing a snow battle with our friends and we want to choose the coldest day for this. Knowing the temperatures predicted by josi, can you tell which day will be the coldest and how many degrees will the temperature be?

### Input
The first line of the input contains $N$ - the number of days. The second line contains $N$ integers separated by spaces, the temperatures of each day ($T_1, T_2, \ldots, T_N$).

### Output
You have to print two numbers in two separate lines. The first line should contain the lowest temperature. The second line should be the index of the day when the temperature will be this low. If there are more than one such days, then the fits index should be printed.

### Constraints
* $1 \le N \le 100$
* $-100 \le T_i \le 100$

### Example input
    5
    10 4 -5 -2 -5

### Example output
    -5
    3

### Explanation of the example
The lowest temperature is -5 degrees and it will be for the first time on the 3rd day.
