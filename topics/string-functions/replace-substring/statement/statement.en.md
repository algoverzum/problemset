## Replace Substring
In a distant part of the galaxy, the Resistance intercepted a critical message sent by the First Order. But there was a problem: the message had been corrupted by the First Order's hackers. Instead of the word "HOPE", the message kept repeating "FEAR".

Leia turned to R2-D2:
*R2, we must fix this message. Every time you see the word "FEAR", replace it with "HOPE". This message is too important to be lost!*

### Input
The input contains $S$ - the message to be fixed. $S$ might look to you as random list of characters. 

### Output
Print the corrected string, replacing "FEAR" with "HOPE" in $S$ everywhere. 

### Constraints
* $4 \le $ the length of $S$ $ \le 1000$
* $S$ contains only upper case English letters

### Example input
    FEARISFEAR

### Example output
    HOPEISHOPE

### Explanation of the example
"FEAR" appers twice in the input and we need to replace both.
