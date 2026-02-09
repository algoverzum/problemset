## Herbivores

On planet Yukka, a survey was conducted about what each animal eats. It was observed that there are animals that eat only plants, but there are also those that eat other animals. Plants do not eat anything. Create a program that selects the animals that eat only plants!

### Input

The first line of the input contains an integer: $N$ &ndash; the number of pairs. The members of the pairs are separated by exactly one space. Their meaning: the first eats the second.

### Output

In the first line of the output, write the number of animals that eat only plants; in the following lines, write the names of these animals.

### Constraints

- $1 \le N \le 100$
- The names consist of lowercase English letters and are at most 10 characters long.

### Example Input

    7
    roka fogoly
    roka galamb
    fogoly foldigiliszta
    csiga uborka
    galamb csiga
    foldigiliszta falevel
    sargarigó mag

### Example Output

    3
    csiga
    foldigiliszta
    sargarigo

### Explanation of the example

The snail (`csiga`) only eats cucumber (`uborka`), which is a plant, since it does not appear in the first position of the pairs; similarly for the earthworm (`foldigiliszta`), which eats leaves (`falevel`), which is a plant, and the oriole (`sargarigó`), which eats seeds (`mag`). The fox (`roka`), the partridge (`fogoly`), and the pigeon (`galamb`) also eat things that appear at the beginning of pairs, meaning they eat animals.