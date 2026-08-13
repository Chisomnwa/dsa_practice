"""
First and Last Match
Video Title: Lecture 3 — The Problem-Solving Journey & Edge Cases
Difficulty: Easy/Medium

## Question Content
In this lecture, we learned that solving a problem is not just about writing code immediately.

A strong engineer first asks:

- What is the goal?
- What are the inputs?
- What should be returned?
- What edge cases could break my solution?

In this problem, you will practice searching through a list while handling edge cases carefully.

## Task
Complete the function first_and_last_match.

The function receives:

nums
a list of integers, and:

target
an integer to search for.

Return a list containing the first and last index where target appears.

If the target does not appear in the list, return:
[-1, -1]

## Examples

Example 1
Input:
[[4, 2, 7, 2, 9], 2]

Expected Output:
[1, 3]
The target 2 first appears at index 1 and last appears at index 3.

Example 2
Input:
[[5, 5, 5], 5]

Expected Output:
[0, 2]
The target appears multiple times. The first index is 0, and the last index is 2.

Example 3
Input:
[[1, 3, 4], 2]

Expected Output:
[-1, -1]
The target 2 does not appear in the list.

Example 4
Input:
[[], 10]

Expected Output:
[-1, -1]
An empty list has no matching indexes.
"""

class Solution:
    def first_and_last_match(self, nums: list[int], target:int) -> list[int]:
        """
        input: a list of nums and a target
        output: list of two integers [index of the first and last occurence of target]

        goal: to return the index of the first and last occurrence(positions) of the target.

        edge cases:
        - if the list is empty -> return [-1, -1]
        - if the target doesn't appear at all  -> return [-1, -1]

        clarifying questions: is nums sorted? I could potentially do this in 
        in O(Logn) with binary search instead of O(n). But, I'll assume it's
        unsorted for now.

        Run through examples with my current understanding:

        Example 1:
        nums = [4, 2, 7, 2, 9] target = 2
                   ^
        
        first : -1

        i = 0: nums[0] = 4 -> no match
        i = 1: nums[1] = 2 -> match! first = 1, break

        I stop as soon as I find the first match, since scanning further
        forward wouldn't change that answer.

        last = -1
        i = 4: nums[4] = 9 -> no match
        i = 3: nums[3] = 2 -> match! last = 3, break

        working backwards from the end, the first macth I hit is
        automatically the rightmost (i.e last occurrence)- so I can stop immediately.

        Resut: [first, last] = [1, 3]

        Example 2:
        nums = [5, 5, 5] target = 5

        first = -1
        i = 0: nums[0] = 5 -> match! first = 0, break

        last = -1
        i = 2: nums[2] = 5 -> match! last = 2, break

        Result: [first, last] = [0, 2]

        Example 3:
        nums = [1, 3, 4] target = 2

        first = -1
        i = 0: nums[0] = 1 -> no match
        i = 1: nums[1] = 3 -> no match
        i = 2: nums[2] = 4 -> no match
        (loop ends, no break triggered)

        first stays at -1

        last = -1
        i = 2: nums[2] = 4 -> no match
        i = 1: nums[1] = 3 -> no match
        i = 0: nums[0] = 1 -> no match

        last stays at -1 too

        Result: [first, last] = [-1, -1]

        What is the problem with this brute force? We are rechecneking the numbers
        multiple times. Inefficnet if I have a large list of numbers.

        My first instincst here is actually to do two seperate scans - one forward
        pass just to find the first match, then a second pass to find the last match.
        That works, but it's wasteful: I'm touching the array twice when I could get
        both the answers from a single pass. So, while it's still O(n), it's roughly
        double the work for no real benefit. I can do this with one pass.

        What best way to appraoch this Pseudocode:

            handle edge cases (list is empty or nums don't exist)

            if target not in list:
                return [-1, -1]

            first = None
            last = None

            loop through nums using enumerate function:
                if v == target:
                    if first is still None:
                        first = i
                    last = i
            return [first, last]
        """
        # handle edge cases (if list is empty or target doesn't exist)
        if target not in nums:
            return [-1, -1]
        
        first = None
        last = None

        for i, v in enumerate(nums):
            if v == target:
                if first is None:
                    first = i
                last = i

        return [first, last]


sol = Solution()

nums1 = [4, 2, 7, 2, 9]
target1 = 2

nums2 = [5, 5, 5]
target2 = 5

nums3 = [1, 3, 4]
target3 = 2

nums4 = []
target4 = 2

sol = Solution()
print(sol.first_and_last_match(nums1, target1))
print(sol.first_and_last_match(nums2, target2))
print(sol.first_and_last_match(nums3, target3))


"""
Brute force:
Time complexity: O(n) because each pass independently scans at most the whole list 
once in the worst case (target not found, or found right at the far edge being scanned from).
Two passes O(n) + O(n), which simplifies to O(n) - constants drop out in Big-O notation.
Space complexity: O(1) because only variables are created. No extra data structures.

Optimized approach:
Time complexity: O(n) because you walk through the list exactly once, checking each element
a single time.
Space complexity: same as above. No extra data structures created.
"""