## Longest Substring
The starship Enterprise received the same message twice ($A$, $B$), but both instances were corrupted during transmission. Your task is to determine the length of the longest contiguous common substring between the two messages. This will help assess the extent of the corruption.

### Input
The first line of the input contains a string: $A$ - the first message.
The second line of the input contains a string: $B$ - the second message.

### Output
Print a single number, the length of the longest common substring in the two messages.

### Constraints
* $1 \le |A|,|B| \le 2500$
* Both strings consist only of lowercase English letters.

### Example input
    ancientlanguagesx
    modernlanguagesy

### Example output
    9

### Explanation of the example
The longest contiguous common part is "languages".
