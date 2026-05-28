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

// Using a Binary Search
func SearchInsertB(nums []int, target int) int {
	// Initialize two pointers; left at start 0, right at the end len(nums) - 1
	left, right := 0, len(nums) - 1

	// Keep searching while left pointer hasn't passed the right pointer
	for left <= right {
		// Find middle index
		mid := (left + right) / 2

		// If middle value is less than target, search right half
		if nums[mid] < target {
			left = mid + 1
		// Otherwise serach left half, (include equal case)
		} else {
			right = mid - 1
		}
	}
	// Return left pointer, position where target should be inserted
	return left
}

/*
The intuition behind the optimized O(log n) solution of solving this question is 
binary search. Because the array is sorted and contains distinct integers, you can 
bypass a slow linear scan, by continally halving the search space.

At any given point, the question boils down to asking: is my target greater or smaller 
than this element?

- if the target is found: return the midpoint index
- if the midpoint value is smaller than the target: the target belongs to the right.
  We shift our search window to the right half.
- if the midpoint value is greater than the target: the target belongs to the left.
  We shift our serach window to the left half.
- When the search window closes: the left pointer (`left` in code) is pointing to the 
  exact index where the pointer either is or belongs.


Walkthrough example:
nums = [1, 3, 5, 6], target = 5

Step 1: Create the left and right pointers (index positions)
	left : =  0
	right := 4 - 1 = 3

Step 2: First iteration - check if left is less than right , which it is
	left (0) < right (3)

Step 3: Get the middle index position
	mid := (0 + 3) / 2 = 1 (gets the integer value, ignores remainder)

Step 4: Confirm if middle value is less than target
	nums[mid] = 3, target = 5 

Step 5: We search the right half
    left = mid + 1 → 1 + 1 = 2
	right = 3 (still 3)

Step 6: Second Iteration - check if left is less than right , which it is
	left (2) < right (3)

Step 7: Get the middle index again
	mid = (left + right) / 2 → (2 + 3) / 2 = 2 (gets the integer value, ignores remainder)

Step 8: Confirm if middle value is less than target
	nums[mid] = 5, target = 5 (they are equal)

Step 9 : Therfeore, we search left half
	right = mid - 1 → 2 - 1 = 1

Step 10: Third iteration - check if left is less than right , which it is NOT
	left (2) > right (1)

Step 11: Final return
	return left which is 2, which is the index poition of target 5

Time complexity: O(log N) → The serach space is halved at every iteration
Space complexity: 0(1) → No extra memory or data structures, just variables with constant memory.
*/
