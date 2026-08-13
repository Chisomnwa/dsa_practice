"""
Question 230 - Kth Smallest Element in a BST (Medium)

Given the root of a binary tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.

Example 1: root = [3,1,4,null,2], k = 1

        3
       / \
      1   4
       \
        2

Example 2: [5,3,6,2,4,null,null,1], k = 3

        5
       / \
      3   6
    /   \
   2     4
  /
 1

Constraints:
- The number of nodes in the tree is n
- 1 <= k <= 10^4
- 0 <= Node.val <= 10^4
"""

"""
Inputs: 
- a root of a Binary Search Tree
- k; an integer telling you which smaller value to find

We need to list the values in ascending order: 1, 2, 3, 4, 5, 6

The:
- 1st smallest = 1
- 2nd smallest = 2
- third smallest = 3

So, the abser is 3

Output: to retyrn the value that is equal the kth position

Goal: Traverse the tree and return the kth smallest value in the tree

Edge cases:
- Can the number of nodes be empty or Null? No because the constraints says: 1 <= k <= n <= 10^4
- k cannot be a number higher that the number of nodes

- - -
Brute Force Approach

Intuition:
Since we want the kth smallest value:
1. Visit every node
2. Put all values in a list
3. Sort the list
4. Return the (k - 1)th element because Python lists are 0-indexed.

This ignores BST property.

Algorithm:
1. Traverse the entire tree (DFS)
2. Store every node value in a list
Sort the list
4. Return values[k- 1]

Pseudocode:

Create an empty list

Define dfs(node):

    if node is None:
        Return

    Add node.value to values

    dfs(node.left)
    dfs(node.right)

Call dfs(root)

Sort values

Return values[k - 1]
- - -

Time complesity: O (n log n) because
    - DFS traversal: (On)
        - Visis every node excastly once
        - Append each value to the list once
    Sorting: O(n log n)
        - the list contains n values
        - Python's sort() uses Timsort which runs in O(n lon g) in the general case
    Accessing values[k - 1]: O(1)
        - List indexing is constant time

    Overall:
        O(n) + O(n log n) + O(1) = O(n log n)
        NB: The sorting stepdominates the traversal

Space complexity: O(n) because
    - values list: O(n)
    - Recursion stack: O(n)
        - h is the height of the tree
        - Balanced tree: O(log n)
        - Skewed tree: O(n)

    i.e O(n) + O(n) = O(n)



    - - - 

    Optimized Approach: Using the BST property
    
    Intuition: A BST has this property.

    Left Subtree < Node < Right subtree

    So an inorder traversal visits the node in ascending order

    Instead of:
    - collecting all values
    - sorting them
    - returning the kth value

    We simply count the nodes as we visit them. When the count reaches k, we've found the answer

    Algorithm:
    1. Initialize a counter
    2. Perform an inorder traversal
    3. Every time you visit a node;
        - Increment the counter
        - If the counter equals k, save the answer
    4. Return the answer

    Pseudocode:
    count = 0
    answer = None

    Define inorder(node):

        If node is None:
            Return

        inorder(node.left)

        count  count + 1

        if count == k:
        answer = node.value
        Return

        inorder(node.right)

    call inorder(root)

    Return answer

"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    #Brute Force Python implementation
    # def kthSmallest(self, root, k):

    #     values = []

    #     def dfs(node):
    #         if node is None:
    #             return
            
    #         values.append(node.val)

    #         dfs(node.left)
    #         dfs(node.right)

    #     dfs(root)

    #     values.sort()

    #     return values[k - 1]

    # Optimized Approach implementation
    def kthSmallest(self, root, k):
        count = 0
        answer = None

        def inorder(node):
            nonlocal count, answer
            if node is None:
                  return
             
            inorder(node.left)

            count = count + 1

            if count == k:
                 answer = node.value
                 return
            
            inorder(node.right)

        inorder(root)

        return answer
