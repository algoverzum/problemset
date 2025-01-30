## Staircase
The entrance to the Jedi Temple has a staircase with $N$ steps. A young padawan can jump up to $K$ steps at a time using the Force.
He goes up to the Temple once each day for training.

CreateMake a program that calculates how many days the padawan can climb the stairs in different ways!

### Input
In the input, there are two integers in a single line: $N, K$ - the number of steps and the maximum jump size. 

### Output
You need to output a single number that gives you the total number of different jumps up to the temple.

### Constraints
* $1 \le N \le 32$
* $1 \le K \le 16$

### Example input 1
    3 2

### Example output 1
    3

### Explanation of the example
The possible jumps are $(1,1,1)$, $(1,2)$ and $(2,1)$, where the numbers are the magnitude of the jumps. 

### Example input 2
    20 5

### Example output 2
    400096
