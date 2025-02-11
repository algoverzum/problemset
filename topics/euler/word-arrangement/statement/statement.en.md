## Word Arrangement
An ancient, secret door contains a mysterious word puzzle. The team of archaeologists can only open it if they manage to solve the riddle. Since there is no other way to gain entry, cracking the puzzle is crucial for them.

The door is covered with numerous magnetic plates, each with a word written on it. The plates must be arranged in such a way that each word starts with the same letter that the previous word ends with. For example, the word "delta" can be followed by "arrow" because it starts with "a".

Your task is to create a computer program that reads a list of words and determines whether it is possible to arrange all the plates according to the given rule – and thus unlock the door.

### Input
The first line of the input contains a single integer: $N$, the number of words.
Each of the next $N$ lines contains one word. 

### Output
You have to print one word, `YES` if you can put the words in the right order, `NO` if not.

### Constraints
* $1 \le N \le 100\,000$
* The words are at least 1 and up to 10 characters long, and they consist of lowercase letters of the English alphabet.

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

