from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Input:
            - head: reference to the first node of a singly linked list
            - n: integer representing the position from the end to remove.

        Example:

        head
         |
        [1] -> [2] -> [3] -> [4] -> [5] -> None

        n = 2

        Output: 
        [1] -> [2] -> [3] -> [5] -> None

        Output:
            - Return the head of the modified linked list

        Goal:
             - Remove the nth node from the end of the linked list
             - Return the remaining linked list
        
        Edge cases:
        1. Can the linked list be empty? 
            - No. Constraints says 1 <= sz <= 30

        2. Can n be greater than the size of the linked list?
            - No. Constraint says 1 <= n <= sz

        3. What if there's only one node?

        Input: [1]

        n = 1

        Remove the only node and return []

        --------------

        Brute force approach:

        Idea:
            - Since we need the nth node from the END,
            - first find the length of the linked list

        Steps:
        1. Traverse the linked list and store all the nodes in an array.

        Example: 
        [1] -> [2] -> [3] -> [4] -> [5]

        Array : 
        nodes = [node1, node2, node3, node4, node5]

        2. The index of the node we want to remove is: length - n

        Example: 
        length = 5
        n = 2

        index: 5 - 2 = 3

        Remove nodes[3]->  which is [4]

        3. Reconnect the linked list without that node

        [3].next = [5]

        leads to: [1] -> [2] -> [3] -> [5]

        --------------
        nodes = []

        # store all nodes
        current = head

        while current:
            nodes.append(current)
            current = current.next

        # find node before the one we remove
        index = len(nodes) - n

        # removing the head node
        if index == 0:
            return head.next

        # reconnect previous node to next node
        nodes[index - 1].next = nodes[index].next

        return head

        Time complexity: O(n) - because we traverse through the list once
        Space complexity: O(n) - because we create an extra data structure

        --------------
        Optimized Approach:

        Use two pointers:
        - fast
        - slow

        Idea:
            We create a gap of n nodes between fast and slow. Then when fast 
            reaches the end, slow will be right before the node we want to delete

        Example: 
        dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None

        n = 2

        Step 1: 

        Create dummy:

        dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
          |
         slow
          |
         fast

        Step 2:

        Move fast n + 1 steps. -> 2 + 1 = 3 (This will always depend on n given for each example)

        So, the means that the fast and slow pointer needs to be 3 nodes away.
        
        Why n + 1 steps? Because slow needs to stop before the target.

        We want: slow -> node_to_remove -> next_node

        So, 

        After moving: 

        dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
                                |
                              slow
                                              |
                                             fast
        
        [4] is the node we remove

        step 3: 

        Delete the node: slow.next = slow.next.next

        After, we'll have:

        dummy -> [1] -> [2] -> [3] -> [5] -> None

        Step 4:

        Return dummy.next

        Pseudocode:
        1. Create dummy node
        2. Connect dummy to head

        3. Create a slow and fast pointers
            slow = dummy
            fast = dummy

        4. Move fast n + 1 steps

        5. Move both pointers until fast reaches None
            slow = slow.next
            fast = fast.next

        6. Remove target node
            slow.next = slow.next.next

        7. Return dummy.next
        """

        dummy = istNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next