## Food Chain
We are on planet Zorgatron-7. We study living creatures and what they eat. Some eat plants. Some eat other animals. Some eat both.  

Each piece of data we found is a **feeding pair**: the first creature **eats** the second.  For example:  
- `nebbi slug` means **nebbi** eats **slug**.  
- `slug moss` means **slug** eats **moss** (a plant).  

We call every creature that **eats something** an **animal**. If a creature eats nothing, it is a plant.  

Some animals eat other animals. We call them **predators**. Your job is to find all the **predators**.

### Input
The first line contains a number $N$: the number of feeding pairs. The next $N$ lines each show one feeding pair: two words, separated by a space: the first word is the **eater** and the second word is the **food**.

### Output
In the first line, print the number of predators. Then, print the names of all predators, one per line. The names must be in **alphabetical order**. If there are no predators, just print `0`.

### Constraints
* $1 \le N \le 100$
* Each name contains only lowercase English letters, up to 10 characters long.

### Example input
    7
    drak puffin
    drak nebbi
    puffin grub
    slug moss
    nebbi slug
    grub root
    nebbi seed

### Example output
    3
    drak
    nebbi
    puffin

### Explanation
- **moss**, **root**, and **seed** are not eaten by anyone → they are **plants**.  
- **slug** eats **moss** → eats a plant → **animal**.  
- **grub** eats **root** → eats a plant → **animal**.  
- **puffin** eats **grub** → eats an animal → **predator**.  
- **nebbi** eats **slug** and **seed** → eats an animal → **predator**.  
- **drak** eats **puffin** and **nebbi** → both are animals → **predator**.

So the predators are:  
**nebbi**, **puffin**, **drak**.
