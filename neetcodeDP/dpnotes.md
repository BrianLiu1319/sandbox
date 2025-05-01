# dynamic programming notes

# introduction
    
## What is dynamic programming and how can it be described?
    - DP is an algorithmic technique based on states
    - Basically brute force but better

    Given a list of N coins (V_1, V_2, ... V_N) and total sum S find the minimum number of coins of which is S (each coin is replaceable) 

## What does a "state" stand for
    state - a way to describe a situation or a sub solution for the problem

    for example :
        a smaller state than state i would be the solution for any sum j

        for finding a state i we need to find all smaller states j

        having found the minimum number of coins which sum up to i we can then easily find i+1
        
## How to find the state?
    for each coin j : V_j <= i look at minimum number of coins found for the i-V_j sum (we have found previously magically) let this be m. if m+1 is less than the minimum number of coins already found for current sum i then we write the new result for it.


    For example: 
    given coins with values 1,3,5
    and SUM S is set to be 11

    we mark that for 
    state 0 - we haven't found a solution for this one (value of ininity could be fine)

    then we can see that only coin 1 is less than or equal to the current sum

    for sum 1-V_1 = 0 we have a solution with 0 coins because we add one coin to this solution we will have a solution with 1 coin for sum1. This coin 1 plus the first coin will sum up to 2 and thus make a sum of 2 with only 2 coins. For sum 3 we now have 2 coins which can be analyzed -> 1 and 3. There exists a solution for sum 2 that we can take for sum 3, but since the best solution for sum 2 has 2 coins. The new solution for sum 3 will have 3 coins. The sum for which this coin needs to make to be added is 0 since we know sum 0 is made of 0 coins. Thus we can make a sum of 3 with only one coin and we see that 1 < 3 meaning we can update it and mark it as 1 coin. For sum 4 we get the solution of 2 coins and so on.


Set Min[i] = INT_INF

For i in SUM_ARRAY
MIN[0] = 0

For i = 1 to S:
For j = 0 to N- 1
    if V_j <= i and min[i-V_j] + 1 < Min[i]
        then min[i] = min[i-V_j] + 1


By tracking data about how we get to a certain sum from a previous one, we can find out what coins were used in building it

for ex at sum 11 we add the coin with value 1 to a sum of 10
to get 10 we got from 5 to 5 from 0.

so we use 1,5,5


