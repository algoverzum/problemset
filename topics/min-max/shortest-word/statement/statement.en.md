## Shortest Word
You want to enter the treasury of an ancient civilization. During your adventures, you have already obtained the keyword list, but several words are on the list as misleading clues. Fortunately, you know the keyword is the shortest word on the list, if there are multiple shortest words, then the keyword is the one that appears first. Find the keyword!

### Input
The first line of the input contains a single integer: $N$, the number of words on the list. 
The second line contains $N$ words separated by a space.

### Output
Print the shortest word in the input. If there are more than one shortest words, print the one that occurred first.

### Constraints
* $1 \le N \le 100$
* The words consist of lowercase letters of the English alphabet and are at most 1000 letters long.

### Example input
    6
    silver gold iron bronze platinum copper

### Example output
    gold

### Explanation of the example
* silver 6 letters
* gold 4 letters
* iron 4 letters
* bronze 6 letters
* platinum 8 letters
* copper 6 letters

There are two four-letter words, but gold occurs first, so gold is the keyword.
