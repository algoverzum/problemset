## Space Signals
A space station receives signals from all over the universe. But, the machine used to receive the signals broke, and now it can't receive signals with frequencies lower than 500. Find out the number of received signals and their sources.

### Input
The first line of the input contains $N$ the number of signals:<br> 
Followed by $N$ signals. Each consists of 2 lines, the first line is a word that is the source of the signal. The second line is the frequency of the signal.

### Output
Print the number of received signals, then the sources of those signals are separated by spaces.

### Constraints
* $1 \le N \le 1000$
* $1 \le N \le 1000$
The words consist of lowercase letters of the English alphabet and are atmost 100 letters long.

### Example input
    6
    earth
    200
    mars
    100
    venus
    600
    jupiter
    500
    saturn
    200
    pluto
    800

### Example output
    3 venus jupiter pluto

### Explanation of the example
    earth
    200<500     can't receive
    mars
    100<500     can't receive
    venus  
    600>=500        received
    jupiter
    500>=500        received
    saturn
    200<500     can't receive
    pluto
    800>=500        received
