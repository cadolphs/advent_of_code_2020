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

Okay, so for the parsing we try pyparsing again!

And now for figuring out the answer to the question. This should be a graph theoretical problem. Let us think about the algorithm. 

Consider graph G where the nodes are bags of a given color. A _directed_ edge goes from node u to node v if there is a rule in which 
bag associated with node u contains bag associated with node v.

In this sort of graph, then, we're interested in all the nodes from which we can reach the "shiny golden bag" node.

Alternatively, we could swap the edges around. Then we would _start_ at the shiny golden bag and ask: How many distinct nodes can I reach from 
there? I assume networkx has the tools to deal with that.

Indeed, it's the "descendants" algorithm for directed acyclic graphs. So part 1 is done.

Next up part2. So now we need the _edge data_ too.

Actually let us flip the edges around and use "ancestors" instead of "descendants". Might make part 2 easier.

Now the algorithm for counting "containing" bags. This has a reasonably simple recursive formulation. Let's just add some tests 
slowly, starting with an empty bag, then adding complexity. Helps make sure we get the base case right.

If input data was too big to work with recursion, we would have to build a Queue or Stack ourselves. Luckily we don't need that.


