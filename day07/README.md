# Day 07
Okay, so two big parts: Parsing the input, and solving the problem.

Let's tackle the parsing first. For each rule, we have the outer bag and the inner bags with their counts.

Start with a simple datastructure or tuple for this.

`light red bags contain 1 bright white bag, 2 muted yellow bags.`

Note the handling of plural... So each row has the format

`{color} bags contain {num} {color} bag(s), {num} {color} bag(s).`

Let us build the grammer from the ground.

Start with simplest case: Bag containing one bag of one color. And I guess I want to already know what sort of datastructure to use
for data access?

Parsing should be simple! 


