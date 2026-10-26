# Task I – The King's Watchtowers (Python)

On the border of the Kingdom of Numbers stand $N$ watchtowers. The king wants to station a guard in every tower, but certain towers cannot be guarded at the same time because their signal fires would interfere with each other.

A *guard assignment* is a subset of the towers in which no forbidden pair of towers appears together.

Your task is to generate all possible guard assignments.

## Input

The first line contains two integers: $N$ and $M$, where

- $N$ is the number of watchtowers,

- $M$ is the number of forbidden tower pairs.

Each of the following $M$ lines contains two integers: $a$ and $b$, meaning that towers numbered $a$ and $b$ cannot be guarded at the same time.

**Constraints**

- $1 \le N \le 20$

- $0 \le M \le 100$

## Output

First line:

The number of valid guard assignments.

Then each guard assignment must be printed on a separate line.

The tower numbers in each line must appear in increasing order.

The empty guard assignment (an empty line) must be printed first. The non-empty guard assignments must then be displayed in lexicographic order.

## Example

### Input

``` text
4 2
1 2
2 3