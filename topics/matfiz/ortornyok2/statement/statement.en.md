# Task II – The King's Watchtowers (C++)

The king has reviewed all possible guard assignments and would like to choose one that places guards in as many towers as possible.

Your task is to find a guard assignment that:

- does not contain both towers of any forbidden pair;
- contains the largest possible number of towers.

If there are multiple maximum-size guard assignments, output the **lexicographically smallest** one.

When comparing two guard assignments, the one with the smaller tower number at the first position where they differ is considered lexicographically smaller. If one assignment is a prefix of the other, the shorter one is considered smaller.

## Input

The first line of standard input contains two integers, $N$ and $M$, where:

- $N$ is the number of watchtowers;
- $M$ is the number of forbidden pairs of towers.

Each of the next $M$ lines contains two integers, $a$ and $b$, indicating that towers $a$ and $b$ cannot both be guarded at the same time.

**Constraints**

- $1 \le N \le 25$
- $0 \le M \le 100$

## Output

On the first line, output the size of a maximum-size guard assignment.

On the second line, output the numbers of the selected towers in increasing order.

## Example

### Input

```text
6 5
1 2
1 4
2 3
3 6
5 6
```

### Output

```text
3
1 3 5
```

## Explanation

In this example, no valid guard assignment contains more than three towers. There are four valid assignments containing three towers: $\{1, 3, 5\}$, $\{2, 4, 5\}$, $\{2, 4, 6\}$, and $\{3, 4, 5\}$. Of these, $\{1, 3, 5\}$ is the lexicographically smallest, so it must be output.

## Hint 1

Again, use three vectors: `forbidden` to store the forbidden pairs (for each tower, a list of towers that conflict with it), and `current` and `best` to store the current and best selections of towers.

## Hint 2

Before selecting a new tower, check that it does not conflict with any previously selected tower.

## Hint 3

Apply **pruning**!

If the current partial solution contains $x$ towers, at most $r$ more towers can still be selected, and a solution of size $k$ has already been found, then whenever

$$x+r < k$$

this branch cannot produce a better solution and can be pruned.

## Hint 4

If

$$x+r = k,$$

the branch can still be pruned if even the best solution obtainable from it cannot be lexicographically smaller than the best solution already found. (This is an additional pruning option; the solution below only applies the pruning described in Hint 3 and continues searching in the case of equality.)

## Hint 5

It is useful to write a separate function for lexicographic comparison. For example:

```text
bool lexicographicallySmaller(const vector<int> &a,
                              const vector<int> &b) {
    return a < b;
}
```

The `<` operator for `vector` objects performs lexicographic comparison.
