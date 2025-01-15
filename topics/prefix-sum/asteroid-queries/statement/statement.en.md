## Asteroid Queries
Welcome to our planet! We need your help!
It has been $N$ days since the asteroid-rain started to fall on us.
We recorded the number of asteroids that we detected each day $(A_i, i=1, 2, \ldots, N)$.

Our mage, Sigissimus says that he can disrupt the force to stop the catastrophe, but he needs to know instantly the answer to two types of questions:

1. How many asteroids were detected in the first $K$ days altogether?
2. How many asteroids were detected in total between two given days (including the beginning and end)?

Sigissimus asks a lot of questions, please help us in giving the answers!

### Input
The first line contains $N$ and $Q$ - the number of days and number of questions. The second line contains N integers $(A_1, A_2, \ldots, A_N)$ - the number of asteroids detected each day.

Each of the next $Q$ lines describes one question in the form of `1 K` or `2 L R`.
The first number is the type of question, and depending on this:

* for type 1 there is a second number, the value $K$ in the question,
* for type 2 there are two more numbers $L$ and $R$ - the start and end day of the period.

### Output
You should print $Q$ integers in separate lines, the answers to the questions, in the same order as the input.

### Constraints
* $1 \le N \le 100\,000$
* $1 \le Q \le 100\,000$
* $0 \le A_i \le 10\,000$
* $1 \le K \le N$
* $1 \le L \le R \le N$

### Example input
    5 2
    4 11 0 6 1
    1 3
    2 3 5


### Example output
    15
    7

### Explanation of the example
The first question asks the total number of asteroids in the first 3 days: 4 + 11 + 0 = 15.
In the second question we have to calculate the sum of asteroids on day 3, 4 and 5: 0 + 6 + 1 = 7.

