## Rolling Cigarette
The old man is a smoker of the traditional kind — the type who fills tobacco into small paper tubes. From each cigarette, a small leftover part (a butt) remains, always the same length.

The smoker bought $N$ ready-made cigarettes, each of the same length (length). From every cigarette, a $butt$ centimeters long piece remains.

After smoking all the cigarettes, he empties the remaining tobacco from the butts and rolls new cigarettes from it. He then smokes those as well.

Your task is to determine:

* how many cigarettes he smoked in total, and
* how many centimeters of tobacco remain at the very end.

### Input
The input contains three integers:

* The first line: $N$ – the number of cigarettes initially bought.
* The second line: $length$ – the length of each cigarette.
* The third line: $butt$ – the length of the remaining part (butt) after smoking one cigarette.

All three numbers are integers.

### Output
Print two integers separated by a space:  
the total number of cigarettes smoked, and the total remaining tobacco length (in centimeters) at the end.

### Constraints
* $1 \le N \le 100$
* $1 \le butt < length \le 20$

### Example input
    20
    12
    2

### Example output
    23 10

### Explanation of the example
After smoking 20 cigarettes, there are 20 butts of 2 cm each. That makes 40 cm of tobacco, which can be used to roll 3 full cigarettes, leaving 4 cm of leftover tobacco.

From those 3 new cigarettes, another 3 butts of 2 cm remain, making 10 cm of tobacco total at the end.

Thus, the old man smoked 23 cigarettes in total, with 10 cm of tobacco left over.
