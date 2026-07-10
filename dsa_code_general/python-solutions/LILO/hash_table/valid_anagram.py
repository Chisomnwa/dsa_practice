"""
Check Valid Anagram with Frequency Maps
Medium

Video Title: Lecture 2.8 - Valid Anagram: Complexity and Dictionary Behavior
Difficulty: Medium-Easy

Question Content
Sorting can solve an anagram problem, but sorting takes extra time.

A hash map approach counts characters in each string and compares the counts.

Task
Complete the function `is_anagram`.

The function receives two strings, `s` and `t`.

Return True if they are anagrams.

Return False otherwise.

Examples:

Example 1
Input:
["race", "acer"]

Expected Output:
True

Example 2
Input:
["rat", "car"]

Expected Output:
False

Hint:
Two strings are anagrams when their character frequency maps are equal.

Common Mistakes to Avoid
- Checking only whether the same letters appear, without checking counts
- Forgetting to handle strings with different lengths
- Assuming dictionary keys are stored in sorted order

Why This Matters:
Hash maps let us compare character frequencies without depending on sorted order.
"""

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """
        Input: two strings `s` and `t`

        Output:
            - True if strings are anagrams
            - False otherwise

        Goal: Determine wether both strings contain the same characters with the same frequencies, regardless of their other.

        Brute Force:
        1. Sorth both starings
        2. Compare the soirted strings
        3. If they are equal, return True; otherwise, return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True

    return False

        Time complexity: Time complexity : O (n log n)
        Space complexity: O(n)

        - - -

        Optimized Approach (Hash Map)
        - Use a frequency map to count the occurrence of each character
        - If the two maps are equal, the strings are anagrams.

        Walkthrough example:
        s = "listen"
        t = "silent"

        Build the frequency map for s:
        {
            'l': 1,
            'i': 1,
            's': 1,
            't': 1,
            'e': 1,
            'n': 1
        }

        Build the frequency map for t:
        {
            's': 1,
            'i': 1,
            'l': 1,
            'e': 1,
            'n': 1,
            't': 1
        }

        The dictionaries are identical, so return true

        - - -
        If the strings have different lengths:
            Return False

        Create an empty dictionary for each string.

        Count the frequency of every character.

        Compare the two dictionaries.
        
        If they are equal:
            Return True

        Return False

        - - -
        Time complexity: O(n) because O(n) + O(n) for each loop equals O(n)
        Space complexity: O(n) because of the extra dictionary created to store n unique characters
            - for the first optimized version -> O(n) + O(n) = O(n)
            - for the second optimized version -> O(n)
        """
        # Return True if s and t are anagrams.
        # if len(s) != len(t):
        #     return False

        # s_dict = {}

        # t_dict = {}

        # for char in s:
        #     if char not in s_dict:
        #         s_dict[char] = 0
            
        #     s_dict[char] += 1

        # for char in t:
        #     if char not in t_dict:
        #         t_dict[char] = 0

        #     t_dict[char] += 1

        # if s_dict == t_dict:
        #     return True
       
        # return False

        # OR

        # Anagrams must be equal
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in s
        for char in s:
            if char not in freq:
                freq[char] = 0

            freq[char] += 1

        # Remove counts using t
        for char in t:
            if char not in freq:
                return False

            freq[char] -= 1

            # Kepp only the characters that haven't been completely matched
            if freq[char] == 0:
                del freq[char]

        # if characters match exactly, the dictionary will be empty
        return len(freq) == 0
