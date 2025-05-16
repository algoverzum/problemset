## Delivery Tracker
The Galactic Postal Service operates on the planet Tatooine, delivering packages to various locations. The planet's surface is mapped using coordinates similar to geographic systems: latitude and longitude, represented as integers.

For each delivery, the following information is recorded:

* the latitude coordinate of the target location ($X_i$),
* the longitude coordinate of the target location ($Y_i$),
* and the number of packages delivered ($P_i$).

Multiple deliveries may be made to the same location.
Your task is to determine the location on Tatooine that received the highest total number of packages.

### Input
The first line contains a single integer $N$ — the number of deliveries.

Each of the next $N$ lines contains three integers: $X_i$, $Y_i$, and $P_i$, where: $X_i$ and $Y_i$ are the coordinates of the delivery location (integers) and 
$P_i$ is the number of packages delivered in that delivery.

### Output
Print one line with three integers: $X, Y, P$, where $(X, Y)$ is the coordinate of the location that received the most packages in total, and $P$ is the total number of packages delivered there.

If multiple locations received the same maximum number of packages, you may print any one of them.

### Constraints
* $1 \le N \le 10^5$
* $-10^9 \le X_i, Y_i \le 10^9$ for all $1 \le i \le N$
* $1 \le P_i \le 10^9$ for all $1 \le i \le N$

### Example input
    5
    2 3 5
    1 4 2
    2 3 4
    0 0 1
    1 4 1

### Example output
    2 3 9

### Explanation of the example
The location at coordinates $(2, 3)$ received two deliveries: 5 and 4 packages, for a total of 9. No other location received more packages.
