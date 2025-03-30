## Bonie Sequence
Bonis are fascinating creatures that live for $N$ years, and each boni can give birth to one baby boni per year. They have their first offspring after two years, and from then on, they give birth to one baby boni each year until the end of their lives. Initially, there is one newborn boni. Can you determine how the number of bonis evolves each year over the $N$ years of its life?

### Input
The input consists of a single integer: $N$ - the number of years.

### Output
You must print $N + 1$ numbers in a single line, separated by spaces: $B_0, B_1, \ldots, B_N$, where $B_0=1$ and $B_i$ represents the number of bonis after $i$ years.

### Constraints
* $1 \le N \le 30$

### Example input
    5

### Example output
    1 1 2 3 5 8

### Explanation of the example
After one year, there is still only one boni. After two years, a new boni is born, making a total of two. After three years, another boni is born, bringing the total to three. After four years, the first-born boni also starts reproducing, resulting in 2 new bonis, making a total of 5. After five years, three bonis are at least two years old, so 3 new bonis are born, leading to a total of 8. The sequence ends here, as the original boni will pass away afterward.
