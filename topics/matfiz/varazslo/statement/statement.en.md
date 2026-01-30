## Wizard
Leo is a young apprentice wizard who has just begun studying basic number spells. He is currently learning how to add numbers together.

One day, the wizard teacher writes a sum on the blackboard. The apprentices are asked to compute its value. To keep things simple, the sum contains only the numbers 1, 2, and 3. Even so, this task is still difficult for Leo. Since he is only starting out, he can calculate the sum only if the numbers appear in non-decreasing order. For example, he cannot handle the sum $1+3+2+1$, but he can easily compute $1+1+2$ and $3+3$.

You are given the sum written on the board. Rearrange it and print the sum in a form that Leo can calculate.

### Input
The first line contains a non-empty string $s$ — the sum that Leo needs to calculate. The string $s$ contains no spaces and consists only of digits and the '+' character. It is guaranteed that $s$ is a correctly written sum that contains only the numbers 1, 2, and 3. The length of $s$ does not exceed 100 characters.

### Output
Print a single number, the

### Constraints
* $1 \le |s| \le 100$
* The string $s$ contains no spaces and consists only of digits and the '+' character. It is guaranteed that $s$ is a correctly written sum that contains only the numbers 1, 2, and 3.

### Example 1 input
    3+2+1

### Example 1 output
    1+2+3

### Example 2 input
    1+1+3+1+3

### Example 2 output
    1+1+1+3+3

### Example 3 input
    2

### Example 3 output
    2
