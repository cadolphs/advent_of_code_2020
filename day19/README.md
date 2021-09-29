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
Probably cleaner to do the latter, but easier to start with the former.

Okay, part 1 done, now part 2 makes the grammar not _regular_ any more because
rule 11 now reads 42 31 | 42 11 31 so it's recursive. I think the so-called 
pumping lemma can show that this rule can't be dealt with by a regexp.

It should still be possible to build some sort of state machine that handles 
this, but we could simply deal with the loopy part manually _if_ the only 
non-regular rules are rule 8 and rule 11.

Now rule 8 just means: "Match 42 any number of times" but at least once.
Rule 11 means: "Match 42 exactly N times and then match 31 exactly N times".

So basically 42^n 42^m 31^m with n, m > 0.

Now, this is tricky _if_ rules 42 and 31 themselves have non-fixed lengths 
there can be ambiguity about when one rule ends and the other starts. However, 
if we check that 42 and 31 don't themselves contain loops, then the lengths 
are fixed (again that's just the special nature of our input, where the 
branches of the or are always the same length.)

That means then we can write a pedestrian rule checker:
Build regexp for rule 42.
Build regexp for rule 31.
Compute n and m from this, check n, m > 0.