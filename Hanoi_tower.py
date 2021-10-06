# TASK:
#
# Please read: https://en.wikipedia.org/wiki/Tower_of_Hanoi

# disks stacked on one rod in order of decreasing size, the smallest at the top
towers = [ 
    [5, 4, 3, 2, 1],
    [],
    []
]

# The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
#
# 1. Only one disk may be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a disk that is smaller than it.

# please implement function to solve to puzzle

# TASK:
#
# Please read: https://en.wikipedia.org/wiki/Tower_of_Hanoi

# disks stacked on one rod in order of decreasing size, the smallest at the top
towers = [ 
    [5, 4, 3, 2, 1],
    [],
    []
]

# The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
#
# 1. Only one disk may be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a disk that is smaller than it.

# please implement function to solve to puzzle

def hanoi(n, source, auxillary, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, auxillary)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from auxillary to target
        hanoi(n - 1, auxillary, source, target)


hanoi(len(towers[0]),towers[0],towers[1],towers[2])

print(towers[0], towers[1], towers[2])