# Day 12
Another one of these position manipulation tasks.

In an object oriented sense, the ship has a position and a 
direction. Executing a move causes things to happen.

Now in terms of doing it in a _super_ object oriented way, using 
"Instruction" classes for the moves etc might be overkill _because_ 
we don't expect a _ton_ of new moves to show up. What more than 
going in all four directions etc is there?

We can just test that our ship does the right thing for all sorts of moves.

Moving around is easy enough. 

Turning, how to do it "nicely"? Divide degrees by 90. That's the actual number 
of steps. Then consider the _sequence_. Right turns for now, go like this:
N -> E -> S -> W -> N -> ...

So I add a bit of lookup stuff and then we ask: Current directio, where in the array are we?
Let's say east, so index = 1.
Then we turn right by 1170 degrees. Well, that happens to be 13 * 90, so 13 steps right. 
1 + 13 = 14. Modulo 4 that's 2, so the new direction is "S".

Finally for the manhattan distance we just move a bit and check that it's right. Just 
for fun I'm using the hypothesis package here: I tell it to give me any two step numbers, 
and any set of directions picked from N/S, and E/W respectively. Then I can check that the resulting distance is correct.

Somewhat unnecessary here, but this package is great for honing in on unexpected edge cases.

## Part 2
Okay, so now there's an "extra feature" (waypoint) and thus the commands mean different things.

The forward and move are pretty easy. Same math / logic just different variables involved.

For turning, what's the easiest way? Maybe this: The waypoint vector is written in 
"East/North" format. We can use our existing rotation logic to turn that into 
a new pair of directions. For rotating left, that would mean "North/West".
So (10, 1) would mean (10 east, 1 north) and after rotation should be
(10 north 1 west), which reads (-1, 10.)

In fact, that behavior should probably go in the Vector class. And then we can 
refactor the "original" `turn` function, too: Turn dir-string, like "E", into 
a Vector(1,0) or so. Rotate it. Then look up the string for _that_.