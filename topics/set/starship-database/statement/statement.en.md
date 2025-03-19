## Starship Database
The Starfleet has assigned you to manage a list of classified starship registry codes in the Starfleet Secure Database. Your mission is to handle incoming orders from Starfleet Command, which will be of the following three types:

* $1 x$ - Register a new starship with registry code $x$ in the Starfleet Secure Database. (If the starship is already in the database, ignore the command.)
* $2 x$ - Decommission a starship with registry code $x$ from the database. (If no such starship exists, ignore the command.)
* $3 x$ - Verify a starship's existence in the database. If registry code $x$ is found, respond with **1**; otherwise, respond with **0**.

Your job as captain is to execute these commands efficiently, ensuring the Starfleet database remains accurate and up to date. (In the beggining the database is empty, no ship is registered.)

### Input
The first line of the input contains $Q$, the number of queries. The next $Q$ lines contain 1 query each. Each query consists of two integers $t$ and $x$ where $t$ is the type of the query and $x$ is a ship registration number.

### Output
For queries of type 3 print **1** if the registration number $x$ is present in the database and if the registration number is not present, then print **0**.
Each query of type 3 should be printed in a new line.

### Constraints
* $1 \le Q \le 10^6$
* $1 \le y \le 3$
* $1 \le x \le 10^9$

### Example input
    10
    1 9
    1 6
    1 10
    1 4
    3 6
    3 14
    2 6
    3 6
    1 9
    2 6

### Example output
    1
    0
    0

### Explanation of the example
Ship 6 is in the database for the first qiery, but not in for the second time. Ship 14 was never registered in the database.
