# Day 14
More funky programming. Okay, mainly we need to parse the actions, and then 
process them. We can ignore the parsing for now and focus on the "computer" 
part. 

Should be a "wrapper" around some sort of array. And we'll do some bit magic.

So the memory is done. Just a simple wrapper around a dict, making sure that 
we conserve memory by only explicitly storing the nonzeros.

Now for the bit mask. Could make that its own class! Make bit mask from string 
and apply it to an integer? Yeah. The trick, I believe, is to create _two_ 
integers from the bit mask:
- One integer whose binary representation is 1 wherever the bitmask is 1, and 0 otherwise
- One integer whose binary representation is 1 wherever the bitmask is 0, and 0 otherwise.

So with an int `ones` and and int `zeros`, we can then use bit-wise operators to apply the mask:

`number | ones` will set every bit to 1 that's 1 in `ones`, and leave all other bits unchanged
`number & ~zeros` will set every bit to 0 that's 0 in `zeros` and leave all other bits unchanged.

Now we can make a computer with some pure commands.
