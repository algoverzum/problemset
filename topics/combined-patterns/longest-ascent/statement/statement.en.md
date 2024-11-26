## Longest Ascent
A scientist built a spaceship, sadly he has no rocket to propell his spaceship up. So he will launch his spaceship off a cliff. The scientist in his older research measured the height of the terrain in fixed intervals. For the highest rate of success the scientist wants to find the longest ascent in the nearby terrain, so the spaceship can accelerate as much as possible. A sequence of numbers of heights is called an ascent if each element is greater than the one before it. The length of an ascent is the number of integers in the sequence.

### Input
The first line of the input contains $N$  <br /> 
Followed by $N$ lines each containing the $M$ height of the $N$-th measurement.

### Output
Print 2 numbers, the start and end points of the longest ascent. If there are no ascents, then write -1.

### Constraints
* $1 \le N \le 1000$
* $1 \le M \le 1000$

### Example input
    10
    100
    110
    115
    110
    105
    115
    125
    130
    125
    125

### Example output
    5 8

### Explanation of the example
    100<110<115  3 heights
    105<115<125<130  4 heights, this is the longest ascent

