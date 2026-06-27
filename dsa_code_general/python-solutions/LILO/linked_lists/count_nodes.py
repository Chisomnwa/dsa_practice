class Solution:
    def count_nodes(self, values: list[int]) -> int:
        """
        input: a linked list

        output : return the number of nodes in the linked list

        goal: same thisng -> to return the number of nodes in a linked list. 
        Rerun 0 if linked list is empty.

        edge cases: empty linked list should return 0

        Walkthrough with examples:

        Example 1:
        head          tail
          |             |
          ▼             ▼ 
         [1] -> [2] -> [3] -> Null

        current = head

        count = 0

        is current None? no -> count = 1
        current = current.next

        head   tail
         |      |
         ▼      ▼ 
        [2] -> [3] -> Null

        count = 2

               tail
                 |
                 ▼ 
        head -> [3] -> Null

        count = 3

        current = Null , and counter stops

        Return 3

        Example 2:
        []

        current = head
        count = 0

        is current none? yes -> return 0

        Example 3:
               tail
                 |
                 ▼ 
        head -> [10] -> Null

        current = head
        count = 0

        is current none? no -> count = 1

        current = current.next

        current = null, counter stops
        
        return 1

        is this initial approach inefficient? 

        Possible wrong approach would be converting the linked list
        to an array and then return the count but that's not necessary .
        We already have the structure, we only need to walk through it once.

        Pseudocode will be:
        count = 0

        for each values in the the values:
            if length of lvalues is 0:
                return count
            else:
                increase count by 1
        return count
        """
        count = 0
        # TODO: Traverse values and count each node.
        for value in values:
            if len(values) == 0:
                return count
            else:
                count += 1
        return count
        