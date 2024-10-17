## Bimm, Bamm, Bumm
Kids here like to play a game with numbers: they will say out loud the numbers in order starting from 1, but sometimes they have to say a word instead of the current number. Specifically:

* if the current number is a multiple of 3, they should say `bimm`,

* if it is a multiple of 5, they should say `bamm`,

* and if it is a multiple of both 3 and 5, they should say `bumm`
instead of the number.

There is a number in the input, which is the current number in the game. Print the word that the kids should say, or the number itself if they don't need to substitute it.


### Input
The first line of the input contains an integer $N$ - the current number.


### Output
Print what the kids have to say, the number itself, or `bimm`/`bamm`/`bumm` based on its divisibility by 3 and 5.

### Constraints
* $1 \le N \le 100$

### Example input
    7

### Example output
    7

### Second example input
    5

### Second example output
    bamm

### Explanation of the example
7 is not the multiple of 3 or 5, so the kids have to say the number itself. 5 is a multiple of 5, but not a multiple of 3, so they have to say `bamm`.
