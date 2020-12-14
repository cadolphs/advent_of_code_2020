# Day 13
For part 1, I think this just is simple modular logic? Yup.

## Part 2
Now this sounds like more complicated modular arithmetic. Let's see.

Find t such that:
t mod id[i] == i for all i.

Well maybe go iteratively? We know that t mod id[0] == 0, so t must be a multiple of id[0].
t mod id[1] == 1 means t = (n * id[1]) + 1.

n * id[1] + 1 = m * id[0]

Some googling on math. 
Turns out this is a direct application of the Chinese Remainder theorem!
Just got to work my way through the constructive proof.

Phew, so in the end it's not so dramatic, just needed to be careful about the sign of 
things. Just follow the Wikipedia article on the Chinese Remainder theorem for the constructive 
proof, and that has all the steps needed. 

PS: I think this is a great example to discuss the value (or lack thereof) of TDD for _algorithm_ 
development. Sitting down at the keyboard and thinking of test-first development of an 
algorithm that figures out how to find a time that makes the bus schedules line up as demanded 
seems like a daunting task, and basically would either lead you to a horifically ineffective 
brute-force algorithm (you can always just "count up" from 0 and stop once you find a number that works.
But _my_ solution turns out to be 775230782877242, which is on the order of 1e15. Or your tests would 
somehow have you re-invent the extended Euclidean algorithm...

Tests are still great and important, but here they're just meant to check that I didn't fudge up 
a minus sign somewhere or mixed up quotient versus remainder, or some such thing. The tests 
won't do me any good in _discovering_ the algorithm.