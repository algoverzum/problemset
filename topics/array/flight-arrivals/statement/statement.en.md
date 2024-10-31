## Flight Arrivals
Mo Sais Lee has two airports: Espa and Pelgo. We know how many airplanes are arriving today and how many passengers will be on those planes. We would like to distribute these machines alternately between them. The first plane should go to Espa, the second to Pelgo, the third to Espa, etc. The two airports want to know as soon as possible how many passengers are on the planes arriving to them.

### Input
The first line of the input contains a single integer: $N$ - the number of airplanes arriving that day.
In the second line we have the space separated numbers $A_0, A_1, \ldots, A_{N-1}$, the number of people arriving on each plane.

### Output
In the first line of the output, print the number of passengers on the planes going to Espa, separated by a space. (That is, $A_0, A_2, A_4, \ldots$ should be written here.)
In the second line of the output, write the number of passengers on the planes going to Pelgo, separated by a space. (That is, $A_1, A_3, A_5, \ldots$ should be written here.)

### Constraints
* $1 \le N \le 100$
* $0 \le A_i \le 100$

### Example input
    5
    1 2 3 4 5

### Example output
    1 3 5
    2 4

### Explanation of the example
The first plane has 1 passenger to Espa, the second plane has 2 passengers to Pelgo, the third plane has 3 passengers to Espa, the fourth plane has 4 passengers to Pelgo, while the fifth plane has 5 passengers to Espa. So 1, 3, 5 passengers go to Espa, and 2, 4 to Pelgo.
