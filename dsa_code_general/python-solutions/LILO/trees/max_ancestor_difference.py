# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Input: The root of a binary tree

        Output: rteurn the largest absolute difference between any node and one of its ancestors.

        Goal: For every node, compare it only with the nodes above it on its path from the root. Find the largest difference.

        Edge cases:
        - Three with only two nodes
        e.g 5
             \
              8
        
        Output is 3

        - All nodes have the same value -> Output is 0

        - Maximum difference occurs deep in the tree ->  return that maximum

        Walkthrough

        Example 1:
             8
            / \
           3   10
          / \    \
         1   6    14
            / \   /
           4   7 13
        
        Start at root 8

        Now, imagine walking down the root to every leaf.

        Along each path, keep track of:
        - the smallest value you've seen
        - the largest value you've seen

        For example, on this path:
        8 -> 3 -> 1

        You've seen:
            minimum = 1
            maximum = 8

        The diffrence is 8 - 1 = 7

        Now, try another part: 8 -> 3 -> 6 -> 7

        Values seen:
            minimum = 3
            maximum = 8
            difference = 5

        Another part: 8 -> 10 -> 14 -> 13

        Values seen:
            minimum: 8
            maximum: 14
            difference = 6

        The answer is the largest ath found on any root-to-node path, which is : 7

        -  - -
        Brute Force Approach:

        Intution: For every node, wak back through all of its ancestors and compute:
        |ancestor.val - node.val|

        Kepp track of the largest difference found.

        The inefficiency is that the same ancestors are revisited many times.

        Algorithm:
        1. Traverse every node in the tree
        2. For each node, compare it with every ancestor on its path from the root
        3. Update the maximum difference
        4. Retrn the maximum

        Pseudocode:
        max_difference = 0

        Define dfs(node, ancestors):

            If node is None:
                Return

            For each ancestor in ancestors:
                Update max_diffrence

            Add node to ancestors

            dfs(node.left, ancestors)

            dfs(node.right, ancestors)

            Remove node from ancestors

        Call dfs(root, [])

        Return max_diffrence

        - - -

        Python implementation:
         max_diff = 0

        def dfs(node, ancestors):
            nonlocal max_diff

            if node is None:
                return

            for ancestor in ancestors:
                max_diff = max(max_diff, abs(node.val - ancestor.val))

            ancestors.append(node)

            dfs(node.left, ancestors)
            dfs(node.right, ancestors)

            ancestors.pop()

        dfs(root, [])

        return max_diff

        - - -
        Time complexity: O(n^2) in worst case

        Why? In a skewed tree:
        - Node 1 compares with 0 ancestors
        - Node 2 compares with 1 ancestor
        - Node 3 compares with 2 ancestors
        - ...
        - Node n compares with n-1 ancestors

        So: 0 + 1 + 2 + ... + (n-1) which is O(n^2)

        Space complexity: O(h) which is the height of the tree
         i.e the recursion stack and the ancestors list can each grow to the treee's height h.

        - - -
        Optimized Approach:
        Intuition: Instead of storing every ancestor, we only need to now:
        - the smallest value seen sofar
        - the largest value sen so far

        Why?

        Because the maximum diffrence with the current node wil always be against one of those two extremes.
        We don't care about the values in between.

        Why this works? Suppose the path is:
        8 -> 3 -> 6 -> 4

        Ancestors of 4 are: 8, 3, 6

        We don't need to comapare 4 with all three. 

        The maximum difference will always be with"
        - the smallest ancestor (3)
        - or the largest ancestor (8)

        Knowing only the minimum (3) and the maximum (8) is enough

        Algorithm:
        1. Strat at the root
        2. Keep track of the minimum and maximum values sen on the current path
        3. Update them at each node
        4. When reaching None, return the difference between the current maximum and minimum
        5. Return the larger result from the left and right subtrees

        Pseudocode:
        Define dfs(node, current_min, current_max):

            If node is None:
                Return current_max - current_min

            Update current_min

            Update curent_max

            Return the larger of:

                dfs(left child)

                dfs(right child)

        Start with the root: dfs(root, root.value, root.value)

        - - -
        Time complexity: O(n) because every node is vsited exactly once
        At each node, we only do constant-time operations:
            - one min()
            - one max()
            - recursive calls
        
        So, the total call grows linearly with the number of nodes.

        Space complexity: O(h) where h is the height of the tree.
            - Balanced tre -> O(log n)
            -Skewed tree -> O(n)
        """
        def dfs(node, current_min, current_max):
            if node is None:
                return current_max - current_min

            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)

            return max(
                dfs(node.left, current_min, current_max),
                dfs(node.right, current_min, current_max)
            )

        return dfs(root, root.val, root.val)
       