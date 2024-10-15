## Kth Ancestor
Susan likes to play with graphs and Tree data structure is one of her favorites. She has designed a problem and wants to know if anyone can solve it. She starts with Node 1 as the root and sometimes she adds or removes a leaf node. Your task is to figure out the $K$-th parent of a node at any instant.
If node $A$ is at $L$ distance away from the Root node and $B$ is at $L$ + $K$ distance away from the Root node and there is a path of $K$ length from $A$ to $B$, then we call A as the $K$-th parent of B.

### Input
The first line of the input contains $N$ the number of Nodes in the tree.
The second line of the input contains $Q$ the number of Queries.
$Q$ lines follow each containing a query.
* $0$ $Y$ $X$ : $X$ is added as a new leaf node whose parent is $Y$ . $X$ is not in the tree while $Y$ is in.
* $1$ $X$ : This tells that leaf node $X$ is removed from the tree. $X$ is a leaf in the tree.
* $2$ $X$ $K$ : In this query output the $K$-th parent of $X$ . $X$ is a node.


### Output
For each query of type 2 , output the $K$-th parent of $X$ . If the $K$-th parent doesn't exist, output 0 and if the node doesn't exist, output 0.

### Constraints
* $1 \le N \le 200000$
* $1 \le Q \le 200000$

### Example input
    20
    16
    0 1 5
    0 5 3
    0 5 7
    0 1 8
    0 8 9
    0 8 6
    0 5 15
    2 15 2
    1 3
    0 15 20
    0 20 13
    2 13 4
    2 13 3
    2 6 10
    2 11 1
    2 9 1

### Example output
    1
    1
    5
    0
    0
    8

### Explanation of the example
    0 1 5 -> 5 is added as a leaf node to 1.
    0 5 3 -> 3 is added as a leaf node to 5.
    0 5 7 -> 7 is added as a leaf node to 5.
    0 1 8 -> 8 is added as a leaf node to 1.
    0 8 9 -> 9 is added as a leaf node to 8.
    0 8 6 -> 6 is added as a leaf node to 8.
    0 5 15 -> 15 is added as a leaf node to 5.
    2 15 2 -> 2nd parent of 15 is 15->5->1 is 1.
    1 3 -> leaf node 3 is removed from the tree.
    0 15 20 -> 20 is added as a leaf node to 15.
    0 20 13 -> 13 is added as a leaf node to 20.
    2 13 4 -> 4th parent of 13 is 1.
    2 13 3 -> 3rd parent of 13 is 5.
    2 6 10 -> there is no 10th parent of 6 and hence 0.
    2 11 1 -> 11 is not a node in the tree, hence 0.
    2 9 1 -> 9's parent is 8.