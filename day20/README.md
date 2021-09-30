# Day 20
So now we have some sort of geometrical puzzle. Constraint programming.

The problem _formulation_ is: For a set N^2 of images, assign position
(i, j) and orientation r to each image such that:
- Each image is assigned a unique position (i, j)
- 0 <= i,j <= N-1
- 0 <= r <= 3
- If two images are adjacent to each other, their corresponding borders line up

Now in _general_ this can be quite the hard problem based on how many 
simultaneous matches we have. In a real-world _puzzle_, for each side of a 
puzzle piece there's exactly one other piece that would fit. But in a more 
general situation there can be multiples.

If it's the "one match" situation, this is a simple search. If it's a 
multiple-match situation, I think we've got an NP-hard problem.

So I'll do some exploration first under the "only one match" assumption.

In that case, we can just grab _any_ puzzle piece, in the standard rotation 
and then go searching for tiles that fit there.

Alternatively we could build a graph where nodes are tuples (tile, side) and 
two nodes have an edge if those tile's sides fit together. Then we can see 
if there's nodes with only exactly one connection, and go from there.

So, created that graph, works beautifully. Instead of indexing by "orientation",
we index nodes by tile and _side_, like top, bottom, etc. And then we ask if 
two tiles match if they're rotated such that two given sides are adjacent to 
each other. That takes care of the inherent rotational symmetry:

For every solution you find, there's 3 more solution that you get by rotating 
the whole puzzle.

Argh, I forgot about the flipping. Mh. But running on my test data, it doesn't 
appear that I need the flipping to find that "only one possible edge". But that
might be wrong if some tiles would have multiple options. The problem is then 
that picking a flip means other flips won't work. Ah, but then I'd have to 
just delete it.

Anyway. Looking at flips. It might seem we have a lot to keep track of, because 
we can flip both along the x-axis and the y-axis. However, these aren't 
independent. You can replace a y-flip by doing an x-flip and rotating by 180 
degrees.

Now, what happens to a border when we flip and then try and align it? It just 
picks the reverse:
- If we flip by x, 
  - top and bottom stay where they are but get reversed
  - left and right stay in their shape but swap places; rotating by 180 gets them
    back to their original position, but reverses them
- Same logic when we flip by y. So there's really only one flip.

So for matching tiles, if both haven't been flipped, or both have been flipped, 
we can use the normal match. If one of them has been flipped, but not the other,
we must reverse one of the borders for the match check.

Great, so in our graph the nodes now also have the alignment label, i.e. whether 
the tile has been flipped. What's our algorithm for assembly now?

Again, the question is how well the puzzle input constrains which pieces go 
together and whether we'd have to do search and backtracking (or some other 
heuristic) or whether we can just greedily put pieces together.

Let's first assume that the puzzle input is benign and that if two tiles 
match along a given border and alignment, then they're _meant_ to match. 

Let's see then. Again we can try and grab a node of degree 1. That node 
represents a tile that has as a side and orientation for which there's exactly 
one other tile, side, and orientation such that those sides match. We somehow 
log that match and then delete the corresponding nodes.

But wait. For every node and edge we find that way, there'll be a node and 
edge with opposite alignment that we could have also picked. So we need to 
keep track of that or be aware of that.

So a bit more experimentation. The tile match graph has max degree 1 and min 
degree 1. Because sides that don't match anything don't even get added!

Now with that observation, part 1 actually becomes quite easy: The corner 
tiles are the ones where exactly two of the sides have degree one...

# Part 2
So now we _actually_ have to assemble the image; but thanks to the degree 
observation, that's not that hard. Don't want to program it right now but 
will describe the plan:

- Pick any of the four corner tiles.
- Put it in the top left corner and rotate it so it's correctly aligned, i.e.
  with its neighbors to the bottom and right. Pick "alignment 1" i.e. no flip.
- Follow the graph along the bottom edge to assemble until it's a no-go, then
  go to the right, start going up etc etc until we're done.

