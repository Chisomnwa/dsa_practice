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

// Using a Hash Map (Optimized Approach)
func TwoSumB(nums []int, target int) []int {
	// Create a map to store each number and its index
	seen := make(map[int]int)

	// Loop through the array with index
	for i, num := range nums {
		// Calculate the number needed to complete the pair
		diff := target - nums[i]

		// Check if we have already seen the complement
		if j, found := seen[diff]; found {
			// Return the stored index and the current index
			return []int{j, i}
		}
		// Store the current number mapped to its index
		seen[num] = i
	}	
	return []int{}
}

/*
Intuition:
Here, we don't need to look for two numbers at once; we only 
need to look for the one that's missing.

For every number `x` I encounter, I already know exactly 
what its partner `y` must be to reach the target (y=target-x).

As I walk through the list, I ask the hash map: "Have you seen my partner yet?"

If the map says "No", I don't give up. I leave my own value and 
index in the map so that if my future partner shows up, they can find me.

I'm trading a little bit of space (the map) to gain massive
speed. I turn a nested search (O(n²)) into a single pass (O(n))
because looking for something up in a map is nearly instant.

In short: It's just like walking into a party looking for a specific friend.
Instead of checking every pair of people, you just ask the person at the
door if your friend already checked in. If not, you leave your name at the
desk and head inside.
*/

/*
Approach (Step by Step):
nums := []int{2, 7, 5, 9, 11}
target := 9

Step 1: 
	i = 0
	num = 2
	diff = 9 - 2 = 7

	Have we seen 7? No
	Store: {2: 0}

Step 2:
	i = 1
	num = 7
	diff = 9 - 7 = 2

	Have we seen 2? Yes → stored at index 0
	Return: [0, 1]

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - map stores at most n entries 
*/
