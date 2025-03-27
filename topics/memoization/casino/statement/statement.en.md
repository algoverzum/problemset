## Casino
On a distant planet, the locals enjoy gambling, and their casinos are filled with slot machines. Each machine operates with a token. The locals think that the machines work randomly, but you have figured out their logic! If you insert a token with value `N`, the machine gives out three tokens: `N/2`, `N/3`, and `N/4`, with each value rounded down, ensuring the casinos always have the upper hand.

These tokens can also be exchanged for the planet's currency, called "Galactic Credits", at a rate of 1:1, but once converted, the currency cannot be used to purchase tokens again.

Your quest is to outsmart the casinos by calculating the maximum possible amount of Galactic Credits you can obtain from a token with value `N`.

### Input
The first line of the input contains $T$ - the number of test cases.
Each test case is a single line with a number $N$ - the initial value of your token.

### Output
For each test case, print a single number, the maximum amount of Galactic Credits you can obtain from the token.

### Constraints
* $1 \le T \le 100$
* $1 \le N \le 10^9$

### Example input
    2
    12
    2

### Example output
    13
    2

### Explanation of the Example
In the first test case, you can insert the token into a machine and receive three tokens: 6, 4, and 3. Then exchange the tokens and get $6+4+3=13$ Galactic Credits. 

In the second test case, if you insert the token into a machine, you will receive tokens with values 1, 0, and 0. From there, you cannot get more than 1 Galactic Credit, therefore you should exchange your original token for 2 Galactic Credits.