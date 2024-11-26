## Space Signals
A space station receives signals from all over the universe. But, the machine used to receive the signals broke, now it can't receive signals with frequency lower than 500. Find out the number of received signals and their sources.

### Input
The first line of the input contains $N$ the number of signals:<br> 
Followed by $N$ signals. Each consisting of 2 lines, the first line is a word that is the source of the signal. And the second line the frequency of the signal.

### Output
Print the number of received signals, then the sources of those signals separated by spaces.

### Constraints
* $1 \le N \le 1000$
* $1 \le N \le 1000$
* $1 \le S.size() \le 100$
### Example input
    6
    Earth
    200
    Mars
    100
    Venus
    600
    Jupiter
    500
    Saturn
    200
    Pluto
    800

### Example output
    3 Venus Jupiter Pluto

### Explanation of the example
    Earth
    200<500     can't receive
    Mars
    100<500     can't receive
    Venus  
    600>=500        received
    Jupiter
    500>=500        received
    Saturn
    200<500     can't receive
    Pluto
    800>=500        received
