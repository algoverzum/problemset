## Longest Ascent
A brilliant scientist, Dr Pulsar, has long dreamed of flying into space, but instead of rockets, he must rely on the planet's natural resources. He has chosen a special mountainous region where he has accurately mapped the altitude of the terrain on previous expeditions. The plan is simple: launch his spacecraft from a long ascent to give him as much time as possible to accelerate. For the launch to be successful, he needs to find the longest continuous ascent in the terrain. An ascent is a section of altitudes where at each measurement point the altitude increases from the previous one. The scientist is asking you to help him determine the start and end points of the longest ascent.

### Input
The first line of the input contains $N$. <br /> 
Followed by $N$ lines each containing the height of the $i$-th measurement: $M_i$ ($i=1, 2, \ldots, N$).

### Output
Print two integers, the start and end indices of the longest ascent. If there are no ascents, then print -1. If there are multiple possible solutions, you should print the one with the smallest start index.

### Constraints
* $1 \le N \le 1000$
* $1 \le M_i \le 1000$

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
The ascent $100<110<115$ consists of 3 height measurements.

The ascent $105<115<125<130$ consists of 4 height measuerements, this is the longest ascent.
