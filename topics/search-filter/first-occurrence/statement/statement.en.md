## First Occurrence
Space explorer Fleet Commander Gammos intercepts a mysterious radio message from the edge of the distant Infinity Sector. The message consists of a single word and contains an important coordinate. Gammos must find where the key letter first appears in the message to decipher the direction in which the expedition must head. If the key letter is not in the message, the message is wrong.

### Input
An $S$ word indicating the contents of the data packet.
A letter $C$ indicating the key letter.

### Output
A single number, the first occurrence of the key letter. If the word $S$ does not contain the key letter $C$, print -1.

### Constraints
The word $S$ consists of lowercase letters of the English alphabet and is up to 1000 letters long.
The key letter $C$ is a lowercase letter from the English alphabet.

### Example input
    surreptitious  
    u

### Example output
    2

### Explanation of the example
    surreptitious is 13 letters long. the character 'u''s first occurrence is at index 2.
