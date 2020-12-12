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

Now we create views, apply the rules, and all is good! Just a bit of testing to get the array indices just right.

To find the stable position, we just repeatedly call "step" until that doesn't change anything. 

## Part 2
Oh, now it's getting messy and I don't think I can use the numpy view trick to quickly produce the global update. 

First step: We can reuse most of the "old" class. I create a new "abstract" base class to capture all the stuff that stays the same.
Then child classes only need to implement the "step" function.

Now how about that step function? Brute force, or something smarter? 
E.g. find where all the seats are, initially their "value" to 0.

Then what? I can save minimally by not bothering with certain direction if I do pair updates!

L....L

first seat, check "to the right" -> hit second seat. Well, now that seat's "left" doesn't need to be checked any more!

Probably not worth the effort.

So, after doing all this, running the whole loop took actually quite some time. That's because I'm iterating over all seats 
and all the directions / steps all the time. You can obviously speed these up. Minor improvements:
- Based on the rules, if we start from an empty seat, as soon as any one direction finds an occupied seat, it's game over.
- Based on the rules, if we have seen 4 empty seats, we can stop as then we can't get to 5 occupied seats.

So a quick refactor then. Use the `all` function which lazily evaluates, and stops as soon as one is false. That speeds up the 
"empty -> occupied" rule. That should give a huge boost! Indeed, took runtime from 20 to 13 secs.

Then we can count how many occupied versus non occupied we've seen. If we hit 5 occupied, we abort and make the seat empty. If we hit 
4 unoccupied, we abort and make leave the seat occupied. This has a much lower impact though as it introduces extra steps to keep track of stuff.


