## Last Occurrence
The Interplanetary Fleet needs to recover an old, corrupt database containing important navigational data. While analyzing the database, they discovered that a key letter always tells them the location of the last valid signal in a given data packet. The engineering team has now asked you to find the last occurrence of a letter in a word so they can recover the corresponding data. If the letter is missing, the data packet is unfortunately unusable.

### Input
An $S$ word indicating the contents of the data packet.
A letter $C$ indicating the key letter.

### Output
A single number, the last occurrence of the key letter. If the word $S$ does not contain the key letter $C$, print -1.

### Constraints
The word $S$ consists of letters of the English alphabet and is up to 1000 letters long. The letters can be upper or lower case.
The key letter $C$ is a lower or upper case letter from the English alphabet.

### Example input
    Incomprehensibilities 
    i

### Example output
    19

### Explanation of the example
    Incomprehensibilities is 21 letters long. the character 'i''s last occurrence is at index 19.
