package missingnumber

/*
[Problem Number 268]
[Problem LInk]:(https://leetcode.com/problems/missing-number/description/)

Given an array `nums` containing `n` distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
[0, 3]. 2 is the missing number in the range since it does not appear in `nums`.


Example 2:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
[0,9]. 8 is the missing number in the range since it does not appear in `nums``.

COnstraints:
n == nums.length
1 <= n <= 10⁴
0 <= nums[i] <= n
All the numbers of nums are unique
*/
import "sort"

func MissingNumberA(nums[]int) int {

	n := len(nums) // get the len of nums

	sort.Ints(nums) // sort the numbers in ascending order
	
	for i, num := range nums { // loop thorugh the array and match the numbers to their index positions
		if i != num {  // if index doesn't match the value
			return i // ireturn the missing numebr
		}
	}
	return n // if no mismatch is found, the missing number is the array length
}

/*
Intuition: The problem states that the array contains `n` unique numbers in the 
range `[0, n]`. This means the length of the array itself is `n`. If no number was 
missing, the array will contain every integer from `0` to n.

So, here the approach involves putting the array in a sequential order and finding
the "gap" or the number that doesbn't match its index.

Imagine a sorted shelf of books numbered sequentially from 0 to n. If you check every
space, you expect the first book to be 0, the second book to be 1, and the i-th book to
be exactly i. If you are looking at a space, and the number on the book does not match
the space's position, you immediately know a book (number) is missing.

The process step by step:
1. Sort: Arrange the numbers in the array in ascending order
2. Scan : Loop through the sorted array and check if the number at index 
	is equal to the integer i
3. Identify: THe first time you find an index where i != num; i.e where index 
	does not match the value, it means the expected index is the missing number.

	If you scan the entire array and find no mismacthes, the missing number is n.

Walkthrough example:
nums = [3, 0, 1]

Step 1: len(nums) = 3
Step 2: nums = [0, 1, 3] - array sorted in ascending order
Step 3: For loop 
	i = 0 → num = 0
	i = 1 → num = 1
	i = 2 → num = 3 error occurs

	Therefore 2 is returned.

Time complexity: O(NlogN) →  sort.Ints(nums) uses quicksort/mergesort internally  → O(NLogN)
Space complexity: 0(1) → sort.Ints(nums) sorts array in place so new memeory is created.
*/