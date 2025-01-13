## Minimal Word
On Coruscant, a droid assembly line is malfunctioning, and its memory core has been scrambled. It begins generating random strings of galactic terms instead of coherent instructions. To restore the droid factory's functionality, the Rebel slicer must find the alphabetically first term in the list of scrambled words from the memory core.
Given a list of words produced by the droid's scrambled output, determine the alphabetically first word.

### Input
The first line of the input contains $N$ - the number of words.
The second line contains $N$ space separated words. Each word contains only lower case letters.

### Output
Print a single word, the first word in alphabetical order.

### Constraints
* $1 \le N \le 100$
* each word contains only lower case letters

### Example 1 input
    5
    how preach coarse at descent

### Example 1. output
    at

### Explanation of example 1
There is only one word starting with "a".

### Example 2 input
    6    
    who wise whose western weekend would

### Example 2 output
    weekend

### Explanation of example 2
All words start with "w", we need to look at the second letter. Two of them start with "we", so we need to even consider the third letter.   
