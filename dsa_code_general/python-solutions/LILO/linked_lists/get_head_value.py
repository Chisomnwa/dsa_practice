class Solution:
    def get_head_value(self, values: list[int])-> int:
        # values represents a linked list from head to tail.
        # Return the value stored at the head node

        """
        input: a list representing a linked list (e.g,. [10, 20, 30])

        output: a sinle value (the first elemnt) or None

        goal: extract and return the head node's value

        edge cases:
            - empty list should return NOne
            - single element list e. [5] should retyurn [5]
        
        Walkthroufgh with an example:

        Example 1: 
        [10, 20, 30]
          ^
        index[0] = 10 -> returns 10

        Example 2:
        [5]
         ^
         index[0] = 5 -> return 5

        Example 3:
        [] -> empty list -> returns None

        is the brute-force approach inefficient?
        No. THere's only one possible approach here: check if the list is empty; 
        if not, return the first element. That's O(1) time (one direct access to
        index 0) and O(1) space (no extra data structure). No optimization needed.

        pseudocode:
        if list is empty:
            return None
        else:
            return first element of list (index 0)
        """
        if values == []:
            return None
        else:
            return values[0]

sol = Solution()

a_list = [10, 20, 30]
print(sol.get_head_value(a_list))