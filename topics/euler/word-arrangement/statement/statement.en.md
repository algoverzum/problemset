## Word Arrangement
A secret door contain a very interesting word puzzle. The team of archaeologists has to solve
it to open that door. Because there is no other way to open the door, the puzzle is very important
for us.
There is a large number of magnetic plates on the door. Every plate has one word written on
it. The plates must be arranged into a sequence in such a way that every word begins with the same
letter as the previous word ends. For example, the word ‘acm’ can be followed by the word ‘motorola’.
Your task is to write a computer program that will read the list of words and determine whether it
is possible to arrange all of the plates in a sequence (according to the given rule) and consequently to
open the door.

### Input
The first line of the input contains a single integer: $N$
The next $N$ lines contains an $S$ word. 

### Output
You have to print out one word, YES if you can put the words in the right order, NO if not.

### Constraints
* $1 \le N \le 100000$
The $S$ words are at least 1 and up to 10 characters long. And they consist of lowercase letters of the English alphabet.

### Example input
    6
    entrance
    exit
    code
    token
    cryptic
    enigmatic

### Example output
    YES

### Explanation of the example
enigmatic -> cryptic -> code -> entrance -> exit -> token

