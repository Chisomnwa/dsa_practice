"""
XOR Operation in an Array
Easy
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

Example 1:

**Input:** n = 5, start = 0
**Output:** 8
**Explanation:** Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

**Input:** n = 4, start = 3
**Output:** 8
**Explanation:** Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Input: 
            - n -> number of elemts in the array
            - start -> starting value

        We don't actually recieve nums, we generate it.

        The rule: nums[i] = start + 2 * i

        example:
        n = 5
        start = 0

        We'll generate:
            i = 0 -> 0 + 2(0) = 0
            i = 1 -> 0 + 2(1) = 2
            i = 2 -> 0 + 2(2) = 4
            i = 3 -> 0 + 2(3) = 6
            i = 4 -> 0 + 2(4) = 8

        array: [0,2,4,6,8]

        Output: return the XOR of every element

        meaning: 0 ^ 2 ^ 4 ^ 6 ^ 8

        Edge cases:
            - n = 1
            - start = 5

            nums[i] = start + 2 * i -> 5 + 2 * 0 -> 5

            answer = 5

        Run through examples:
        Example 1:
            n = 5
            start = 0

            nums = [0, 2, 4, 6, 8]

            XOR: 

            Binary:
                0 = 0000
                2 = 0010
                4 = 0100
                6 = 0110
                8 = 1000

            XOR step-by-step:
                 0 ^ 2 = ?
                 0000
                 0010
                 ----
                 0010    ---> which is 2

                 2 ^ 4 = ?
                 0010
                 0100
                 ----
                 0110    ---> which is 6

                 6 ^ 6 = ?
                 0110
                 0110
                 ----
                 0000    ---> which is 0

                 0 ^ 8 = ?
                 0000
                 1000
                 ----
                 1000    ---> which is 8

                 Therefore, return -> 8

        Example 2:
            n = 4
            start = 3

            nums = [3, 5, 7, 9]

            XOR:

            Binary:
                3 = 0011
                5 = 0101
                7 = 0111
                9 = 1001

            XOR step-by-step:
                3 ^ 5 = ?
                0011
                0101
                ----
                0110    ---> 6

                6 ^ 7 = ?
                0110
                0111
                ----
                0001    ---> 1

                1 ^ 9 = ?
                0001
                1001
                ----
                1000    ---> 8

                returns -> 8

                What this approach is doing?

                1. Build an entire array
                2. Store it
                3. Loop again to XOR

                Brute force pseudocode:
                    nums = []
                    for i in range(nums):
                        nums.append(stsrt + x * i)

                    answer = 0

                    for num in nums:
                        answer = answer ^ num

                Time complexity = O(n)
                Space complexity = O(n)

                So, the brute force appraoch is iefficient as it makes the code take extra memeory - not necessary

                Optimized approach:
                - We don't need a new array
                - We can generate each number and immediately XOR it

                Pseudocode:
                    answer = 0

                    loop through i from 0 to n-1:
                        current = start + 2*i
                        anser = answer XOR current
                    return answer

                    Time complexity: O(n)
                    Space complexity = 0(1) - no new data structure
        """
        answer = 0

        for i in range(n):
            current = start + 2 * i
            answer = answer ^ current

        return answer
    

n = 5
start = 0

n2 = 4
start2 = 3

sol = Solution()
print(sol.xorOperation(n, start))
print(sol.xorOperation(n2, start2))
