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

// Using the optimized approach (Euclidean Division)
 func BuildArrayB(nums []int) []int {
	n := len(nums)

	// Phase 1: Encode two numbers in one spot
	for i := 0; i < n; i++ {
		targetValue := nums[nums[i] % n] % n
		nums[i] = nums[i] + (targetValue * n)
	}

	// Phase 2: Decode to keep only the target numbers
	for i := 0; i < n; i++ {
		nums[i] = nums[i] / n
	}
	return nums
 }

 /*
Intuition:
The intuition here involves storing two numbers in a single array element simultaneously.
This allows you to achieve O(1) auxiilliary space complexity by mutating the array in place 
without overwriting the original values needed for subsequent calculations.

The Core Mechanism:
in Go, you can pack two integers into one memory location using the mathematical
formula:
 			New Value = Original Value + (Target Value * Constant)

For this problem:
- Original Value : nums[i]
- Target Value : nums[nums[i]] (the value you want to place there)
- Constant :q(the length of the array, n)

Because the problem guarantees that all numbers in the array are strictly less than the
length of the array (nums[i] < n), you can use the modulo operator (%) to retrieve the 
original value and integer division (/) to extract the new value.

Walkthrough:
nums = [0,2,1,5,3,4]

n := 6

PHASE 1: ENCODING
Store two numbers in one spot using: original + (target * n)

Step 1: Loop through nums using index i

	when i = 0:
		- nums[i] = 0 (original)
		- nums[nums[0]] = nums[0] = 0 (target value)
		- targetValue = 0 % 6 = 0
		- nums[0] = 0 + (0 * 6) = 0

	when i = 1:
		- nums[i] = 2 (original)
		- nums[nums[1]] = nums[2] = 1 (target value)
		- targetValue = 1 % 6 = 1
		- nums[1] = 2 + (1 * 6) = 8

	when i = 2:
		- nums[i] = 1 (original)
		- nums[nums[2]] = nums[1] = 2 (target value)
		- targetValue = 2 % 6 = 2
		- nums[2] = 1 + (2 * 6) = 13

	when i = 3:
		- nums[3] = 5 (original)
		- nums[nums[3]] = nums[5] = 4 (target value)
		- targetValue = 4 % 6 = 4
		- nums[3] = 5 + (4 * 6) = 29

	when i = 4:
		- nums[i] = 3 (original)
		- nums[nums[4]] = nums[3] = 5 (target value)
		- targetValue = 5 % 6 = 5
		- nums[4] = 3 + (5 * 6) = 33

	when i = 5:
		- nums[i] = 4 (original)
		- nums[nums[5]] = nums[4] = 3 (target value)
		- targetValue = 3 % 6 = 3
		- nums[5] = 4 + (3 * 6) = 22

After Phase 1: nums = [0, 8, 13, 29, 33, 22]

PHASE 2: DECODING
Extract target values by dividing by n

 	when i = 0: nums[0] = 0/6 = 0
	when i = 1: nums[1] = 8/6 = 1
	when i = 2: nums[2] = 13/6 = 2
	when i = 3: nums[3] = 29/6 = 4
	when i = 4: nums[4] = 33/6 = 5
	when i = 5: nums[5] = 22/6 = 3

Step 3: Return array [0,1,2,4,5,3]

Time Complexity: O(N) - two passes through the array
Space Complexity: O(1) - no extra data structure (modifies in-phase)

Why it's optimized:
 - Same time as brute force: O(N)
 - But uses O(1) space instead of O(N) by modifying the input array in-place

 Tricky one, but I get the idea
*/ 