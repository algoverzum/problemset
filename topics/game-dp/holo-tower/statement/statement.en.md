## Holo Tower
On the Millennium Falcon, R2-D2 and C-3PO are playing a game of **Holo-Tower**, a futuristic tower-building challenge.

* R2-D2 always makes the first move.
* On each turn, a droid can place **4, 5, or 11 holo-cubes** on top of the tower (increasing its height by 4, 5, or 11 cubes).
* The droid who makes the tower exceed a height of **$N$ cubes loses** the game. Reaching exactly $N$ is allowed.

Both droids play with perfect logic — always making the best possible move.
Given the maximum allowed tower height $N$, determine who will win.

### Input
The first line contains an integer $T$, the number of games played.

The next $T$ lines each contain a single integer $N_i$ — the maximum allowed height for that game.

### Output
For each game, print in separate line:

* "R2-D2" if R2-D2 will win
* "C-3PO" if C-3PO will win

### Constraints
* $1 \le T \le 10$
* $1 \le N_i \le 10^5$ for each $i=1,\ldots,T$

### Example input
    5
    2
    5
    14
    20
    33

### Example output
    C-3PO
    R2-D2
    R2-D2
    R2-D2
    C-3PO

### Explanation of the example
For $N=2$ the first player will make the height bigger already.

For $N=5$ the first player can place 4 or 5 holo-cubes and winning the game.

For $N=14$: 

* R2-D2 places 5 holo-cubes (height = 5)
* C-3PO cannot place 11 cubes (would exceed 14), so places either 4 or 5
* If C-3PO places 4, height becomes 9, and R2-D2 can place 5 to reach 14 exactly and win
* If C-3PO places 5, height becomes 10, and R2-D2 can place 4 to reach 14 exactly and win
