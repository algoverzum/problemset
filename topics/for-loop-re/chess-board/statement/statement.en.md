### Chess Board
I lost my boarding pass. It turns out that there were `X` and `Y` characters on it forming a square with a chessboard pattern. Can you help me print a new one?

### Input
A single line of the input contains an integer: $N$ - the length of the side of the chessboard.

### Output
$N$ lines must be printed. In each row, there should be exactly $N$ pieces of `X` or `Y` character such that the adjacent ones are different.
There should be `X` in the upper left corner, i.e. the first character of the first line should be `X`!

### Constraints
* $1 \le N \le 20$

### Example 1 input
    4

### Example 1 output
    XYXY
    YXYX
    XYXY
    YXYX

### Explanation of example 1
We need to draw a $4 \times 4$ chessboard.

### Example 2 input
    5

### Example 2 output
    XYXYX
    YXYXY
    XYXYX
    YXYXY
    XYXYX
