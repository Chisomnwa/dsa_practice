"""
Longest Unique Substring Length
Video Title: Lecture 2.11 - Longest Substring: Sliding Window with a Set
Difficulty: Medium

Question Content
A sliding window can help us avoid regenerating every possible substring.

A set can help us quickly check whether the current window already contains a character.

Together, these ideas can solve the longest substring without repeating characters problem.

Task
Complete the function longest_unique_length.

The function receives one string called s.

Return the length of the longest substring that has no repeated characters.

Examples

Example 1
Input:
["abcabcbb"]

Expected Output:
3

Example 2
Input:
["bbbbb"]

Expected Output:
1

Hint:
Keep a left pointer, a right pointer, and a set of characters currently inside the window.

If the next character is already in the set, move the left side forward until it is safe to add the character.

Common Mistakes to Avoid:
- Clearing the whole set every time a duplicate appears
- Forgetting to update the maximum length
- Moving the left pointer only once when the duplicate is still inside the window

Why This Matters
This problem shows how hash sets combine with other patterns, like sliding window, to create efficient solutions.
"""


class Solution:
    def longest_unique_length(self, s: str) -> int:
        """
        Input: a string `s`

        Output: return the length of the longest substring with no repeating characters.

        Goal: Find the longest contiguous substring where every character is unique.

        Edge cases:
        - Empty string -? return 0
        - One charscter -> return 1
        - All characters are the same -> return 1
        - All characters are unique -> return len(s)

        Brute Force:

        Idea: Generate every substring.

        For each substring:
            - Check whether all characters are unique.
            - If yes, update the longest substring.

        Walkthrough:
        Example 1:
       
        s = "abc"

        Generate:
        "a"     ✔
        "ab".   ✔
        "abc"   ✔
        "b"     ✔
        "bc"    ✔  
        "c"     ✔

        Longest = 3

        Example 2:

        s = "abca"

        Generate:
        "a"      ✔
        "ab"     ✔
        "abc"    ✔
        "abca"   x
        "b"
        "bca"
        ...

        Longest = 3

        Pseudocode:

        longest = 0

        For every starting index:
            For every ending index:
                Generate the substring

                If the substring has no duplicates:
                    Update longest

        Return longest

        Brute Force Code:
        longest = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                if len(substring) == len(set(substring)):
                    longest = max(longest, len(substring))

            return longest

        - Time complexity: O(n³)
            - Generate 0(n²) substrings
            - Checking uniqueness with set(substring) takes up to O(n)

        - Space : O(n) 
            - set(substring) creates a set under the hood and loops theorugh every character once
            - Each set get discarded after each iteration
        
        - - -

        Optimized (Sliding window + Set):
        Idea: Instead of rebuilding every substring:
            - Keep one window
            - Expand it with the right pointer.
            - If a duplicate appears, shrink from the left until it's gone.

        The window always contain unique characters.

        Walkthrough:

        s = "abcabcbb"

        Start:
            left = 0
            seen = {}
            longest = 0

        Add 'a' -> Window: [a]

        Longest = 1

        Add 'b' -> Window: [a, b]

        Longest = 2

        Add 'c' -> Window: [a, b, c]

        Longest = 3

        Next character is a 

        Current window: [a, b, c]
                         ^
                        left
        
        Cannot add another 'a'

        Remove from left:

        remove 'a' -> [b, c]

        Now, add the new 'a': [b, c, a]

        Longest = 3

        Continue till the end.

        - - -
        Pseudocode:

        Create an empty set.

        left = 0
        longest = 0

        For each right pointer:
            While s[right] is in the set:
                Remove s[left] from the set
                Move left forward

            Add s[right] to the set.

            Update longest

        Return longest

        Time complexity: O(n)
        Each character:
            - is added to the set once
            - is removed from the set once

        Although, there is a while loop, the left pointer only moves forward, never backward.
        Across the entire algorithm, both pointers move at most n times.

        Space complexity: O(n)

        In the worst case (all characters are unique), the seen set stores all n characters.
        """
        # Return the length of the longest substring with no repeated characters.
        seen = set()

        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            longest = max(longest, right - left + 1)

        return longest
