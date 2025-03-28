## Most Frequent Name
The spaceport at Moseyslee is experiencing unusually high traffic. The Rebel Alliance has received a secret message from an undercover agent: the Empire is conducting covert operations at the port.

R2-D2 and C-3PO gain access to the station's arrival records - a long list of names of recently docked spaceships. If they can identify the ship that has appeared most often, it could be the key to solving the mystery.

### Input
The first line of the input is $N$, the number of names in the list.
This is followed by line $N$, the names of the spaceships.

### Output
In the first line, print the number of times the most common name on the list appears.
In the following rows, the names of all the most frequently used spaceships in alphabetical order (one per row).

### Constraints
* $1 \le N \le 10^5$
* all spacecraft names are in lower case English alphabet and up to 25
* different spaceship names are guaranteed to be different 

### Example input
    8
    naboostarfighter
    millenniumfalcon
    ghost
    naboostarfighter
    millenniumfalcon
    ghost
    naboostarfighter
    millenniumfalcon

### Example output
    3
    millenniumfalcon
    naboostarfighter

### Explanation of the example
Both naboostarfighter and millenniumfalcon are listed three times.
