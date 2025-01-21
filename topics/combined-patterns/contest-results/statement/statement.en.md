## Contest Results
The Galactic Race Archive contains a huge database of the results of races across the galaxy. The latest results of the legendary "Nebulon Race" have just been digitalized, and the Galactic Explorers Association asked the development team to create a program that would help quickly retrieving the results of the race. Your task is to write a program that will tell you the place of the some given contestants in the race results. If a contestant does not appear in the result list, then print -1 instead of their place.

### Input
The first line of the input contains two integers: $N$ is the length of the race result list and $Q$ is the number of contestants to query.
The second line contains $N$ strings separated by a space, the result list of the race, i.e. the names of contestants listed in the order of their final rank in the race.
The third line contains $Q$ strings separated by a space, the names of the contestants for whom you need to tell their final rank in the race. Each string consists of lowercase letters of the English alphabet and is up to 100 characters long.

### Output
You have to print $Q$ numbers, the places of the contestants in the race results. If a contestant did not participate in the race, then print -1.

### Constraints
* $1 \le N, Q \le 100$
* Each string consists of lowercase letters of the English alphabet and is up to 100 characters long.


### Example input
    5 4
    nova odyssey phoenix voyager aurora
    nebula nova aurora phoenix

### Example output
    -1 1 5 3

### Explanation of the example
`nebula` not in the list, `nova` is in the first place, `aurora` is in the fifth place, and `phoenix` is in the third place.

