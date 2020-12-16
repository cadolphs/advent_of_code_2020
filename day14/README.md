# Day 14
More funky programming. Okay, mainly we need to parse the actions, and then 
process them. We can ignore the parsing for now and focus on the "computer" 
part. 

Should be a "wrapper" around some sort of array. And we'll do some bit magic.

So the memory is done. Just a simple wrapper around a dict, making sure that 
we conserve memory by only explicitly storing the nonzeros.

Now for the bit mask. Could make that its own class! Make bit mask from string 
and apply it to an integer?