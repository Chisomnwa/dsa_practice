class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Input: nums -> list of integers
        Output: return bool
            - true if nums contains duplicate
            - false if all numbers are unique

        Goal:
            n true if the list contains a duplicate and false otherwise

        Edge cases:
        - One element -> return False
        - All unique numbers -> return False
        - Duplicates at the beginning -> return True
        - Duplicates at the end -> return True
        nums can't be empty because vonstraints assy=ured that
        - nums[i] can be poitive or negative

        Walkthrough:
        Example: 
        nums = [1, 2, 3, 1]

        Have I seen this before?

        - Visit 1
            Haven't awwn it

        - Vist 2
            Haven't seen it

        - Visit 3
            Haven't sseenn it

        -   Visit 1
            Have seen it

        Return True

        Brute Force Approach:

        Pseudocode:
        Loop throught the list of nums:
            loop again starting from the second element in the list:
                if nums[i] == nums[j]:
                    return True
            return false

        Python Implementation:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

            return False

        Time complexity: O(n^2) because in the worst case, every element is compared
        Space complexity: O(1) because no extra data structure

        - - -
        Optimized approach:

        Pseudocde:
        Create an empty set

        lop through each item in nums:
            if it's already in set:
                return true
            els:
                add item to set

            return false
        """
        nums_set = set()

        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
           
            nums_set.add(nums[i])

        return False
