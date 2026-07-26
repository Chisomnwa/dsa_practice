# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: int, k: int) -> List[int]:
        """
        Input:
            - root: the root of a binary tree'
            - target: a node in the tree
            - k: a non-negative integer

        Output: Return all the node values that are exactly k edges away from the target node.
        The order doesn't matter.

        Goal: Starting from the target node, find every node that is exactly k edges away.
        Unlike the previous tree problems, you may need to move :
        - down to children
        - up to parent

        Edge cases:
        - One node, k = 0
            output : [1] because target is 0 edges away from itself

        - One node, k > 0
            output: [] because there are no other nodes

        - K is larger than the tree's height:
            output: []

        - target is a leaf ; you may have to move up before finding nodes

        - - -

        Walkthrough:
        Example:
             3
            / \
           5   1
          / \ / \
         6  2 0  8
           / \
          7   4

        Target = 5, k = 2

        Think of yourself standing on node 5

        Distance 0: 5
        Distance 1: 6, 2, 3
        distance 2: 7, 4, 1

        No distance required to move again. So from:
        - from 2: we get 7, 4
        - from 3: we get 1
        
        So, we return [7, 4, 1]

        Notice: in Distance 1, we moved up to 3, trees don't normally let you move upward

        My though process:
        A binary tree only has child pointers. Since I also need to move upwars, I'll first build
        parent pointers. After that, I can treat the tree like an undirected graph and perform a 
        BFS from the target.

        This problem combines two patterns:
        1. DFS -> Build a parent map
        2. BFS -> Starting from the target, find all nodes exactly k edges way

        Think of it as:

        Tree
         |
        Convert into a graph (by remembering each node's parent)
         |
        Run BFS from the target node

             3
            / \
           5   1
          / \ / \
         6  2 0  8
           / \
          7   4

        So, still lookig at the tree. To build the parent map:
        7, 4 -> parent is 2
        1 -> parent is 3

        Now, every node knows:
        - left child
        - right child
        - parent

        This effectively turns the tree into an undirected graph.

        Then, we perform a BFS starting from the target node.

        when we have moved exactly k levels in the BFS, every node currently in the queue is an answer.

        - - -

        Pseudocode:
        Create an empty dictionary parent

        Define dfs(node, parent_node):

            If node is None:
                Return

            parent[node] = parent_node

            dfs(node.left, node)

            dfs(node.right, node)

        Call dfs(root, None)

        Create a queue containing only target

        Create a visited set containing target

        distance = 0

        While queue is not empty:
            If distance == k:
                Return the values of every node in the queue

            Process every node currently in the queue:

                Remove one node

                Look at:
                    left child
                    right child
                    parent

                For each neighbour:

                    If it exists and hasn't been visited:

                        Mark visited
                        
                        Add to queue

            distance += 1

        return []

        - - - 
        Time complexity: O(n) because DFS visists every node once, and BFS also visits each node at most once.
        Space complexity: O(n) because the parent map, and queue can all grow to at most n nodes
        """
         # Build a map: child -> parent
        parent = {}

        def build_parent(node, parent_node):
            if node is None:
                return

            parent[node] = parent_node

            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root, None)

        # Find the target TreeNode from its value
        def find(node):
            if node is None:
                return None

            if node.val == target:
                return node

            left = find(node.left)
            if left:
                return left

            return find(node.right)

        target_node = find(root)

        # BFS from the target node
        queue = deque([target_node])
        visited = {target_node}
        distance = 0

        while queue:

            if distance == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor is not None and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            distance += 1

        return []
