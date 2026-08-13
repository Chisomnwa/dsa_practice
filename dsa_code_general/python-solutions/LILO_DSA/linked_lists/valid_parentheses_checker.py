"""
Question Content
This is a smaller version of the Valid Parentheses problem.

The string only contains ( and ). Complete is_balanced_parentheses so it returns True 
when every opening parenthesis has a matching closing parenthesis in the correct order.

Rules:
- Only handle ( and ).
- Return True if the parentheses are balanced.
- Return False if a closing parenthesis appears without a match.
"""


class Solution:
    def is_balanced_parentheses(self, s: str) -> bool:
        """
        input : a string containing bracket characters

        output: Bool -> if opening and closing brackets matched correctly.

        goal: check wether every bracket is closed by the same type, in the correct order,
            with no orphan closers or leftover openers.

        edge cases:
        - empty string: no brackets to mismatch, so it's valid (True)
        - odd-length string: can never be perfectly paired -> return False
        - string that starts with a closing bracket -> nothing to match -> return False
        - string that ends with a leftover unclosed openers e.g "(((" -> return False

        Walkthrough using a valid example:

        s = "(())"

        stack = []

        char "(" -> opener -> push to stack -> stack = ["("]
        char "(" -> opener -> push to stack -> stack = ["(", "("]
        char ")" -> closer -> top of stack "(" -> matches ")" -> pop -> stack = ["("]
        char ")" -> closer -> top of stack "(" -> matches ")" -> pop -> stack = []

        end of string -> stack is empty -> return true

        Walkthrough using an invalid example:

        s = [")("]

        stack = []

        char ")" -> closer -> top of stack -> empty -> no opener to match -> return false

        Pseudocode:

        # Map each opener to the closer it must macth
        mapping: {"(": ")"}

        # create a stack to hold to hold all openers that we must match\staxk = []

        loop through each character:
            check if character is an opener:
                if it is, append to stack
            else:
                # it means it's a closer, then we check if there's any opener in the stack
                check if stack is empty:
                    return false  # because it means no opener to match the orphan closer
                top = stack.pop()
                check if top elemnt matches the closer:
                    continue if they match
                else:
                    return false
        
        at the end return true if stack is empty (it means all matches has been made)
        """
        mapping = {"(" : ")"}

        stack = []
        # TODO: Use the stack to validate the parentheses.
        for char in s:
            if char in ["("]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if mapping[top] == char:
                    continue
                else:
                    return False
        return len(stack) == 0
