# Day 3
Let's see what features we need. Obviously we will need to read the map. 
That's easy enough as the format is straightforward.

Next, we need a _representation_ of the actual terrain. This whole idea that 
the tree map "repeats to the right" means that indexing on that coordinate is 
done "modulo" the width of the original map. Perfect for writing a class that 
wraps this logic around whatever internal data structure we use, so our code 
isn't littered with modulo operations!

Then it's just a matter of generating the positions to check and counting the 
trees we encounter.

First we write a utility class that's a RightCyclicalArray.

Next up, we want to parse the map, which is simple enough.

Finally, we want to generate positions. For that we can just write a generator.

The rest is just plugging things together correctly...

Of course in trying this run I mixed up the array directions; with numpy arrays 
the first index is commonly understood to be the "row" and the second index is the 
column; this problem uses the opposite order.