## Contest Results
The Galactic Race Archive contains a huge database of the results of races across the galaxy. The latest results of the legendary "Nebulon Race" have just been digitised, and the Galactic Explorers Association asked the development team to create a program that would help you quickly retrieve the results of the race. Your task is to write a program that will tell you the position of the racers in the archive. If the archive does not contain any, then print -1.

### Input
The first line of the input contains two integers: $N$ is the length of the database and $M$ is the number of questions.
The second line is $N$ string separated by a space. Each string consists of lower case letters of the English alphabet and is up to 1000 characters long
The third line is $M$ string separated by a space. Each string consists of lower case letters of the English alphabet and is up to 1000 characters long

### Output
You have to print $M$ numbers, if the word is in the database, then the index of it. if not, then -1.

### Constraints
* $1 \le N \le 1000$
* $1 \le M \le 1000$


### Example input
    5 4
    nova odyssey phoenix voyager aurora
    nebula nova aurora phoenix

### Example output
    -1 1 5 3

### Explanation of the example
nebula not in the database
nova is in first place
aurora is in fifth place
phoenix is in third place

