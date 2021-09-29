# Day 19
This is a problem with a grammar, specified in something loosely resembling 
EBNF. So the language described by this grammar will be a regular expression.

Two thoughts come to mind about how to implement this. First, I could just 
parse the grammar rules and build a python-style regular expression, and then 
just use the matching capabilities of that.

Or I'd have to implement "by hand" the sort of state machine / finite automate 
that will match an input against a grammar. Which is basically what the 
regexp module will be doing behind the scenes anyway. 

I think parsing into regexp should be easiest.

Next question is, do I want to rely on recursion, or use my own stack?
Probably cleaner to do the latter.