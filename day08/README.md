# Day 8
Ah! Another one of those computers. Let's start with a simple but extensible design.

Some requirements:
- Instructions have _positions_, i.e., some sort of Sequence
- There's the accumulator.
- And of course the parsing again.
- Let's not overthink at fist.

So now there's the run method. What we want this to do is to execute the instruction under the cursor, 
and _stop_ if it sees the same position again!

So a bit of back and forth with the testing but I like the layout. Computer depends on instructions. They have 
"mutual" interfaces. An instruction can be executed and gets the computer as an argument. 

An instruction messes with the accumulator and the instruction pointer. We are using template methods here: 
The Instruction class just calls methods on itself to figure out how much to jump by and how much to increase the counter by.

Okay, I will finish later... Sounds like we need "debug" capabilities ;)

## Part 2
So we need to know whether we stopped via infinite loop or via normal exit. Let's refactor that to use exceptions.

Now if we run into an infinite loop we get an exception, and if the instruction goes "out of bounds" it just stops. Now that currently 
includes "not nice" out of bounds stops (e.g. jumping to -1000.) We can revisit that when we _have_ to.

How would we go about testing the debugger? We expect the Debugger class to take in a list of instructions, and then tries to find 
which instruction should switch from nop to jmp or vice versa to avoid an infinite loop.

Means we want to know if a program has an infinite loop. Okay, that's done.

Next up, we need to generate the candidate programs. Generator! Could be its own class type of thing but maybe just a generator expression. 
And we _test_ it like a class?

Okay, can generate candidates. Next up, debugger should find the program that terminates.