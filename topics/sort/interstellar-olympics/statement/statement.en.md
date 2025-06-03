## Interstellar Olympics
The Olympic Games have just ended in the Milky Way. After the event, we recorded how many gold, silver, and bronze medals each planet won. The data was organized into a table, where the $i$-th row contains the results of the planet with index $i$.  
We want to sort the planets based on their medal results according to the following rules:

* A planet ranks higher if it has more gold medals.
* If the number of gold medals is equal, the one with more silver medals ranks higher.
* If the number of silver medals is also equal, the one with more bronze medals ranks higher.
* If all medal counts are the same, the planet with the smaller index ranks higher.

After sorting, print the order of the planets.

### Input
The first line of the input contains an integer $N$, the number of planets.  
The next $N$ lines each contain three integers — the number of gold, silver, and bronze medals (the $i$-th line corresponds to the $i$-th planet):

$G_1, S_1, B_1$  
$G_2, S_2, B_2$  
$\vdots$  
$G_N, S_N, B_N$

### Output
Print a single line containing $N$ integers — the indices of the planets sorted by their medal counts.

### Constraints
* $1 \le N \le 100\,000$
* $1 \le G_i \le 10^6$ for every $i = 1,\ldots,N$
* $1 \le S_i \le 10^6$ for every $i = 1,\ldots,N$
* $1 \le B_i \le 10^6$ for every $i = 1,\ldots,N$

### Example input
    5
    4 4 4
    3 2 3
    3 3 1
    1 5 5
    2 1 1

### Example output
    1 3 2 5 4

### Explanation of the example
Planet 1 has the most gold medals (four). The second highest number (three) is tied between planets 2 and 3, but the number of silver medals breaks the tie in favor of planet 3. Then comes planet 5 with two gold medals, and finally planet 4 with one gold medal — despite having many medals in total.
