# Day 16
Let' see. Need to read in the rules, my ticket, and the other tickets.

What's our data structure? Reading input will produce a tuple of rules, 
my ticket, and nearby tickets.

For a rule, we'll have a name and two ranges. Need to check if an entry is valid.

Anyway. That parrt was easy enough. Next step, based on only valid tickets, 
find which rule corresponds to which "column" in a ticket.

Some thoughts that would work? This is an interesting constraint problem.

Mathematically: Find labeling of columns to rules such that there is exactly 
one column per rule and such that all the values in one column are valid for 
that rule, for each rule.

That's a satisfiability criterion so we need a heuristic. Might be enough 
with constraint propagation without search?

Idea: Start with mapping or so? For each rule (by index) find the list of 
columns for which it is a candidate.

