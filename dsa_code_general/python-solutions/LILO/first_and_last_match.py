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

class Solution():
    def first_and_last_match(self, nums: list[int], target:int) -> list[int]:
        """
        input: a list of nums and a target
        output: list of two integers [index of the first and last occurence of target]

        goal: to return the index positions of the first and last occurrence(positions) of target

        edge cases:
        - if the list is empty -> return [-1, -1]
        - if the target doesn't appear at all  -> return [-1, -1]

        clarifying questions: is nums sorted? I could potentially do this in 
        in O(Logn) with binary search isntead of O(n). BUt, I'll assume it's
        unsorted for now.

        Run through examples with my current understanding:
        Example 1:
        nums = [4, 2, 7, 2, 9] target= 2

        at 0: i = 4 -> no
           1: i = 2 -> first match
           2: i = 7 -> no
           3: i = 2 -> last index
           4: i = 9 -> no

        brute force: 
        first = -1

        first loop:
            [4, 2, 7, 2, 9]
                ^
             first = i -> 1
             break

        last = -1 
        second loop:
        

        2: 4, 2
        2: 7, 2
        2: 9
       
        """