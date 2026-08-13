                    A
                   / \  \     # A points to D
                  B   C  D    # D points to F and F points to C
                     / \ |
                    E   F

start = A
result = [A B C D E F]
visited = {A, B, C, D, E, F}

Steps:
1. Start at some node (A)
    a. Add it to our result
2. Add the node to the queue
3. Check which nodes we can visit from the current node that we're at
    a. Nodes we can visit: B, C, D
4. Choose a new node
    a. We chose node B
    b. add it to our result
5. Repeat steps 2 - 4 until we hit a dead end
    a. if we hit a dead end:
        i. dead end
            1. if a node has no neighbours
            2. if a node only has neighbors that have all been visited
        ii. pop from our stack
        iii. repeat steps 3-4


Edge caes:
- There are no neighbors at the node we visited
    - Take a step back, turn around and check the other places
- The only node we can visit has already been visited
    - Take a step back, explore other parts