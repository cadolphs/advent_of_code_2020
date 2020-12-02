This problem has a _straightforward_ solution using iterators.

Of course this sort of brute-force solution has runtime O(N^2) for the 
pair combinations and O(N^3) for the triplet combinations.

The question is: Can we do better, and how much better?

I can think of an O(N) solution for the pair combinations:
Put items from first list in a set,
Create a second set, put in "2020 - item" for item in first set.
Compute set intersection (should run in O(N) because sets and hashes for ints are super fast)
Pick item from that intersection set, then this item and 2020 - item are your pair!

Then this also suggests an O(N^2) solution for the triplets:
Iterate over the items.
For given item, see if there's a pair that sums to 2020 - item.

One should definitely do this if the input list was gigantic!

PS: If the number of items in the sum wasn't fixed, we'd be looking at the subset sum problem, 
which in its general case is NP hard. It would have a straightforward QUBO implementation to
run on a quantum annealer, but the resulting QUBO would be very dense and thus require 
lots of connections...
