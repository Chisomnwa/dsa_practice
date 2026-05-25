package searchinsertposition
/*
[Problem Number 35] - Binary Search
[Problem LInk]:(https://leetcode.com/problems/search-insert-position/)

Given a sorted array of disntict integers and a target value, return the index
if the target is found. If not, return the index where it would be it were inserted 
in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 10²
-10⁴ <= nums[i] <=  10⁴
nums contains disntinct values sorted in ascending order
-10⁴ <= target <= 10⁴
*/

// Using a Brute Force - A Linear Scan
func SearchInsertA(nums []int, target int) int {
	// Iterate through the array sequentially
	for i, num := range nums {
		// If we find an element >= target, this is the insert position
		if num >= target {
			return i
		}
	}
	// If we reach the end, it goes at the very end
	return len(nums)
}

/*
Intuition: The intuition involves searching for an insert position 
using a linear scan - we simply walk through the sorted array from 
left to right, comparing the target against each element until you
find a value equal to or greater than your target. THe current index 
is your answer, or if you reach the end, it goes at the very back.

Step by Step Walkthrough:

So, we look at it this way:

1. Target exists: The moment you find a number exactly equal to the
target, you return its index.

2. Target belongs in the middle: The moment you find a number that is 
strictly greater than the target, you know the target belongs right before 
it. Because everything before this index is smaller and everything after 
is larger, you stop and return the index.

3. Target belongs at the end: If you check every single element in the array
and none of them are greater than the target, the target is larger than all 
elemnets currently in the list. It belongs at the end, so you return the 
length of the array.


Walkthrough example:
nums = [1, 3, 5, 6], target = 2

Step 1: Loop through the array
Step 2: When you find a number greater than the target, return the index of that number
		because that's where the number was supposed to be.
		
		So, when:
			i = 0 → num = 1
			i = 1 → num = 3

			Therefore 1 is returned because 2 is supposed to be placed before 3

Step 4: If target is not found in the array, then we return the len(nums) which will be the 
index position of the target.

Time complexity: O(N) → We iterate over every element through the for loop.
Space complexity: 0(1) → No extra memory or data structures, just variables with constant memory.
*/