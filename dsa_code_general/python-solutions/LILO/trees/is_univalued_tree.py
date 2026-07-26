# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        Input: The root of a binary tree

        Output: A boolean
            - True if tree is univalued
            - False otherwise

        Goal: here is to determine wether an entire tree isunivalued. i.e every node contains the same value.
        
        Edge cases: 
            - single node -> return True
            - empty node (None) -> return True because it doesn't violate the rule
            - if a node's value differs -> return False
            - all nodes have the same value -> return True

        Walkthrough:
        Example 1 - Consider this tree:
                1
               / \
              1   1
             / \   \
            1  1    1

        Start at the root -> the root's value is 1.

        Now  visit every other node.

        For each node, ask: "Is your value also 1?"

        - Left child -> Yes
        - Left.left -> Yes
        - Left.right -> Yes
        - Right child -> Yes
        - right.right -> Yes

        Everyone agrees, return True.

        Example 2 - Consider this tree:
                2
               / \
              2   2
             / 
            5

        Start at the root - the root's value is 2

        Now, visit every node and ask "Is your value also 2?"

        - Left child -> Yes
        - left.left -> No

        Immediately return False
        - - -
        Brute Force Approach:

        Intuition:
        The root's value is the value that every other node should have.

        So:
        1. Save the root's value
        2. Visit every node in the tree
        3. If any node has a different value, return False
        4. If you finish visiting every node without fnding a different value, return True

        Algorithm:
        1. Store the root's vale
        2. Create a recursive function
        3. If the current node is None, return True
        4. Compare the current Node's value with the roots value
        5. If they differ, return False
        6. Otherwie, recursively check the right subtree
        7. Return true only if both subtrees return true

        Pseudocode:
        if root is None:
            Return True

        target = root.value

        Define dfs(node):

            If node is None:
                Return True

            if node.value != target:
                Return False

            Return dfs(node.left) AND dfs(node.right)

        Return dfs(root)

        - - -
        Time complexity: O(n)

        Why? 
        - In the worst case scenario, we visit every node exactly once
        - Each visit performe only constant-time work (compare one value and make recursive call)

        So, if there are n nodes: 1 comparism * n nodes = O(n)

        Space complexity: O(h) where h is the height of the tree

        Why?
        - We are not creating extra data structures
        - The only extra memory comes from the recursion call stack
            - Balanced tree: h = log n, so space is OO(log n)
            - Skewed tree (like a linked list): h = n, so space is O(n)

        """
        target = root.val

        def dfs(node):
            if node is None:
                return True
            
            if node.val != target:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)