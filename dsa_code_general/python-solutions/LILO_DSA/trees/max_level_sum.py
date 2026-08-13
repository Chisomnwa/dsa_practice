# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Input: the root of a binary tree

        Output: return the 1-indexed level number whose nodes have the largest sum.
        If two leves have the same sum, return the smallest level number.

        Goal: Compute the sum of every level and return the level with the largest sum.

        Edge cases:
        - One node: -> return 1
        - All negative numbers: -> return 1 becuase it syas don't initialize the best sum to 0

        e.g    -1
               / \
              -2  -3

        Return Level 1

        - Tie: -> return the smaller level
        e.g 
            Level 1 sum = 5
            Level 2 sum = 5

        Return Level 1

        Walkthrough:
                1
               / \
              7   0
             / \
            7  -8

        Process one leve at at a time 

        Level 1: sum = 1
        Level 2: sum = 7
        Level 3: sum = -1

        Solution(BFS)

        Intuition: Since the problem asks about levels, the natural choice is BFS(level-order traversal)

        A queue let's us process:
            Level 1
               |
            Level 2
               |
            Level 3

        For each level:
        1. Compute its sum
        2. Compare it with the best sum seen so far
        3. If it's larger, update the answer

        Algorithm:
        1. Put the root into a queue
        2. Start at level 1
        3. While the queue is not empty:
            - Process exactly the curent level
            - Compute its sum
            - Update the best level if needed
            - Add all the children to the queue
        4. Return the best level

        Pseudocode:

        Create a queue containing the root

        best_sum = root.value
        best_level = 1
        current_level = 1

        While queue is not empty:

            level_sum = 0

            Repeat for every node currently in the queue:

                Remove a node

                Add its value to level_sum

                Add its left child if it exists

                Add the right child ifit exiss

            If level_sum > best_sum:

                Update best_sum

                Update best_level

            Move to the next level

        Return best_level
        """
        queue = deque([root])

        best_sum = root.val
        best_level = 1
        current_level = 1

        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > best_sum:
                best_sum = level_sum
                best_level = current_level

            current_level += 1

        return best_level
