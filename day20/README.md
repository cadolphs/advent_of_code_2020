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