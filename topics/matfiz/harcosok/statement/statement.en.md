## Warriors
In a fantasy game, there are $n$ warriors. The number of warriors is even. The strength of the $i$-th warrior is denoted by $a_i$.

The game master wants to form $\frac{n}{2}$ pairs such that:

* each pair consists of exactly two warriors,
* each warrior belongs to exactly one pair,
* a pair can only be formed by warriors with equal strength (otherwise they cannot fight together).

Warriors can train to increase their strength.
Each training session increases a warrior's strength by 1.

The game master wants to know the minimum total number of training sessions required so that exactly $\frac{n}{2}$ pairs can be formed (i.e., every warrior has a partner).

Your task is to determine this minimum number.

### Input
The first line contains an integer $n$ — the number of warriors. It is guaranteed that $n$ is even.

The second line contains $n$ integers: $a_1, a_2,\ldots,a_n$, where $a_i$ is the strength of the $i$-th warrior.

### Output
Output a single integer - the minimum total number of training sessions required to form exactly $\frac{n}{2}$ pairs.

### Constraints
* $2 \le n \le 100$
* $1 \le a_i \le 100$ for all $i = 1,2,\ldots,n$

### Example 1 input
    6
    5 10 2 3 14 5

### Example 1 output
    5

### Explanation of example 1
The optimal pairs of warriors are: (3,4),(1,6),(2,5), where the numbers in parentheses are the indices of the warriors in the input.

For the first pair (3,4), the difference in strength is $|3 - 2| = 1$, so 1 training session is needed.

For the second pair (1,6), the difference is $|5 - 5| = 0$, so 0 trainings are needed.

For the third pair (2,5), the difference is $|14 - 10| = 4$, so 4 trainings are needed.

The total number of trainings is therefore $1 + 0 + 4 = 5$.

### Example 2 input
    2
    1 100

### Example 2 output
    99

### Explanation of example 2
In the second example, the first warrior needs 99 training sessions to match the strength of the second warrior and form a pair.
