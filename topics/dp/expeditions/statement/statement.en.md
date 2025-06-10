## Expeditions
The Galactic Archaeological League has launched the Ancient Relic Expeditions, aiming to survey and extract the lost technologies of ancient civilizations from various planetary surfaces.
The surface of each planet is divided into sectors, and every expedition team can submit a permit request for a contiguous range of sectors.
Each request specifies the starting and ending sector for exploration,
and the amount of credits they offer to the League in exchange for the exploration rights.
The League’s objective is to select the permits that result in the highest total number of credits — ensuring that no sector is assigned to more than one team at a time.
Help the League make the best decision!

### Input
The first line contains two integers:  
$N$ : the number of permit requests  
$M$ : the number of sectors on the planet  
Each of the next $N$ lines contains three integers:  
$A_i$ : starting sector, $B_i$ : ending sector, $K_i$ : the amount of credits offered for the expedition  


### Output
The first line should contain the maximum total number of credits achievable.  
The second line should contain the indices of the selected permit requests (in any order). If multiple solutions exist, you can print any one of them.

### Constraints
* $1 \le N, M \le 1000$
* $1 \le A_i \le B_i \le 1000$ for all $i=1 \dots N$
* $1 \le K_i \le 1000$ for all $i=1 \dots N$

### Example input
    5 7
    2 3 600
    6 6 180
    3 4 900
    1 6 990
    4 7 600


### Example output
    1200
    1 5


### Explanation of the example
We accept the first and fifth permit requests.
The first provides 600 credits, and the fifth provides 600 credits, totaling 1200 credits. It can be proven, that the League cannot earn more credits.
