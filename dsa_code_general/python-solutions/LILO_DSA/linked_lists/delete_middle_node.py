# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        input : head of a linked list. Each node has:
            - node.val
            - node.next

        output: return a modified linked list after deleting the middle node

        goal: to return the new modified head (linked list)  afer deleting the given head (linked list)

        edge case:
        - The problem definition already assured me that the linked list cannot be empty i. e
        it's in the range of [1, 105].
        - It also assured me that each node value is between [1, 105) inclusive so no need to validate values.
        - But a list that contains one node should return None. Why? Because 
            n = 1; 1 // 2 = 0; then you delete 0 -> return None

        How do we find the middle number?

        middle number =  floor(n / 2)

        where n = number of nodes.

        Example: [1] -> [3] -> [4] -> [7] -> [1] -> [2] -> [6]
                  0      1      2      3      4      5      6

        n = 7

        middle number = 7 // 2 -> 3

        so, we delete the node at index position 3 -> deletes [7]

        modified or new linked list = [1] -> [3] -> [4] -> [1] -> [2] -> [6]

        Example walkthrough:

        Example 1:
        [1] -> [2] -> [3] -> [4]
         0      1      2      3

         n = 4

         middle number = 4 // 2 = 2

         deletes [3]

         modified linked list: [1] -> [2] -> [4]

         brute force approach would be:
         1. traverse the linked list and count nodes
         2. find the middle number. i.e middle = n // 2
         3. traverse again until the node before middle
         4. remove the middle number

        But the cons is that we will be traversing twice.

        Optimized approach:
        Having two pointers:
            - slow: 1 step ahead
            - fast: 2 steps ahead

        When fast reaches the end, slow will be at the middle

        Example:  [1] -> [3] -> [4] -> [7] -> [1] -> [2] -> [6]
                    |
                   slow

                    |
                   fast

        slow moves one step, fast moves two steps

        Eventually:
         [1] -> [3] -> [4] -> [7] -> [1] -> [2] -> [6]
                               |
                              slow
        slow will be at the middle, and then we remove it.

        Pseudocode:
        if only one node:
            return None

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # remove the middle number
        prev.next = slow.next

        return head

        - - -
        Time complexity = O(n) because we traverse only once
        Space complexity = 0(1) because no extra data structure
        """
        # if there's only one node, remove it
        if head.next is None:
            return None

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle number
        prev.next = slow.next

        return head
