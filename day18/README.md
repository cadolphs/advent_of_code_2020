# Day 18
Ah, a calculator. Using fancy math so we can't just use python's eval or it's 
safer alternatives.

We could go all out and build a parser that generates an expression tree and 
all that.

Or we build a simple "state machine". That could be fun too.

Let's play with this a bit... 

So I got it working on some of the input, but not on all. Probably related to 
difficulties with the fact that, using a stack etc to compute these things, 
I really shouldn't be relying on the infix notation.

Two ways about it:
1. Just write code that can evaluate expressions with no parentheses.
2. Recursively eliminate all bracketed expressions from the inside out.
3. 