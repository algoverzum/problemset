## Shortest Word
You want to enter the treasury of an ancient civilization. During your adventures, you have already obtained the keyword list, but several words are on the list as misleading clues. Fortunately, you know the keyword is the shortest word on the list. Find the keyword!

### Input
The first line of the input contains a single integer: $N$ 
The second line contains $N$ words separated by a space.

### Output
Print the shortest word in the input. If there is more than one shortest word, Print the one that occurred first.

### Constraints
* $1 \le N \le 100$
The words consist of the letters of the English alphabet and are almost 1000 letters long. The letters can be lowercase or uppercase.

### Example input
    6
    silver gold iron bronze platinum copper

### Example output
    gold

### Explanation of the example
    silver 6 letters
    gold 4 letters
    iron 4 letters
    bronze 6 letters
    platinum 8 letters
    copper 6 letters
    There are 2 4 four-letter words, but gold occurs first, so gold is the keyword.
