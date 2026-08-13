# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Input:
            - the root of a binary search tree
            - low: lower bound
            - high: upper bound

        Output: return the sum of values within the inclusive range [[low, high]]

        Goal: Visit the tree and add up every node whose value satisfies: 
            low <= node.value <= high

        Edge caes:
            - Only one node, and it's withn range -> return its value
            - Only one node, and it's out of range -> return 0
            - No nodes fall within range -> return 0
            - Every node falls within range -> return the sum of all nodes.

        Walkthrough:
        Example 1:
              10
             /  \
            5    15
           / \     \
          3   7     18
        
        Range:
        low = 7
        high = 15

        Visit the tree:
        - 10 in range -> sum = 10
        - 5 not in range
        - 3 not in range
        - 7 in range -> sum = 17
        - 15 in range -> sum = 32
        - 18 not in range

        Answer is 32

        Brute Force Appproach:
        - Ignore the fact that this is a BST.
        - Treat it like a normal binary tree
        - Visit every node, and if its value is within [[low, high]], add it to the sum

        Algorithm:
        1. If the node is None, return 0
        2. Recursively get the sum from left subtree
        3. Recursively get the sum from right subtree
        4. If the current Node is in range, add its value
        5. Return the total

        Pseudocode:
        Define dfs(node):

            If node is None:
                Return 0

            left_sum = dfs(node.left)

            right_sum = dfs(node.right)

            total = left_sum + right_sum

            if low <= node.value <= high:
                total += node.value

            Return total

        return dfs(root)

        Python Implementation:

        def dfs(node):

            if node is None:
                return 0

            left_sum = dfs(node.left)

            right_sum = dfs(node.right)

            total = left_sum + right_sum

            if low <= node.val <= high:
                total += node.val

            return total

        return dfs(root)

        - - -
        Time complexity: O(n) since every node is visited exactly once.

        Space complexity: O(h) which is the height of the tree (the recursive stack)

        - - -
        Optimized Approach:
        We recognize this as a binary search tree

        That means:
        - Everything in the left subtree is smaller than the current node
        - Everything in the right subtree is larger than the current node

        So when necessary, we can skip an entire subtree

        For example:

              10
             /  \
            5    15

        low = 7
        high = 15

        then:
        - 5 is less than low
        - every node in the left subtree is <= 5
        - therefore None of them can be in the range

        So, don't even visit the left subtree

        Similarly if node.val > high, skip the right subtree

        That is how BST property saves work

        Algorithm:
        1. if the node is None, return 0
        2. If node.val < low, recurse only into the right subtree
        3. If node.eval > high, recurse ony in the left tree
        4. Otherwise:
            - include the curret node
            - recurse left
            - recurse right

        Pseudocode
        Define dfs(node):
            if node is None:
                return 0

            if node.value < low:
                return dfs(node.right)

            if node.value > right:
                return dfs(node.left)

            return node.value + dfs(node.left) + dfs(node.right)

        return dfs(root)
        """
        def dfs(node):
            if node is None:
                return 0

            if node.val < low:
                return dfs(node.right)

            if node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
                