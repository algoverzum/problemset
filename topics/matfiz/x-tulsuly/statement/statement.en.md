## Dominant X
Lili is a young fairy who considers the letter "x" very important. Lili is given a magic word called $s$. She calls a word good if more than half of its characters are the letter "x". For example, "xxbxx" and "axxx" are good words, while "bxcx", "xvvvx", or the empty word ("") are not.

Lili may delete some characters from the word $s$. She wants to know what the longest good word she can obtain is after deleting some (possibly zero) characters. It is guaranteed that the word contains at least one "x", so a valid answer always exists.

### Input
The first line contains a string $s$, consisting of lowercase English letters.  
It is guaranteed that the string $s$ contains at least one "x".

### Output
Print a single integer — the length of the longest good word that Lili can obtain after deleting some (possibly zero) characters from $s$.


### Constraints
* $1 \le |s| \le 100$
* It is guaranteed that the string contains at least one "x".

### Example Input 1
    axaaaax

### Example Output 1
    3

### Explanation of Example 1
In the first example, it is sufficient to delete any four "a" characters. The answer is 3, since this is the maximum number of characters that can remain.

### Example Input 2
    xxxbxx

### Example Output 2
    6

### Explanation of Example 2
In the second example, no characters need to be deleted.
