#!/usr/bin/env python3

def solve(r, c, paths):
    NO_SOLUTION = 100000
    
    shorest_path = -1
    path_costs = []

    for path in paths:
        stack = []
        index, steps = 0, 0

        stack.append((index, steps))
        while stack:
            index, steps = stack.pop()
            if index == c-1:
                break
            
            if index+1 <= c-1 and path[index+1] != 1:
                stack.append((index+1, steps+1))
            if index+2 <= c-1 and path[index+2] != 1:
                stack.append((index+2, steps+1))

        if index != c-1:
            path_costs.append((index, NO_SOLUTION))
        else:
            path_costs.append((index, steps))

    shorest_path = min(path_costs, key = lambda t: t[1])

    return shorest_path[1] if shorest_path[1] != NO_SOLUTION else max(path_costs, key=lambda t: t[0])[0]


def main():
    r, c = map(int, input().rstrip().split())
    
    paths = []
    for i in range(r):
        paths.append(list(map(int, input().rstrip().split())))

    print(solve(r, c, paths))


if __name__ == "__main__":
    main()