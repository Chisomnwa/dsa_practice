"""
128. Longest Consecutive Sequence

Medium - https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: 
            - An unsorted list of integers

        Output: the length of the longest consecutive elements sequence

        Goal: Given an array of integers, look at how many numbers that consecutively follow each other and return their number (how many they are)
            - The diference between the elements cannot be greater than 1,

        Edge Cases:
            - An array can be empty, so if array is empty -> return 0
            - One element should -> return 1
            - nums[i] i.e a number in the array can be negative, zero or positive.
            - Can a number appear more than once? yes. Showing from the example given, we only need to  consider unique appearances.

        

        Walkthrough:
        Example 1:

        nums = [100, 4, 200, 1, 3, 2]
        longest_con_seq = [1, 2, 3, 4]
        len(longest_con_seq) = 4

        return 4

        Example 2: 

        nums = [0,3,7,2,5,8,4,6,0,1]
        longest_con_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        len(longest_con_seq) = 9

        Example 3:

        nums = [1, 0, 1, 2]
        longest_con_seq  = [0, 1, 2]

        len(longest_con_seq) = 3

        Example 4:

        nums = []
        longest_con_seq = []
        len(longest_con_seq) = 0

        Example 5

        nums = [-1, -2, -7, 5, 2, 1, 3, 4, 0 12, 2, 5]
        longest_con_seq = [-2, -1, 0, 1, 2, 3, 4, 5]
        len(longest_con_seq) = 8

        Brute force approach:
        For every number:
        - Assume it's the start of a sequence
        - Keep checking wjhether the next consecutive number exists by scanning the entire array.
        - Count how long the sequemce is
        - Update the maximum length

        Pseudocode:

        if nums is empty:
            return 0

        result = 0

        for num in nums:

            current = num
            length = 1

            while True:

                found = False

                For each value in nums:
                
                    If value == current + 1:
                        found = True
                        current += 1
                        length += 1
                        break

                If found is false:
                break

            result = max(result, length)

        return result
        """
        # if not nums:
        #     return 0

        # result = 0

        # for num in nums:

        #     current = num
        #     length = 1

        #     while True:

        #         found = False

        #         for value in nums:
        #             if value == current + 1:
        #                 found = True
        #                 current += 1
        #                 length += 1
        #                 break

        #         if not found:
        #             break

        #     result = max(result, length)

        # return result

        ####################################

        """
        Optimized approach (Hash set):

        nums = [100,4,200,1,3,2]

        A sequence should only be counted once.

        Instead of starting from every number, only start from numbers that are the beginning of a sequence.

        How do we know a number is the beginning?

        if num - 1 does not exist

        For example: 1 is the beginning because 0 doesn't exist.

        But 2 is not the beginning because 1 already exits.

        - - -

        walkthrough

        nums = [100,4,200,1,3,2]

        Convert to a set = {100, 4, 200, 1, 3, 2}

        num = 100
        Check: 99 in set? -> No
        Start counting: 100 -> length = 1
        101 doesnt exist -> Done

        num = 4
        Check: 3 in set? Yes
        Don't start here. Why? Because if we started. here, we'd count 4 again.

        num = 200
        Check: 199 does it exist? No
        Start counting: 200 -> length = 1

        num = 1
        Check: 0 in set? No
        Start counting: 1, 2, 3, 4 -> length = 4

        num = 3
        2 exists. Skip

        num = 2
        1 exists. Skip

        Answer = 4

        - - -
        Pseudocode:

        Convert nums into a set.

        reuslt = 0

        For each number:

            if number - 1 not in the set:

                length = 1
                current = number

                while current + 1 exists:

                    current += 1
                    length += 1

                Update result

        Return result
        """
        num_set = set(nums)

        result = 0

        for num in num_set:

            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                result = max(result, length)

        return result
    