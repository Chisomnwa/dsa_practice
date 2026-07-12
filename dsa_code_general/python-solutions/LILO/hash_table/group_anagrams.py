"""
49. Group Anagrams
Medium - 

Problem link [49] - https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Input : 
            - a list of lowercase strings
            - can contain empty strings

        Output:
            - A list of groups
            - Each group contains strings that are anagrams of each other

        Goal: Group together all strings that are anagrams.

        Example:
        [eat", "tea", "tan", "ate", "nat", "bat"]

                            |
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

        Edge cases:
        - Empty string -> return on empty string
            input: [""]
            output: [[""]]

        - One string -> return a one string
            input: ["a"]
            output: [["a"]]

        - Duplicate strings -> duplicates should stay in the same anagram group
            input: ["eat", "eat", "tea"]
            output: [["eat"], ["eat"], ["tea"]]

        - All strings are already anagrams -> they all belong to one group
            input: ["eat", "tea", "ate"]
            output: [["eat", "tea", "ate"]]

        - No strings are anagrams -> each string forms its own group
            input: ["cat", "dog", "pen"]
            output: [["cat"], ["dog"], ["pen]]

        Walkthrough:

        input: ["eat", "tea", "tan", "ate", "nat", "bat"]

        Notice: 
        - eat, tea, ate all become aet when sorted
        - tan, nat become ant when sorted
        - bat becomes abt when sorted

        Idea: Use the sorted string as the dictionary key

        Dictionary becomes:

        {
            "aet": ["eat", "tea", "ate"],
            "ant": ["tan", "nat"],
            "abt": ["bat]
        }

        Return:
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

        - - -
        Brute force idea:
        - Compare each word with every other ord
        - If two words are anagrams:
            - Put them in the same group
            - Mark the second word as already grouped so you don't process it again.
        
        - To check whether twoo words are anagrams:
            - sort both words
            - Compare the sirted strings.

        Pseudocode:
        Create an empty result list

        create an empty set called visited

        For each index i:

            If i has already been visited:
                continue

            Create a new group containing str[i]

            Mark i as visited

            For each index j after i:
                If j has not been visited:
                    if sorted(strs[i]) == sorted(strs[j]):
                            Add strs[j] to the group

                            Mark j as visited

            Add the group to the result

        Return result

        - - -

        Brute Force Code:

        result = []
        visited = set()

        for i in range(len(strs)):

            if i in visited:
                continue

            group = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(strs)):

                if j not in visited:

                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        visited.add(j)

            result.append(group)

        return result

        Time complexity: O(n² · k log k)
        Why?
            - Outer loop: O(n)
            - Inner loop: O(n)
            - Every comparism sorts two strings: O(k log k)
        Overall: O(n² · k log k)

        Space Complexity: O(n)
        Why?
            - visited can store up to n indices.
            - result stores the grouped strings (the output itself is typically not counted as extra space in interviews, but the auxilliary set is O(n)).
            
        - - -
        Optimized approached:
        Key insight: Every anagram has the same sorted version.

        Example:
        eat -> aet
        tea -> aet
        ate -> aet

        Use: sorted(word) as the dictionary key

        Pseudocode:
        Create an empty dictionary

        For each word:

            Sort the word

            Convert it to a string

            If the key is not in the dictionary:
                Creat an empty list

            Append to that list

        Return all dictionary values
        """

        # stores sorted_word -> list of anagrams
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        