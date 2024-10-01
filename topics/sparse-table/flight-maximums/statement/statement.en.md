## Flight Maximums
There's an interesting bird on our planet, the *arboreon*, which lives in the tops of roadside trees. Along a road there are $N$ trees with heights $H_1, H_2, \ldots, H_N$. There are $Q$ arboreon birds perched at the top of some trees, and for each bird we even know how old it is: the $i$th bird is at the top of the tree $S_i$, and its age is $K_i$ years.

Each bird will visit the top of some number of consecutive trees depending on its age, in search of food, starting from its starting position. A bird of age 0 will go nowhere, so it will only visit its starting tree, a bird of age 1 will move on to the next tree, so it will visit two trees, a bird of age 2 will visit four trees in a row, and so on, i.e. a bird of age $K$ will visit $2^K$ trees. So the $i$-th bird visits the tops of the following trees in sequence: $S_i, S_i+1, \ldots, S_i+2^{K_i}-1$. It is guaranteed that no bird will go beyond the $N$-th tree.

For each bird, determine the maximum height it will visit. Formally, for each $i$, find the value of $max\{ H_j | S_i \le j < S_i+2^{K_i} \}$. 

### Input
In the first line of the input, there are two integers $N$ and $Q$ - the number of trees and birds. The second line contains $N$ integers, the height of each tree ($H_1, H_2, \ldots, H_N$). Each of the following $Q$ lines contains two numbers $S_i$ and $K_i$ - the starting position and age of the $i$-th arboreon bird. 


### Output
Output $Q$ numbers on separate lines, the $i$-th line should contain the height of the highest tree visited by the $i$-th bird. 

### Constraints
* $1 \le N \le 100\,000$
* $1 \le Q \le 300\,000$
* $1 \le H_i \le 10^9$ $(i = 1, 2, \ldots, N)$
* $1 \le S_i \le N$ $(i = 1, 2, \ldots, Q)$
* $0 \le K_i \le 17$ $(i = 1, 2, \ldots, Q)$
* $1 \le S_i + 2^{K_i} \le N$ $(i = 1, 2, \ldots, Q)$

### Example input
    9 4
    13 42 7 9 1 25 7 1 2
    2 1
    4 2
    1 3
    9 0

### Example output
    42
    25
    42
    2

### Explanation of the example
The first bird visits the second and third trees, their heights are 42, 7, the largest of which is 42.

The heights of the trees visited by the second bird are: 9, 1, 25, 7, the tallest being 25.

The heights of the trees visited by the third bird are 13, 42, 7, 9, 1, 25, 7, 1, the tallest being 42.

The fourth bird visits only the last tree, which is of height 2.
