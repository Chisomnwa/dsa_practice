package concatenationofarray

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

// Using a brute force approach (Manual, element-by-step copying)
func GetConcatenationA(nums []int) []int{
	n := len(nums)
	ans := make([]int, 2 * n)

	for i := 0; i < n; i++{
		// Get the first half of ans
		ans[i] = nums[i]
	}

	for i := 0; i < n; i++ {
		// Get the second half of ans
		ans[i + n] = nums[i]
	}

	return ans
}

/*
Intuition: Given an integer `nums` of length `n`, we need to create a new array `ans` of 
length `2n` such that:

	- For 0 <= i < n, ans[i] == nums[i]
	- For 0 <= i < n, ans[i + n] == nums[i]

In simpler terms, the output `ans` is just the `nums` array concatenated with
itself. i.e., ans = nums + nums

Walkthrough: CORRECT THISSSSSSSSSSS
nums = [1,2,1]

Step 1: get the length of nums
	n = len(nums) = 3

Step 2: Create a new array `ans` of size `n`.
	ans := make([] int, 2 * n) → ans = [0, 0, 0, 0, 0, 0]

Step 3: Iterate through the array `nums` twice
	- in the first pass, assign elements from nums for the first half of ans
	- in the second pass, assign elements from nums to the second half of ans

	when  i = 0; n = 3:
		ans[i] = nums[i] = nums[0] = 1

		ans[i + n] = nums[i] → ans[0 + 3] = ans[3] = 1

		ans becomes = [1, 0, 0, 1, 0, 0]

	when i = 1; n = 3:
		ans[i] = nums[i] = nums[1] = 2

		ans[i + n] = nums[i] → ans[1 + 3] = ans[4] = 2

		ans becomes = [1, 2, 0, 1, 2, 0]

	when i = 2; n = 3:
		ans[i] = nums[i] = nums[2] = 1

		ans[i + n] = nums[i] → ans[2 + 3] = ans[5] = 1

		ans becomes = [1, 2, 1, 1, 2, 1]

Step 4: Return ans = [1,2,1,1,2,1]

Time complexity : Because we looped through the elements twice; O(n) + O(n) = O(2n) → O(n)
Space complexity : O(n) because we created an extra array(an extra data structure)
*/