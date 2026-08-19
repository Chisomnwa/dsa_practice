class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Input: nums - an array of integers
        Output: return a boolean

        Goal: return a boolean; Trrue is the array contains a duplicate and return false otherwise

        Edge cases:
        - if the array is empty - > return False
        e.g nums = []
        - if the array contains only one number -> return False
        e.g nums = [5]
        - if the array contains only distinct numbers -> return False
        e.g nums = [1,2,3,4]
        - if the array contains a duplicate -> return True
        e.g nums = [1,2,3,3]

        Walkthrough:

        Example 1:
        nums = [1, 2, 3, 3]
                0  1  2  3
                         ↑
        At index 0: have I seen 1 before? No
        At index 1: have I seen 2 before? No
        At index 2: Have I seen 3 before? No
        At index 3: Have I seen 3 before? Yes

        We return True

        - - -
        Brute Force Approach
        Intuition:
        Compare every number with other number and check wether any of them are equal

        Compare nums[i] with nums[i+1], nums[i+2], nums[i+3]... and so on

        For example:
        nums = [1, 2, 3, 3]
                0  1  2  3
                      ↑
                      i
                         ↑
                         j

        At index 0: 
        Compare 1 wth 2
        Compare 1 with 2
        Compare 1 with 3

        At index 1:
        Compare 2 with 3
        Compare 2 with 3

        At index 2:
        Compare 3 ith 3

        And 3 -> 3 is a duplicate!

        Algorithm:
        1. start with the first number
        2. compare it with every number after it
        3. if the two numbers are equal, return True
        4. Move to the next number
        5. continue until all pairs have been checked
        6. if no duplicate is found, return False

        Pseudocode
        for i from 0 to length of nums - 1
            for j from i + 1 to length of nums - 1 

                if nums[i] == nums[j]
                    return True

        return False

        Time complexity: O(n^2) because we potentially compare every pair of numbers
        Space complexity: O(1) because no extra data structure

        - - -
        Optimized Approach(Using a Hash Set)

        Intuitiion:
        Can we save time and avid coparing every number against every other number?
        We need to avoide repeatedlyvisting uubers we have already visited before.

        We need a data structure to store every number wehave visited before.

        Set is a perferct data structure.

        Say we have nums = [1, 2, 3, 3]

        set = {}

         nums = [1, 2, 3, 3]
                 0  1  2  3
                          ↑
                       pointer

        At index 0: Have I seen 1 before? No
            set = {1}
        At index 1: Have I seeen 2 before? No
            set = {1, 2}
        At index 2: Have I seen 3 before? No
            set = {1, 2, 3}
        At index 3: Have I seen 3 before? Yes

        Return True

        Algorithm:
        1. Create an empty set called seen
        2. Go through each number in nums
        3. Check wether the number is already in seen
        4. If it is, return True
        5. if not, add it to seen
        6. If we fimish the entire array, we return False

        Pseudocode:
        create an empty set

        for i from 0 to length of nums - 1
            check if nums[i] is in set
                return True if it's in set
            else:
                Add it to set
        return False
        """
        # # brute force Implementation
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Optmized Approach Implementation
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])

        return False
