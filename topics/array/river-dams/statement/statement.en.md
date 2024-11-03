## River Dams
We want to build a new hydroelectric power plant on a river, the width of which has been measured at $N$ different points. From the selected points, we can build a hydroelectric power plant at those points where the width of the river is greater than the previous and next points. Since we have no measurement data before the first point and after the last point, they are not suitable for building a hydroelectric power plant. At how many points can we build a hydroelectric power plant?

### Input
The first line of the input is a number, the number of points on the river: $N$.
The second line contains $N$ numbers, the width at each point: $A_1, A_2, \ldots A_N$.

### Output
You have to print one number, the number of places suitable for building a hydroelectric power plant, i.e. the number of measurement points where the measured width is strictly greater than the width measured at the point before and after.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 10000$

### Example input
    5
    5 1 5 1 5

### Example output
    1

### Explanation of the example
The river is wider at the third point than at the second and fourth points. Although it is also wider at the first and fifth points than it is next to them, because they are on the edge, they are not considered good locations.
