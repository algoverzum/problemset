## Grades in Yukka
The semester has just ended in Yukka, and the teacher wants to evaluate the students. We receive a list of students with their names and scores. The teacher wants to see the following statistics:

1. How many students failed (achieved less than 50 points).
2. Who achieved the highest and the lowest scores (name and score).
3. The scores of all students in ascending order.
4. The names of the students who passed (achieved at least 50 points). If everyone failed, print a hyphen after "Átmentek:". That is: "`Átmentek: -`"

Help the teacher calculate these values!

### Input
The first line of the input contains an integer: $N$: the number of students ($1 \le N \le 100$).

Each of the next $N$ lines contains two pieces of data: $name\ score$, where $name$ is a word consisting only of English letters, and $score$ is an integer ($0 \le score \le 100$).

### Output
Print lines in the following format:

    Megbuktak: X
    Legjobb: <name> (<score>)
    Legrosszabb: <name> (<score>)
    Rendezett pontok: p1 p2 p3 ... pn
    Átmentek: name1 name2 name3 ...

The first line should indicate how many students failed, the second line should indicate the best student and their score, the third line should indicate the worst student and their score, the fourth line should list all scores in ascending order, and the fifth line should list the names of the students who passed.

### Example Input
    5
    anna 60
    bela 45
    cili 90
    dani 50
    emil 30

### Example Output
    Megbuktak: 2
    Legjobb: cili (90)
    Legrosszabb: emil (30)
    Rendezett pontok: 30 45 50 60 90
    Átmentek: anna cili dani
