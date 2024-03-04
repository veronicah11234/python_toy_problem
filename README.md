# Title 
# Bricks Distribution Problem Solver

## Problem Description

Imagine you have a row of boxes, each containing a certain number of bricks. In a single move, you can take one brick from a box and move it to the adjacent box on either side. The goal is to distribute the bricks in such a way that each box ends up with exactly 10 bricks. This Python script provides a solution to find the minimum number of moves required for this distribution.

## Solution

The `solution` function in the `box.py` script tackles this problem. Given an array `A` representing the initial distribution of bricks, the function returns the minimum number of moves needed to achieve the goal. If it's not possible to have exactly 10 bricks in each box, the function returns -1.

## Examples

1. For `A = [7, 15, 10, 8]`, the function should return 7. The sequence of moves is:
   - Move three bricks from box number 1 to the box on the left: [10, 12, 10, 8];
   - Move two bricks from box number 1 to the box on the right: [10, 10, 12, 8];
   - Finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].

2. For `A = [11, 10, 8, 12, 8, 10, 11]`, the function should return 6. The sequence of moves is:
   - Move a brick from box number 0 to box number 2 (using two moves);
   - Move a brick from the last box two positions to the left (using two moves);
   - Move a brick from the middle box to each of its neighbors (another two moves).

3. For `A = [7, 14, 10]`, the function should return -1. It is not possible to end up with exactly 10 bricks in each box.

## Usage

To use the provided script, run it with a Python interpreter:
python3 box.py


## Dependencies
This script does not have any external dependencies. It runs on Python 3.

## License
This solution is released under the MIT License