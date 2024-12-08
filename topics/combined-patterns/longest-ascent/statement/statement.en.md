## Longest Ascent
A brilliant scientist, Dr Pulsar, has long dreamed of flying into space, but instead of rockets, he must rely on the planet's natural resources. He has chosen a special mountainous region where he has accurately mapped the altitude of the terrain on previous expeditions. The plan is simple: launch his spacecraft from a long ascent to give him as much time as possible to accelerate. For the launch to be successful, he needs to find the longest continuous ascent in the terrain. An ascent is a section of altitudes where at each measurement point the altitude increases from the previous one. The scientist is asking you to help him determine the start and end points of the longest ascent.

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

