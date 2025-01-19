## Building
In the distant future, aboard the USS Enterprise, Captain Picard has given you an important mission. Some of the decks of the starship need to be repainted for maintenance. You must decide which decks should be painted red (`R`) and which should be painted white (`W`).
However, Starfleet Protocol states: Two red decks cannot be directly adjacent to each other.
Print all valid paint patterns in **alphabetical** order.

### Input
The input is a single integer: $N$, the number of adjacent rooms.

### Output
All possible colorings must be given, line by line, in alphabetical order.

### Constraints
* $1 \le N \le 25$

### Example input
    3

### Example output
    RWR
    RWW
    WRW
    WWR
    WWW

### Explanation of the example
We should list all possibilities in alphabetical order.
