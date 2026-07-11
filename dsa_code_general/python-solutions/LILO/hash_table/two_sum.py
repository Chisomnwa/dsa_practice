"""
Question: Two Sum with a Dictionary

A set can tell us whether a complement exists, but Two Sum asks us to return indices.

That means we need to store both:

number -> index

A dictionary is a good fit for this.

Task:
Complete the function two_sum_indices.

The function receives:

- nums: a list of integers
- target: the target sum

Return the indices of two numbers that add up to the target.

If no pair exists, return an empty list.

Examples

Example 1
Input:
[[2, 7, 11, 15], 9]

Expected Output:
[0, 1]

Example 2
Input:
[[3, 2, 4], 6]

Expected Output:
[1, 2]

Hint
For each number, compute the complement. If the complement is already in the dictionary, return the saved index and the current index.

Common Mistakes to Avoid
Storing only numbers when the problem asks for indices
Adding the current number before checking the complement in a way that reuses the same index
Returning values instead of indices
Why This Matters
This is the classic example of using a hash map to remove a nested loop.
"""

class Solution:
    def two_sum_indices(self, nums: list[int], target: int) -> list[int]:
        # Return indices of two numbers that add to target using a dictionary

        """
        Input:
        - nums: A lisst of integers
        - target: a number that the sum of numbers equals to

        Output: the integer of the two numbers that equals to target

        Goal: Return the indices of the two numb ers whose sum equals target.

        Idea: Store each number along with its index.

        For each number:
        1. Compute its complement
            complement = target - num
        2. if the complement is already in the ictionary, we've found the answer.
        3. Otherwise, store the current number and its index

        Walkthrough:
        nums = [2, 7, 11, 15]
        target = 9

        Step 1:
        - Create an empty dictionary
            seen = {}

        - Start looping:
            index 0: nums = 2, complement = 7
            7 not in seen -> seen = {2:0}

            index 1: nums = 7, complement = 2
            2 in seen

            Return [seen[complement], 1] -> [0, 1]

        Pseudocode:

        Create an empty dictionary

        For each index and number:
            compute the complement

            If the complement is in the dictionary:
                return the saved index and the current index

            Store the current number and the index

        Return an empty list

        - - -
        Time complexity: O(n) because of one pass through the list
        Space complexity: O(n) up to n key-value pairs stored
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

        return []
