## Factory
Robots are assembled on an industrial planet. Each robot is made up of a body and an even number of limbs, meaning that an odd number of parts are needed to build it. As a factory supervisor, your job is to use your list of parts ordered for each robot to notify the factory as soon as possible if you find a robot with an even number of parts ordered. Since robots are made so quickly, you don't have time to send all the faulty robots. Only print out the index of the first robot with an even number of parts, counted from 1. If there are none, write $-1$.

### Template
Start from the predefined template code! Do not change anything in the main program, otherwise it will not be accepted. You need to write the `first_even` function, which takes as parameters the sequence of numbers and the limit and returns the number of items below the limit.

### Constraints
* $1 \le N \le 1000$, where $N$ is the size of the number sequence.
* All elements of the sequence are between $1$ and $1000000$.

### Example
In the sequence (1 5 9 3 2 4), the first even number to appear is 2, at the 5th index.