## Longest Substring
Enterprise received the same message twice ($A$, $B$), but both times the original message was corrupted. Our task is to determine the longest common substring. The common substring can help us understand the message.

### Input
The first line of the input contains a string: $A$ - the first message.
The second line of the input contains a string: $B$ - the second message.

### Output
Print a single number, the length of the longest common substring in the two messages.

### Constraints
* $1 \le |A|,|B| \le 2000$
* both strings contain lowercase English letters

### Example input
    ancientlanguagesx
    modernlanguagesy

### Example output
    9

### Explanation of the example
The longest contiguous common part is "languages".
