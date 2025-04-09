## Election
We're looking for an astronaut to lead a voyage. We want to select this by voting, but due to poor organisation, the votes were put into several different boxes, so now we have to sum them up. Write a program that can sum up the number of votes for each candidate from several pairs of **candidate - vote count**.

### Input
The first line of input is a single integer, the number of vote packets: $N$.
The next line $N$ contains a string $S_i$ and an integer $A_i$ separated by a space, the name of the candidate and the number of votes.

### Output
Print all candidates in alphabetical order on separate lines in the following way:

The first element of the line should be the name of the candidate, followed by the number of votes, separated by a space.

### Constraints
* $1 \le N \le 1000$
* $S_i$ contains only lowercase letters of the English alphabet and its length is at most 10 for each $1 \le i \le N$
* $1 \le A_i \le 10000$ for each $1 \le i \le N$

### Example input
    5
    dreebo 5
    eeper 2
    dreebo 2
    dreebo 6
    scrimbler 8

### Example output
    dreebo 13
    eeper 2
    scrimbler 8

### Explanation of the example
dreebo received votes in several different packets, so they are added together. The others had only one packet each.
