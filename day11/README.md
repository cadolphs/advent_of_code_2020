# Day 11
Okay this is a bit like Conway's "Game of Life". (Did I get the name right...?)

The most "annoying" part here will be checking the edge cases.

The logic here in general is:
`val_new[i] = get_new_val(i, neighbors_of[i])`

The question is: Could this be done efficiently with some numpy magic?

Probably! We pad everything with "floor". Then we create four _views_ into the array, one 
for each shift. Then we apply the conditions to these views.

So we model this as a numpy array. 0 means floor, 1 means seat, 2 means occupied.

A first step is to read a seating plan from file. Done that.

Now we create views, apply the rules, and all is good.



