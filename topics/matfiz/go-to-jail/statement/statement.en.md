## Go To Jail
Tak performed the following action $N$ times: rolling **two** dice. The result of the $i$-th roll is $D_{i,1}$ and $D_{i,2}$ .

Check if doublets occurred at least three times in a row. Specifically, check if there exists at lease one $i$ such that $D_{i,1}=D_{i,2}$, $D_{i+1,1}=D_{i+1,2}$ and $D_{i+2,1}=D_{i+2,2}$ hold.

### Input
In the first line of the input, we are given the value of $N$, which is followed by $N$ lines. Each of these lines contains the results of two dice rolls, separated by a space. (In the $i$-th line, the two rolls are $D_{i,1}$ and $D_{i,2}$.)

### Output
Print **Yes** if doublets occurred at least three times in a row. Print **No** otherwise.

### Constraints
* $3 \le N \le 100$
* $1 \le D_{i,1}, D_{i,2} \le 6$
* All values in input are integers.

### Example input 1
    5
    1 2
    6 6
    4 4
    3 3
    3 2

### Example output 1
    Yes

### Explanation of the example 1
From the second roll to the fourth roll, three doublets occurred in a row.

### Example input 2
    5
    1 1
    2 2
    3 4
    5 5
    6 6

### Example output 2
    No

### Example input 3
    6
    1 1
    2 2
    3 3
    4 4
    5 5
    6 6

### Example output 3
    Yes
