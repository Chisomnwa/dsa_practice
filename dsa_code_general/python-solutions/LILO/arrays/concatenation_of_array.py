"""
/*
[Problem Number 1929]
[Problem LInk]:(https://leetcode.com/problems/concatenation-of-array/description/)

Given an integer array `nums` of length n, you want to create an array `ans` of length
2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, `ans` is the concatenation of two nums arrays.

Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows: 
	- ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
	- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation:
	- ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
	- ans = [1,3,2,1,1,3,2,1]

Constraints:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
*/
"""


############################################################################################
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        input = array of integers of length n
        output = array of integers of size 2n

        goal: to return a new array whose size is double the size of the old array -> nums + nums = ans

        edge cases: 
            - constraints has shown that nums cannot be empty.  i.e n >= 1
            - an array of size 1 -> [x] returns [x, x]

        Run through given examples:
        Example 1:
        nums = [1, 2, 1]

        n (size of ans) = 3

        ans = [0] * (2 * n) -> [0, 0, 0, 0, 0, 0]
                                              ^

        i : 0 -> nums[0] = ans[0] = 1
        i : 1 -> nums[1] = ans[1] = 2
        i : 2 -> nums[2] = ans[2] = 1
        i : 3 -> nums[0] = ans[0 + n] -> ans[3] = 1
        i : 4 -> nums[1] = ans[1 + n] -> ans[4] = 2
        i : 5 -> nums[2] = ans[2 + n] -> ans[5] = 1

        ans = [1, 2, 1, 1, 2, 1]

        Is this brute force approach efficient? Yes, we must always output 2n elements anyway i.e O(n) + O(n) -> 2 * O(n) -> O(n)

        So, going with this:

        n = length of nums
        create a new array of size 2n

        for in in range(nums):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans        
        """
        n = len(nums)

        ans = [0] * (2*n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans
    
sol = Solution()

numsA = [1,2,1]
numsB = [1,2,3,1]

print(sol.getConcatenation(numsA))
print(sol.getConcatenation(numsB))