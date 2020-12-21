# Day 15
Just need to keep track of stuff for this one... Implement as iterator

## Part 2
Given that N is so large, the question is: Can we "speed up" the computation? The _best_ case 
would of course be some explicit formula, but I doubt we can find that. Instead, I suspect that we 
might be able to find cycles: Although the actual turn counter steadily increases, what matters 
for the output is only the _differences_; so cycles can definitely exist.

Now, keeping track of all the differences is kinda expensive! Whatever we do needs to be fast!

Some thoughts:
What if we just keep track of the "sequence" we've seen so far? But how do we know we're "good"?

A zero means we have seen the preceding number for the first time; this can never be part of a 
cycle because next time 'round it won't be.

...

Okay, this took way too long, but I think there _is_ no cycles. The proof of this would probably 
be quite some fun bit of math. So it's really just about speeding things up.

## Speeding up
First, I noticed that I over-designed by using a Tracker class. We really don't need to track the 
last _and_ second-to-last time we saw a number, because the last time, at the time that we check!, will always 
be _just now_. So then we only need to track one number, so a class is overkill.

Let's take that class out, then, and measure speed again.

Okay, doing that already cuts everything in half. Cool!

Now we can do it even better by preallocating the array...

And finally, we can throw away all the class stuff and turn it into a single function that we then _compile_ 
with numba. That takes the time down from 50 seconds (the original very inefficient class version) to 0.6 seconds.
That's almost a factor 100.