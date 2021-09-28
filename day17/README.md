# Day 17
Good old Convay, this time in 3d.

I remember a talk from PyCon from a few years ago, along the lines of 
"Don't overuse classes". Python has some good batteries-included data structures 
and sometimes `dict` and `set` are all you need. The speaker gives an example of 
Conway's game of life, which you _could_ of course solve with a bunch of 
classes, representing the game, a cell, etc. 

But it's actually much easier to just treat it as a set and have simple 
update functions. So let's do that now here.

Now for part 2, making the change is of course pretty straightforward, but 
can I make it in a way that doesn't break part 2? Optional dimensionality 
parameter or something? Yeah, just involves figuring out the right dimension 
and looping over things in the right way. 

Note: It's not required to center the frame after each step. That takes some 
time. But not crucial. More important, computing the neighbors etc I'm 
currently doing in a somewhat wasteful way. It allows for very expressive 
explanation of what I'm doing, but leaves a lot of room for optimization and 
being smart about what needs to be computed and when. Especially since I'm 
using pure Python loops and tuples instead of numpy arrays.