# Day 5
The description here is pretty long, but all in all it's just binary encoding 
of numbers! Just replace F/B with 1/0, and L/R with 1/0, then parse as binary.

This should be all available in the standard library.

So, we know we'll want a function that replaces F/B with 1/0, and then just 
translate that to an int.

Actually, we don't even need to split the string, duh! If the last 3 digits are for seat, then they range from 0 to 7, and multiplying row with 8 shifts row bits to the left by 3, 
so there's "space" for those bits...

So we just need to, in one pass, replace F and L with 0, B and R with 1, then turn that into an int.

Now we need to just check all the ids and see which one is missing.
