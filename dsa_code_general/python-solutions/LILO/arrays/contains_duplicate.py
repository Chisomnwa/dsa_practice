"""
Contains Duplicate

Given an integer array 'nums', return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true


EXample 2:
Input: nums = [1,2,3,4]
Output: false
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        
        Input: array of numbers
        Output: bool

        Goal: check if any value appears twice

        edge cases: 
        - what if array is empty
            -> return false

        Trying the example inputs:

        Example 1:
        nums = [1, 2, 3, 1] -> True
                         ^        

        brute force approach:
            1: 2, 3, 1  -> True

        Example 2:
        nums: [1, 2, 3, 4]
                        ^

            1: 2, , 3, 4
            2: 3, 4
            3: 4
            4:           -> False

        Why brute force is slow?
            - If you have large numbres, you are rechecking the same numbers multiple times

        Optimized approach Pseudocode:

            seen = set(1, 2, 3, )  -> O(1) constant time lookup and stores distinct elements

            nums = [1, 2, 3, 4, 1]
                                ^
            loop through nums
                check if i've seen element
                    if seen:
                        return True
                    if not seen:
                        add to seen
                return False
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


sol = Solution()
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]

print(sol.containsDuplicate(nums1))
print(sol.containsDuplicate(nums2))

"""
brute force approach:
- Time complexity: O(n²) because for each element, we compare it against every other element in the array.
- Space complexity: O(1), no extra data structure was created.

optimized approach:
- Time complexity: O(n) because we loop through each element once, and set lookups are O(1) on average.
- Space complexity: O(n) because the set can grow to hold every element in the worst case (no duplicates).
"""