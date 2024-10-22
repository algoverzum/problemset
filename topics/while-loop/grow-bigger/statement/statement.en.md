## Grow Bigger
While studying the fauna of our planet, researchers have found two different subspecies of brumara, called type A and type B brumara. Type A brumara are born with a smaller body weight but grow faster, while type B brumara are born with a larger body weight but grow more slowly.
A type A brumara will triple its own weight in a year, while a type B will double its own. Help the researchers work out how many years it will take for Type A to outgrow Type B among the newborn brumara they are studying.

### Input
The input consists of two lines. The first line contains a single number, the weight of the type A brumara: $A$. The second line contains a single number, the weight of the type B brumara: $B$.

### Output
You need to print a single number, the number of years after which the type A brumara will be strictly heavier than the type B brumara.

### Constraints
* $1 \le A \le B \le 10$

### Example input
    4
    7

### Example output
    2

### Explanation of the example

After one year, the weight of the brumaras will look like this: A = 4 * 3 = 12, B = 7 * 2 = 14. At this point, type A has not yet outgrown type B, so we wait another year. For the second year, this will change to A = 12 * 3 = 36, B = 14 * 2 = 28. At this point type A has a weight that is strickly greater then that of type B, so we output 2.

### Second example input
    4
    9

### Second example output
    3

### Explanation of the example

After two years, the weight of both brumara will be 36, so only after the third year will type A have a weight that is stricktly larger then type B.
