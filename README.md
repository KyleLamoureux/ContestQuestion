# Contest Question
Was interested in writting a question for the CSSA programming contest and they were cool with it

## Problem Description: Path Traversal

You are present with no more than **10^3** individual paths(rows) ranging in length(columns) of no more than **10^3**. Your task is to either find the shortest number of steps to traverse a single path(row) **or** find the deepest possible traversal index if there is no way to traverse **any** of the paths(rows).

You start at index **0** and then you can move with two different traversal options available to you. You can either jump **2** indexs or your can jump **1** index. **0's** represent locations you can step on. **1's** represent locations you can't step on. Lets look at an example for this to make sense

### Input Example 1
```
2 6
0 0 0 1 0 0
0 0 1 0 0 1
```
`output: 3`

Index **0** will be 0 100% of the time so we start there for all rows. Finding either the shortest path to the end of the array **or** the deepest index for row 1. In row 1 we can jump 2 indexs so we go to index **2**. Then we can jump another two indexs so we go to index **4**. Then we can go to the end by jumping 1 index so we are at index **5**. We made it to the end in 3 steps for row 1. In row 2 we can't get to the end can get as close as index **4**. But since 1 path had a solution the output solution is **3**

### Input Example 2
```
3 7
0 0 0 0 1 0 1
0 0 1 0 0 1 1
0 1 1 0 0 0 1
```
`output: 5`

In this example we attempt to calculate the shortest path to the end of each row. None of them have a solution though so we print out 5 as the solution. This is because it was the deepest index we could traverse to.



### Run the comparison file with:
- `source run_commands.txt` > sanity check
- Should be changed to a shell script loop but its 2:25am
- No output means successful run
- `~15s` per comparison run
