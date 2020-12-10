# Day 10
- Another "algorithmic" problem! 
- Am I naive or do we just sort them?
- This assumes that the input is valid... So what?
- Okay so we just sort, and then compute diffs, either with numpy.diff or just zipping the list with a shifted version.

## Part 2
Ah now it's getting fun. The puzzle hint tells us that a brute force approach will not work.
What would brute force even look like? We could construct a networkx graph: Each joltage gets a node, and we make 
edges to those with joltage +1, +2, +3. Then we count the number of distinct paths from source to end.

Of course we can be smarter! From 0 to end, how many ways are there?
- Well, from 0 we can go to 1, 2, or 3.
- Then recursively we can ask: How many ways are there from 1 to end? From 2 to end? From 3 to end?
- And of course we should "memoize" that. Or use dynamic programming.

- So we can use "dynamic programming" here. Initialize an array set to zero, whatever.
- Start at the largest final joltage. Set the array to "1" as the "recursion base".
- Now go down the list in reverse order:
- The value to get from i to the end is the sum of the values of getting from i+1, i+2, i+3 to the end.
- That's why defaulting the array to 0 is great!
- Since we skip joltages that aren't in the list, their value in the array remains 0.


