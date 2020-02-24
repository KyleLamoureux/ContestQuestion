# Contest Question
Was interested in writting a question for the CSSA programming contest and they were cool with it

## Problem Description: Path Traversal

You are present with no more than **750** paths ranging in length of no more than **250** steps needed to travel down them. Your task is to either find the shortest number of steps to traverse the path **or** find the deepest possible traversal index if there is no way to traverse **any** of the paths.

You have two traversal options available to you. You can either take **2** steps or your can take **1** step. **0's** represent locations you can step on. **1's** represent locations you can't step on. Lets look at an example for this to make sense

### Input Example 1
```
2 6
0 0 0 1 0 0
0 0 1 0 0 1
```
`output: 3`

Index **0** will be 0 100% of the time so we start there. In row 1 we can take a two step so we go to index **2**. Then we can take another two step so we go to index **4**. Then we can go to the end with a one step index is **5**. We made it to the end in 3 steps for row 1. In row 2 we can't get to the end can get as close as index **4**. But since 1 path had a solution the output solution is **3**

### Input Example 2
```
3 7
0 0 0 0 1 0 1
0 0 1 0 0 1 1
0 1 1 0 0 0 1
```
`output: 5`

In this example we attempt to calculate the shortest path to the end for each row. None of them have a solution though so we print out 5 as the solution as it was the deepest index we could traverse to.

### Run the comparison file with:
- `source run_commands.txt` > sanity check
- Should be changed to a shell script loop but its 2:25am
- No output means successful run
- `~15s` per comparison run