## Fragment
On board, the spacecraft "Mars Explorer" is a data collection system that receives various secret messages from space. The spacecraft's software is responsible for extracting a fragment from a given message, that falls between the first and last occurrence of a given letter, including the first and last occurrence of the letter. If the given letter does not occur in the message, this error should be reported by giving -1 as the result. Can you help writing the program for this?

### Input
The first line of the input is a string $S$, the message. It does not contain spaces.
The second line contains a $C$ character.

### Output
Print the part of the $S$ string between the first and last occurrence of the $C$ character, including the first and last occurrence of the character. If the $C$ character does not occur in $S$, print -1.

### Constraints
* The string $S$ consists of lowercase letters of the English alphabet and is up to 1000 characters long.
* The character $C$ is a lowercase letter of the English alphabet.

### Example input
    fragmented
    e

### Example output
    ente

### Example input 2
    message
    m

### Example output 2
    m

### Example input 3
    hello
    x

### Example output 3
    -1
