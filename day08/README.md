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

Okay, I will finish later...