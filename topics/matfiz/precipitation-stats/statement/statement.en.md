## Precipitation Statistics

For the past $N$ weeks, we measured the amount of precipitation that fell every day, in millimeters. Write a program that determines the wettest week!

### Input
The first line of the standard input contains the number of weeks ($N$). The following $N$ lines each contain the 7 precipitation amounts for a week ($C$).

### Output
The standard output must contain the serial number (1-based index) of the wettest week in a single line (in case of multiple solutions, the one with the smallest serial number)!

## Constraints
- $2 \le N \le 1000$
- $0 \le C_{i,j} \le 1000$

### Example

#### Example 1 Input

    6
    5 10 15 20 25 30 35
    0 2 0 0 0 0 0
    0 0 0 1 0 3 0
    0 1 2 3 4 5 6
    5 1 0 0 2 1 0
    0 0 0 0 0 0 0

#### Example 1 Output

    1

#### Example 2 Input

    2
    1 0 1 0 0 0 1
    0 1 0 1 1 0 0

#### Example 2 Output

    1