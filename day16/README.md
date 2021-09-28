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

So I did it quick and dirty, but that was fun and good enough. No overthinking.
YAGNI and KISS.

How does it work? We build a matrix. Rows are rules, columns are positions 
in the ticket. A 1 in a given position i, j means that all the values in 
ticket position j are valid for rule i. That's of course a necessary but not 
sufficient condition that a given field is associated with a given ticket 
position.

Then we just look at that matrix and see if there's ever either a row or a 
column that contains _exactly_ one entry that's 1, and all 0s otherwise. In that
case, we have either found a field that can only be associated with one 
position, or a position that has values that are valid only for one particular rule.

In either case, we know that the only way to find a valid correspondence of 
tickets and rules would be to associate them. So we add that to our list of 
"found" values.

Next, we go to that row/column and set _everything_ in that row and 
_everything_ in that column to 0, because of course if field i is associated 
with position j, no other fields can be associated with position j, and 
no other positions can be associated with field i. 

Then we loop over that whole idea until the matrix has only zeros left.

If we ever get stuck where we can't find such a row or column with only one 
1 in it, but haven't deleted _everything_ yet, we know that our simple 
algorithm wasn't enough. (Think of a sudoku where you eventually run out 
of "easy" moves of super-constrained fields). 

This didn't happen for my puzzle input so I assume it's simple enough. What 
we'd have to do then is to find instead the row or column with the least 
amount of 1s in it, and then _branch_ over the decision of which field and 
position to associated with each other: Let's say a row has 2 ones, and that's 
the best we can do. Then we recursively (or via an implementation by hand 
with a stack) first try the first of the ones. If we succeed after that, good.
If not, we try the next one. 