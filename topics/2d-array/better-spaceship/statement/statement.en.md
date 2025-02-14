## Better Spaceship
We evaluate the properties of spaceship models with integers, because we want to find the ones that are redundant. Write a program that finds the spacecraft whose ratings are better than another in all respects.

### Input
The first line of the input contains two integers, the number of spaceships and the number of evaluation criteria: $N$ and $M$.
The next line $N$ contains $M$ integers, the rating of the $i$-th spacecraft in category $j$: $S_{i,j}$.

### Output
You have to print one number, the index (indexed from 1) of the spaceship whose rating is better than another in all categories. If there are more than one, write the lowest number, if there are none, write -1.

### Constraints
* $1 \le N,M \le 100$
* $1 \le S_{i,j} \le 1000$

### Example input
    3 5
    10 15 12 10 10
    11 11 11 11 20
    12 16 16 16 20

### Example output
    3

### Explanation of the example
The third spaceship has better properties than the first spaceship.
