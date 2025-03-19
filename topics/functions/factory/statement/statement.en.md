## Factory
You work as a supervisor in a factory where robots are assembled. Each robot consists of a body and an even number of limbs, meaning that an odd number of parts is required to build it. You are given a list that contains the number of parts assigned to each robot. Your task is to notify the factory as soon as you find a robot that has been assigned an even number of parts. Since robots are built quickly, there is no time to report all faulty robots. The factory only expects you to return the index of the first robot with an even number of parts (indexing starts from 0). If no such robot exists, return -1. Write a function to accomplish this task!

### Template
Start from the predefined template code! Do not change anything in the main program, otherwise it will not be accepted. You need to implement the `first_even` function, which takes a sequence of numbers as a parameter and returns the position of the first even number, using 0-based indexing.

### Constraints
* $1 \le N \le 1000$, where $N$ is the size of the number sequence.
* All elements of the sequence are between $1$ and $1000$.

### Example
In the sequence (1 5 9 3 2 4), the first even number to appear is 2, at index 4.
