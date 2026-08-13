class Solution:
    def choose_structure(self, operation: str) -> str:
        # Return one of: "Array" or "Linked List"
        """
        input: an operation which is a string
        
        output:
        - Array if the operation is "fast index access" or "contiguous memory"
        - Linked List if the operation is "fast insertions" or "fast deletions" or "pointer rewiring"

        goal: is to choose which data structure match certain operations

        Pseudocode:

        if operation is fast index access or operation is contiguous memory:
            return "Array"
        else:
            return "Linked List"

        is the pseudocode approach efficient?

        Yes, it's efficient because it's a straightforward approach where I use an if-else statemnt with 
        conditional statemet to group the operations into two categories i.e the data structures that match.
        """
        if operation == "fast index access" or operation == "contiguous memory":
            return "Array"
        else:
            return "Linked List"
