# Day 9
Okay, some sort of algorithmic problem. A brute-force solution is obvious: Grab the 
25 relevant numbers, compute the set of all pairs, see if the next number is in there, 
update the set of numbers contained.

One thing not super clear: "The two numbers in the sum must be different". So if my numbers 
are 1, ..., 25, then 50 doesn't work. But what if my numbers themselves contained "25" twice?

Maybe the longer example will bear that out.

This is about finding the right data structure and algorithm. Store current numbers that 
are under consideration in vector of size 25. Then build a matrix M so that 

`M_ij = v[i] + v[j] if v[i] != v[j] else nan`

To _check_ if a new number is valid, see if it is contained in the matrix.

To drop the latest and add the newest, efficiently rebuild the matrix:
- Delete the first row and first column, as `v[0]` is being dropped.
- Add a row / column at the end with the sum of the new element with all the old elements.

Once we have that, we just need to initialize with the right preamble, then iterate over the 
remaining numbers from the input until we hit an invalid number.

And now for finding the contiguous set, this is a classical scanline algo, so should be able to 
do that in O(N). So how does the scanline work? Let's work it out here:

- There is an index for the start of the range and an index for the back of the end of the range.
- `start` starts at 0, `end` starts at 1.
- We keep track of the `sum` of the range.
- If the `sum` is smaller than our number, we increase the `end` index by 1 and update the `sum`.
- If the `sum` is larger than our number, now we know there's no way the number situated at `start` is part of 
  the solution range! Therefore, we bump it up by 1 and update the `sum`.
- So what next? If we are too small, we go back to bumping the `end` index.
- If we are too large, we have to go _back_ with the `end` index, because there's ranges we haven't tried yet!
- So we keep going _down_ with `end` until we're too small.
- If, while going _down_, we end up too small, we know that the current `start` didn't work. So we bump it up
  by 1. Now we _know_ that we'll be too small (as bumping up `start` takes numbers away), so we go back to "increase end" mode.
- If at any time we hit the number exactly, we're of course done.
- If at any time we would set start == end, we know the range doesn't work. We start with a new range start, start+1.


- Actually there's further simplifications. I think that "Decrease" case never happens:
    - Assume the correct range is `(L, R)`.
    - Assume the "current" left end is `l < L`.
    - Then the current right `r` will never move past R!
    - Because: If `l < L` then `sum(l...R) > sum(L, R) = number`.
    - That means at the very latest when we hit r = R will the condition "sum > number" occur
    - Now, if r can never move _past_ R, we never have to decrease r.
    - Instead, if we are too large, we increase l, and if we are too small, we increase r.