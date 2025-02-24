## Count Words
The crew of the Millennium Falcon has received another mission from the Rebels. The message is, of course, encrypted. To decode it, they first need to count how many unique words appear in the message. R2-D2 solved this in the blink of an eye. Can you do it too?

### Input
The first line of the input contains an integer: $N$ - the number of words in the message.
The second line contains $N$ space-separated words.

### Output
You must print a single number: the count of unique words in the message.

### Constraints
* $1 \leq N \leq 100000$
* Each word consists of lowercase letters of the English alphabet and is at most 20 characters long.


### Example input
    25
    ten green bottles sitting on the wall and if one green bottle should accidentally fall there will be nine green bottles sitting on the wall

### Example output
    18

### Explanation of the example
"green" appears 3 times. "bottles", "sitting", "on", "the", and "wall" each appear 2 times.
