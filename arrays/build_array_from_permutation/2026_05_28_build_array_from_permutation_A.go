package buildarrayfrompermutation

/*
[Problem Number 1920]
[Problem LInk]:(https://leetcode.com/problems/build-array-from-permutation/)

Given a zero-based permutation `nums` (0-indexed), buyild an array `ans` of the
same length where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and return it.

Example 1:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], 
       nums[nums[5]]]
	= [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
	= [0,1,2,4,5,3]

Example 2:
Input : nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]

Explanation: The arrays ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]],
       nums[nums[5]]]
	= [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
	= [4,5,0,1,2,3]

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct
*/

func BuildArrayA(nums []int) []int {
	// Create an array that will be returned as the new array
	ans := make([]int, len(nums))

	// Initiate a counter to loop through every index
	for i := 0; i < len(nums); i++ {
		// 
		ans[i] = nums[nums[i]]
	}
	return ans
}

/*
Intuition:
- Find nums[i]
- Use that value as another index
- Get nums[nums[i]]
- Store it

Walkthrough:
nums = [0,2,1,5,3,4]

Step 1: We create ans; the new array, same length as nums

Step 2: Loop through nums using index i

	The first iteration
		when i = 0, nums[nums[0]] = nums[0] → 0 → ans[0] = 0
		when i = 1, nums[nums[1]] = nums[2] → 2 → ans[1] = 1
		when i = 2, nums[nums[2]] = nums[1] → 1 → ans[2] = 2
		when i = 3, nums[nums[3]] = nums[5] → 5 → ans[3] = 4
		when i = 4, nums[nums[4]] = nums[3] → 3 → ans[4] = 5
		when i = 5, nums[nums[5]] = nums[4] → 4 → ans[5] = 3

step 3: Return array [0,1,2,4,5,3]

Time Complexity : O(N) - we loop through all the values in the array at once
Space Complexity : O(N) - we created an extra data structure 'ans' (the new array)
*/