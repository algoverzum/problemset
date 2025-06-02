## Terraform Bids
The Ereus Colony is planning to build new terraforming stations on various planets and moons. To this end, the Colonial Council has announced a public bidding process for companies.

Each participating company submitted its name and an estimated cost of implementation. The Council wants to rank the offers in increasing order of cost. If multiple companies have the same cost, their names should be ordered in alphabetical order.

### Input
The first line of the input contains a single integer $N$ – the number of offers.  
Each of the following $N$ lines contains two values:  
a word of at most 10 characters $A_i$ – the name of the company,  
and a positive integer $B_i$ – the company's bid.


### Output
Print $N$ lines, each containing the name of one company.  
The companies must be listed in increasing order of their bid.  
If multiple companies have the same bid, they should be ordered alphabetically by name.


### Constraints
* $1 \le N \le 100\ 000$  
* $1 \le B_i \le 100\ 000$ for all $i=1 \dots N$
* $A_i$ for all $i=1 \dots N$ consists of lowercase English letters and has at most 10 characters



### Example input
    5
    oriontech 12000
    aerodyne 8000
    cosmotek 12000
    zenicorp 9000
    novastar 8000

### Example output
    aerodyne
    novastar
    zenicorp
    cosmotek
    oriontech

### Explanation of the example
Both `aerodyne` and `novastar` submitted bids of 8000. Since the letter `a` comes before `n` in the alphabet, `aerodyne` is placed first, followed by `novastar`.  
The company `zenicorp` comes third with a bid of 9000.  
Among the companies bidding 12000, `cosmotek` is ranked before `oriontech` because the letter `c` appears earlier in the alphabet than `o`.


