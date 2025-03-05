## Word Lookup
Our brave astronauts have crash-landed on a strange planet. The grumpy aliens took their phones, but luckily, one astronaut kept a secret, a tiny dictionary! Now, they need your help to translate a message and convince the aliens they're friendly. Translate the message quickly before the aliens get angry and suspicious!

### Input
The first line tells you how many word pairs are in the astronauts' dictionary. Let's call this number $N$.
The next $N$ lines each show a pair of words: first, the English word, and then, after a space, the alien word. The lines are ordered alphabetically by the English words.
The following line tells you how many words are in the message the astronauts need to translate. Let's call this number $M$.
The next $M$ lines give you the English words from the message, one word per line.

Every English word in the message will be in the dictionary.

### Output
Print $M$ lines, each containing the alien translation of the corresponding English word from the message.

### Constraints
* $1 \le N \le 100\,000$
* $1 \le M \le 50\,000$
* Each word is made of lowercase letters of the English alphabet.
* Each word is between 1 and 10 letters long.

### Example input
    5
    are borp
    friend zortan
    hello aloha
    planet kryton
    we glorp
    3
    we
    are
    friend

### Example output
    glorp
    borp
    zortan

