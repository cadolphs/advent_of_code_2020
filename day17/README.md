# Day 17
Good old Convay, this time in 3d.

I remember a talk from PyCon from a few years ago, along the lines of 
"Don't overuse classes". Python has some good batteries-included data structures 
and sometimes `dict` and `set` are all you need. The speaker gives an example of 
Conway's game of life, which you _could_ of course solve with a bunch of 
classes, representing the game, a cell, etc. 

But it's actually much easier to just treat it as a set and have simple 
update functions. So let's do that now here.