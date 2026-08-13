# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Input: The root of a binary tree

                2
               / \
              1   3

        Output: return a bollean
            - True if the tree is a valid BST
            - False otherwise

        Goal: determine wether every node satisfiies the BST property
        - Every node in the left subtree is smaller than the current node
        - Every node in the right subtree is greater than the current node
        - This must be true for every node, not just the root

        Edge cases:
        - single node
            e.g    5
          
          output: return True
        
        - an empty tree
            e.g None

          output: return True
          
        - invalid bst deeper in the tree
                    5
                   / \
                  1   6
                     /
                    3
          
          output: return False because even though 3 < 6, it is still in the right subtree of 5 and so should be > 5

        Walkthrough:
        Example 1: 
        
                    5
                   / \
                  1   4
                     / \
                    3   6

        At first glance:
        - 1 < 5
        - 4 < 5 instead of greater, so this fails

        But say we have this:

                    5
                   / \
                  1   6
                     /
                    3

        notice 3 < 6 and that works, but if we only compare a node with its paret, we'd iincorrectly think this is fine.

        But 3 is inside the right subtree of 5, so it must also satisfy: 3 > 5 but it doesnt.

        Therefore the tree is not a BST.

        Key Insight:
        a node must satisfy all liits from its ancestors, not just its parent.

        e.g     8
               /
              3
               \
                7
        Here, 7 > 3 but because it's on the left subtree of 8, it must also satistfy 7 <. 8, which it does. So, this is a valid BST.

        The idea is that every recursive call carries a minimu and maximum value that the curret node is allowed to be in between.

        This is a DFS pre-order recursion where the parent tells each child:
        "This is the minimum and maximum values you're allowed to be."

        So, the order is:
        1. Visit the current node
        2. Validate it against its allowed range
        3. Pass updated ranges to the left and right children

        - - -
        Brute Force Approach
        Intution: For everye:
        - check wether all nodes in its left subtree are smaller
        - Check wethere all nodes in its right subtree are greater
        - Repeat the same process for the left and right subtrees

        This works, but it repeatedly scans subtrees

        Pseudocode:
        Function isValidBST(root):

            if root is None:
                return True

            if any value in the left subtree is >= root.value:
                return False

            if any value in the right subtree is >= root.value:
                return False

            Return isValisBST(root.left) AND isValiidBST(rooot.right)

        Time complexity: O(n^2) in the worst case (especially for a skewed tree) because may subtrees are scanned repeatedly.

        Space complexity: O(h) for the recursion stack where h is the height of the tree

        - - -
        Optimized Approach:
        Pattern:
        DFS pre-order with recursion
        Why? Because each paremt passes the minimu. and maximum bounds to its children before recursing.

        Intution:
        Instead of checking every subtree repeatedly:
        - Carry the valid range(low, high) as you traverse
        - Every node must satisfy: low < node.val < high

        if any node violates this, return False immediately

        Pseudocode:
        function isvalidBST(root):

            Define DFS(node, low, high):

                if node is None:
                    return True

                if node.value <= low OR node.value >= high:
                    return False

                return DFS(node.left, low, node.value) AND DFS(node.right, node.bvalue, high)

            Return DFS(root, -%, +%)

        Time complexity: O(n) because every node is visited exactly once.

        Space complexity: O(h)
        - h is the height of the tree (recursion stack)
        - balanced tree : O(log n)
        - skewed tree: O(n)

        Space complexity: 
        """
        def dfs(node, low, high):

            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("+inf"))
        