package twosum

/*
[Problem Number 1]
[Problem LInk]:(https://leetcode.com/problems/two-sum/description)

Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
*/

// Using Brute Force
func TwoSumA(nums []int, target int) []int {
	// Outer loops picks the first element of the pair
	for i:= 0; i < len(nums); i++ {
		// Inner loop picks the second element of the pair, always ahead of i
		for j := i + 1; j < len(nums); j++ {
			// Checks if thuis pair sums to the target
			    if nums[i] + nums[j] == target {
					return []int {i, j}
				}  
		}
	}
	return []int{}
}

/*
Intuition:
The solution involves contigously picking two numbers, and 
summing them to see if they equal target. The outer loop (i) 
selects  the first number starting from index 0. The inner loop (j)
iterate through all subsequent numbers (starting from i + 1) to 
find a partner for the first number.

I  find a pair that sums to target, I return their indices.

THis methos is simple, readable, reliable, and has a space 
effieciencey of O(1) but time completixy of O(n²), which means 
for large inputs, the performance will be poor.

THere is an opportunity to optimize it and reduce the lookup time
to O(n).

Approach (Step by Step):
nums := []int{2, 7, 5, 9}
target := 9

Step 1: i=0, j=1 → 2 + 7 = 9
Return: [0, 1]

(If it hadn't matched here, the loop would continue checking)
Step 2: i=0, j=2 → 2 + 5 = 7 ✘
Step 3: i=0, j=3 → 2 + 9 = 11 ✘
Step 4: i=1, j=2 → 7 + 5 = 12 ✘
... and so on until a match is found.

Time Complexity: O(n²) - every pair is checked in the worst case
Space Complexity: O(1) - no extra data structures used
*/
