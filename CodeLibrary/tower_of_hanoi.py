from data_structures.stack_array import Stack

"""
Troy Brunette
Midterm
CS240

Tower of Hanoi is a famous puzzle that is a classic example of recursion.
The minimum number of moves to solve the puzzle is 2^n-1, where n is the number of disks
The rules:
1. One disk moves at a time
2. A disk can be moved to an empty rod or onto another stack
3. A disk cannot be placed on a disk that is smaller than it


To solve this with recursion
Base Case: 
If there is only one disk, move the disk from the source rod to the destination rod
Recursive Case:
If more than one disk
move the top n - 1 disks from the source rod to an auxilary rod
move the largest disk from the source rod to the destination
move the n - 1 disks from the auxiliary to the destination rod

The Recursive case continues until the base case applies and solving the puzzle.

Recursion helps solve this problem by breaking the problem down into smaller problems and recursively solving them.

This implementation uses a Stack data structure to represent the different rods 
and its push and pop methods are used to move the disks around.
"""



def move(start, end):
    disk = start[1].pop()
    end[1].push(disk)
    print(f"Disk {disk} moved from {start[0]} to {end[0]}.")


def move_disks(n, source, target, auxiliary):
    if n == 1:
        move(source, target)
    else:
        move_disks(n - 1, source, auxiliary, target)
        move(source, target)
        move_disks(n - 1, auxiliary, target, source)



# The Tower of Hanoi 
A = ('A', Stack())  # The starting rod
B = ('B', Stack())  # The aux rod
C = ('C', Stack())  # The Target rod
n = 3  # Number of Disks
for i in range(n, 0, -1):
   A[1].push(i)


move_disks(n, A, B, C)
"""Prints out 
Disk 1 moved from A to B.
Disk 2 moved from A to C.
Disk 1 moved from B to C.
Disk 3 moved from A to B.
Disk 1 moved from C to A.
Disk 2 moved from C to B.
Disk 1 moved from A to B."""
