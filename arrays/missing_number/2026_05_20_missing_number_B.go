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

func MissingNumberB(nums []int) int {
	n := len(nums) 						// Get the length of the array (n)

	expectedSum := n * (n + 1) / 2 		// Calculated the expected sum using Gauss's formula: n * (n + 1) / 2

	actualSum := 0 						// Initialize actualSum to 0

	for _, num := range nums { 			// Loop through each number in the array
		actualSum += num 				// Add current number to actualSum
}
	// Return the difference between expected and actual sum (the missing number)
	return expectedSum - actualSum
}

/*
Intuition: Gauss's formula, n(n+1)/2, allows us to instantly calculate the total 
sum of all consecutive numbers from 0 to n.

Imagine a scenario: you have all numbers from 0 to 4 sitting in an array,
but one number is missing:
1. The Expected Sum: if none of the numbers were missing, they would add up perfectly:
0 + 1 + 2 + 3 + 4 = 10. Gauss's formula gives us this theoritical sum instantly without
adding the digits one by one.

2. The Actual Sum: We loop through your Go array and sum up the numbers that
are present.

3. The Missing Number: SUbstracting the actual sum from the expected total sum
leaves the misisng number behind.

Walkthrough example:
nums = [3, 0, 1]

Step 1: len(nums) = 3
Step 2: expectedSum = 6
Step 3: actualSum = 0
Step 3: For loop
	num = 3; actualSum = 3
	num = 0; actualSum = 3
	num = 1; actualSum = 3 + 1 = 4

Step 4: return 6 - 4 = 2

Time complexity: O(N):
	- len(nums) → O(1)
	- n * (n+1) / 2 → O(1) (arithmetic operation)
	- for loop iterates through all N elements → O(N)
	Overall : O(1) + O(1) + O(N) = O(N)

Space complexity: n, expectedSum, actualSum are all variables with contstant space →  O(1)
*/