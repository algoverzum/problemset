## Election
We're looking for an astronaut to lead a voyage. We want to select this by voting, but due to poor organisation, the votes were put into several different boxes, so now we have to sum them up. Write a program that can sum up the number of votes for each candidate from several pairs of "candidate"-"vote count".

### Input
The first line of input is a single integer, the number of vote packets: $N$.
The next line $N$ contains a string and an integer separated by a space, the name of the candidate and the number of votes: $S_1, S_2, \dots, S_N$; $A_1, A_2, \dots, A_N$

### Output
Write out all candidates in alphabetical order on separate lines in the following way:
The first element of the line should be the name of the candidate, followed by the number of votes, separated by a space.

### Constraints
* $1 \le N \le 1000$
* $1 \le $ length of $ S_i \le 256$
* $1 \le A_i \le 10000$

### Example input
    5
    Dreebo 5
    Eeper 2
    Dreebo 2
    Dreebo 6
    Scrimbler 8

### Example output
    Dreebo 13
    Eeper 2
    Scrimbler 8

### Explanation of the example
Dreebo received votes in several different packets, so they are added together. The others had only one packet each.
