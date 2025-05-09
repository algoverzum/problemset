## Expeditions
The Galactic Archaeological League has launched the Ancient Relic Expeditions, aiming to survey and extract the lost technologies of ancient civilizations from various planetary surfaces.
The surface of each planet is divided into sectors, and every expedition team can submit a permit request for a contiguous range of sectors.
The requests are submitted in encrypted form, and each request specifies:
the starting and ending sector for exploration,
and the amount of credits they offer to the League in exchange for the exploration rights.
The League’s objective is to select the permits that result in the highest total number of credits — ensuring that no sector is assigned to more than one team at a time.
Help the League make the best decision!



### Input
The first line contains two integers:
$N$ : the number of permit requests
$M$ : the number of sectors on the planet<br>
Each of the next $N$ lines contains three integers:
$A$ : starting sector
$B$ : ending sector
$K$ : the amount of credits offered for the expedition<br>
The input permit requests are given in non-decreasing order of their ending sector $B$.

### Output
The first line should contain the maximum total number of credits achievable.<br>
The second line should contain the indices of the selected permit requests, listed in increasing order.

### Constraints
* $1 \le N \le 1000$
* $1 \le A,B \le 1000$
* $1 \le K \le 1000$

### Example input
    4 5
    2 3 500
    4 4 600
    4 5 500
    1 5 1000


### Example output
    1100
    1 2


### Explanation of the example
We accept the first and second permit requests.
The first provides 500 credits, and the second provides 600 credits, totaling 1100 credits.
