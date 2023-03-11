# minesweeper

A minesweeper simulator and solving algorithm written in python

The solver uses a few algorithms
1. Check for simple solutions:
  First, the solver will check for any obvious solutions such as a 1 with only 1 unknown neighbor, or a 4 with 3 unknown neighbors and 1 flagged neighbor. The algorithm will flag the other neighbors appropriately. It will also check for cases such as a 3 with 3 flagged neighbors, and test the other neighbors which are guaranteed to be safe. This algorithm will solve a good majority of a solvable board (depending on difficulty)

2. neighbor Intersection:
  By comparing the sets of possible bomb neighbors for spaces within a radius of 2 spaces away, you can see if there are any 2 spaces such that all the possible bomb   locations adjacent to one space are contained within the set of possible bomb locations of another set, and thus that second set can now guarantee that n bombs will be within that subset. If the leftover bombs is 0, or equal to the leftover unknown neighbors, then all the leftover unknown neighbors are guaranteed to be not bombs, or bombs accordingly. 

3. Guess randomly:
  If the other two algorithms cannot be applied, then guess randomly from the remaining unknown spaces. This can be improved by calculating some sort of probability for each of the unknown spaces depending on the neighboring spaces
