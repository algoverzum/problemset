## Forest of Mirrors
In the Mirror Forest, two peoples live: the Alvanians and the Invanians. Although their languages seem almost completely identical at first glance, there is a strange rule: every Alvanian word is pronounced and written exactly in reverse in the Invanian language. For example, the Alvanian word `magic` appears as `cigam` among the Invanians.

However, translation is not always problem-free. Sometimes someone works carelessly. Ivan claims that he correctly translated the Alvanian word $s$ into the Invanian language, and the result was $t$.

Help determine whether he is right!

### Input
The first line contains the word $s$, the second line contains the word $t$.  
Both words consist of lowercase English letters, contain no spaces, are non-empty, and are at most 100 characters long.

### Output
Print `YES` if the word $t$ is indeed the reverse of $s$.  
Otherwise, print `NO`.

### Constraints
* $1 \le |s|, |t| \le 100$
* Both words consist of lowercase English letters.

### Example Input 1
    code
    edoc

### Example Output 1
    YES

### Example Input 2
    abb
    aba

### Example Output 2
    NO

### Example Input 3
    code
    code

### Example Output 3
    NO
