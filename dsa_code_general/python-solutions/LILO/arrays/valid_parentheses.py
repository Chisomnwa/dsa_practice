"""
Valid parentheses

Given a string 's' containing just the characeters '(',  ')', '{', '}', '[', ']', , 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open braclket of the same type

Example: 
Input: s = "()[]{}"
Output: True
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        input : a string containing bracket characters
        output: bool i.e if opening and closing brackets match correctly

        goal: check wether every bracket is closed by the same type, in the correct order,
            with no orphan closers or no letfover openers.

        edge cases:
            - empty string -> no brackets to mismatch, so it's valid (True)
            - odd-length string -> can never be perfectly paired (this is a cheap early check, not strictly required but saves work)
            - string that starts with a closing bracket - nothing open yet to match it -> False
            - string that ends with a leftover unclosed openers, e.g "(((" -> fALSE

        Walkthrough using a VALID example:

        s = "()[]{}"

        stack = []

        char '(' -> opener -> push -> stack = ['(']
        char ')' -> closer -> top of stack is '(' -> matches ')' -> pop -> stack = []
        char '[' -> opener -> push -> stack = ['[']
        char ']' -> closer -> top of stack is '[' -> matches ']' -> pop -> stack = []
        char '{' -> opener -> push -> stack = ['{']
        char '}' -> closer -> top of stack is '{' -> matches '}' -> pop -> stack = []

        end of string. stack is empty -> nothing left unclosed -> return true

        Walkthrough using an INVALID example (wrong order):
        s = "([)]"

        char '(' -> opener -> push -> stack = ['(']
        char '[' -> opener -> push -> stack = ['(', '[']
        char ')' -> closer -> top of the stack is '[' -> not ')' -> doesn't match -> return False

        Notice why this fails rule 2 (correct order): even though '(' exists somwhere in the stack,
        the bracket that must close next is whatever that was opened recently and that was '[' not '('.
        That's exactly why a stack (LIFO) is the right structure: it always hands you the most recent 
        unclosed opener first, which is the one any new closer is obligated to match.

        Pseudocode:

        # map each closer to the opener it must match
        mapping = {')': '(', ']': '[', '}': '{'}

        # create a stach to hold all brackets that we must match
        stack = []

        for char in s:
            if char is an opener (one of these '(', '[', '{')
                push car onto stack
            else:
                # char is a closer
                if stack is empty:
                    return False # orphan closer -> nothing to match it
                top = pop from stack
                if top != mapping[char]:
                    return False # wrong type or wrong order

        # if stack still has openers left, they were never closed
        return true if stack is empty else return false

        ---
        Why a dict (mapping) instead of multiple if/elif checks?
        Using mapping[char] gives O(1) lookup to find "what opener does this cloder need?".
        This helps us avoid writing seperate if-statemen per bracket type. It also makes it trivial 
        to extend to more bracket types later, with no new logic, just one more dict entry.

        Why check "if stack is empty" before popping?
        Popping from an empty stack would raise an error (or, if checked carelessly, silently breaks).
        This check catches an orphan closer early. e.g s = ")(" where a closer appears with nothing open yet.

        Why the final check "stack is empty" at the very end, not just inside the loop?
        The loop only catches MISMATCHES as they happen. It never catches the case where openeers are left
        dangling with no closer ever arriving. e.g s = "(()" - - the loop finiches with no mismatch found, 
        but the stack still holds an unclosed '('. That leftover is what rule 3 is really checking: every 
        OPENER must also eventually be closed, not just every closer needing an opener.

        Time complexity: O(n) - because we loop through the string exactly once, character by character.
            Every operqation under that loop is O(1)

        Space complexity: O(n) - a new data structure stack was created. it can grow as large as the input string
            in the worst case. The mapping dictionary is O(1) because it is fixed at three entries regardless of 
            input size, so it doesn't count towards growth.
        """
        # create a dict that shows what closers to openers they must match
        mapping = { ')': '(', ']': '[', '}': '{'}

        # create a stack to help us check if the brackets match
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                # stack must be a closer but check if stack is empty
                if stack == []:
                    return False         # if it's empty, we return false because it's an orphaned closer
                top = stack.pop()        # if it's not empty, we pop the element at the top to match
                if top != mapping[char]:
                    return False
        if stack == []:
            return True
        else:
            return False                 # helps us track dangling openers
        
sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
print(sol.isValid("(()"))
print(sol.isValid(""))