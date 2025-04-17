## Droid Repair
At the Galactic Empire's droid repair facility, the ID numbers of the robots arriving there have been written down. They need to find out which robots have been sent in for repair more than once and recommend that they be scrapped.

### Input
The first line of the input is $N$, the number of IDs in the list.
The second line contains $N$ IDs, separated by spaces: $A_1, A_2, \ldots, A_{N}$. 

### Output
Print **-1** if all IDs in the list are different. Otherwise, print the **indices** of the first and second occurrences of the first repeated ID in one line. The indexing of the list starts from 1.

### Constraints
* $1 \le N \le 10^5$
* $-10^9 \le A_i \le 10^9$

### Example 1 input
    8
    -1 4 -3 1 7 4 7 4

### Example 1 output
    2 6

### Explanation of the example
Droids with IDs 4 and 7 have been repaired several times, but 4 is listed earlier at positions 2 and 6.

### Example 2 input
    8
    -1 4 -3 1 7 -4 8 9

### Example 2 output
    -1
