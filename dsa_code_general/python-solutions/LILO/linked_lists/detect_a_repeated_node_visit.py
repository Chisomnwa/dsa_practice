class Solution:
    def has_repeated_visit(self, visited_ids: list[str]) -> bool:
        """
        input: a list of strings made up of ids

        output: bool -> return true if an id appears twice in the list, else return false

        edge case:
        - an empty list should return false, because no repeated values

        Example walkthrough:

        Example 1:

        visited_ids: ["A, "B", "C", "B]
                       0   1    2    3

        - we define a set to store unique ids
        - loop through the list of ids, and check if each id exists in the set
        - if the id exists in it, we return true, else false

        seen = set()

        at index 0: "A
            check if "A" in seen -> not found, add to seen = ["A]

        at index 1: "B"
            check if "B" in seen -> not found, add to seen = ["A", "B"]

        at index 2: "C"
            check if "C" in seen -> not found, add to seen =["A", "B", "C"]
        
        at index 3: "B"
            check if "B" in seen -> found -> return True

        example 2:

        visited_ids: []

        Nothing in there to check, so no repeating ids -> return False

        Example 3:

        visited_ids = ["A", "B", "C"]

        at index 0: "A
            check if "A" in seen -> not found, add to seen = ["A]

        at index 1: "B"
            check if "B" in seen -> not found, add to seen = ["A", "B"]

        at index 2: "C"
            check if "C" in seen -> not found, add to seen =["A", "B", "C"]

        no other id to chek, so no repeating ids, return False

        Pseudocode:
        seen = set()

        for each value in visited_ids:
            if value in found in seen:
                return True
            else:
                add it to seen
        return False

        """
        seen = set()
        # TODO: Return True if an ID appears twice.
        for value in visited_ids:
            if value in seen:
                return True
            else:
                seen.add(value)
        return False
