#!/usr/bin/env python3
import argparse
import os
import random

def generate_path(steps):
    path = ['0']
    for i in range(1, steps):
        if random.random() <= .35:
            path.append('1')
        else:
            path.append('0')
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', required=True, type=int, help='Number of rows')
    parser.add_argument('-c', required=True, type=int, help='Number of cols')
    parser.add_argument('-n', required=True, type=str, help='Name/path of output file')

    args = parser.parse_args()
    
    with open(args.n, 'w+') as f:
        f.write('{} {}\n'.format(args.r, args.c))
        for r in range(args.r):
            path = ' '.join(generate_path(args.c))+'\n' if r != args.r-1 else ' '.join(generate_path(args.c))
            f.write(path)
    

if __name__ == "__main__":
    main()