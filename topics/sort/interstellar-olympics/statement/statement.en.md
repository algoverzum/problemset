## Interstellar Olympics
In the Milky Way system, the Olympic Games have just ended. After the event, we recorded all the gold, silver and bronze medals won by each planet. These are entered in a table, where the data for the planet with the id number $i$ is entered in the $i$th row. Based on these, we would like to rank each planet in order of who has won the most medals. The rule of ranking is as follows. If two planets have the same number of gold medals, the one that has more silver medals will be ranked first. If the two planets have the same number of gold medals, the one with more bronze medals will be the first. If all the medals have the same number, the one with the lower id will be placed first. Sort the planets according to this order.

### Input
The first line of the input is an integer, the number of planets: $N$
The next $N$ line of the input is three numbers in order, the number of gold, silver and bronze medals: $G_1 \dots, G_N; S_1 \dots S_N; B_1 \dots B_N$

### Output
n the output, you need to write a single line with $N$ integers, sorting the numbers of the planet's ids by the medals.

### Constraints
* $1 \le N \le 100$
* $1 \le G_i \le 1000$
* $1 \le S_i \le 1000$
* $1 \le B_i \le 1000$

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
The first, fourth and fifth rows can be sorted by the number of gold medals. The second and third rows are decided by the number of silver medals.
