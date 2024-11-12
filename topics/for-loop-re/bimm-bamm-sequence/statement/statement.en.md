## Bimm-Bamm Sequence
Some kids are playing the game where they say out the numbers in order, but they have to say `bimm` instead of numbers that are multiples of 3, `bamm` instead of numbers that are multiples of 5, and `bumm` instead of numbers that are multiples of both 3 and 5. Can you write a program that prints everything that they say up to a given integer number $N$?

### Input
The first line of the input contains $N$ - the upper limit of the game.

### Output
Print $N$ lines, each line should contain a number, or the appropriate word (`bimm` / `bamm` / `bumm`) that has to be said instead of the number.

### Constraints
* $1 \le N \le 100$

### Example input
    8

### Example output
    1
    2
    bimm
    4
    bamm
    bimm
    7
    8

### Explanation of the example
The kids have to say `bimm` instead of 3 and 6, because they are divisible by 3, and `bamm` instead of 5, because it is divisible by 5. The example doesn't contain `bumm`, the first time that it should be used would be in place of the number 15.
