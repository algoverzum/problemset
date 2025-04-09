## Best Employee
In a galaxy not so far away, a renowned company, Galactical Technology Solutions Inc., decided to honor its most dedicated employee — the one who spent the longest time inside the corporate office without stepping out. This employee would be celebrated as the most loyal and hardworking individual in the company. To identify this star performer, the company recorded the arrival and departure times of its employees.

Your mission is to help the company uncover who this exceptional employee is. The data is reliable: no one left without entering first, no one entered twice without leaving, and the office was empty both before and after the recorded events. Additionally, the employee with the maximum time spent inside the building exists uniquely, so the maximum time can't be shared by two employees.

### Input
The first line of the input contains $N$—the number of events recorded.  
The next $N$ lines each describe an event with three space-separated integers:  
- The ID of the employee ($A_i$).  
- The type of event ($E_i$, where 0 means the employee left the building, and 1 means the employee entered the building).  
- The timestamp of the event ($T_i$).

### Output
Your task is to print two numbers separated by a space:  
- The ID of the employee who stayed inside the building the longest.  
- The length of this uninterrupted time period.

### Constraints
* $1 \le N \le 100\,000$
* $0 \le A_i \le 10^9$ for all $i = 1 \dots N$
* $0 \le T_i \le 10^9$ for all $i = 1 \dots N$
* Events are provided in chronological order (sorted by time).

### Example input
    8
    1 1 1
    2 1 2
    1 0 5
    3 1 7
    1 1 8
    2 0 8
    3 0 10
    1 0 11

### Example output
    2 6

### Explanation of the example
Employee 1 entered the office at timestamp 1 and left at timestamp 5, spending 4 units of time inside, then entered once more to spend 3 units of time inside between timestamp 8 and 11.  
Employee 2 entered at timestamp 2 and left at timestamp 8, spending 6 units of time inside.  
Employee 3 entered at timestamp 7 and left at timestamp 10, spending 3 units of time inside.  
