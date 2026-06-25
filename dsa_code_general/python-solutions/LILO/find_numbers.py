class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        input: array of nums

        output: the number of integers with an even number of digits

        goal: to return an int, which represents how many integers are made of even digits

        edge cases:
            - No need to treat an empty array since constraints asssured us that array can never be empty. i.e 1 <= nums.length <= 500
            - Also, num integers; num[i] can never be zero . i.e 1 <= nums[i] <= 10^5

        Walkthrough with an example:

        Example 1:

        Brute force approach:

        nums = [12, 345, 2, 6, 7896]
                0    1   2  3    4
                                 ^

        at index 0: nums[i] = nums[0] = 12 -> 2 digits -> has even number of digits ✅
        at index 1: nums[i] = nums[1] = 345 -> 3 digits -> has odd number of digits ❌
        at index 2: nums[i] = nums[2] = 2 -> 1 digit -> has odd number of digits ❌
        at index 3: nums[i] = nums[3] = 6 -> 1 digit -> has odd number of digits ❌
        at index 4: nums[i] = nums[4] = 7896 -> 4 digits -> has even number of digits ✅

        return 2

        Example 2:

        Brute force approach:

        nums = [555, 901, 482, 1771]
                 0    1    2     3
                                 ^

        at index 0: nums[i] = nums[0] = 555 -> 3 digits -> has odd number of digits ❌
        at index 1: nums[i] = nums[1] = 901 -> 3 digits -> has odd number of digits ❌
        at index 2: nums[i] = nums[2] = 482 -> 3 digits -> has odd number of digits ❌
        at index 3: nums[i] = nums[2] = 1771 -> 4 digits -> has even number of digits ✅

        return 1

        Pseudocode:

        n = len(nums)

        count += 0

        for i in range of nums:
            digits_num = len(str((nums[i]))
            if digits_num % 2 == 0:
                count += 1
        return count

        ---

        Is this brute force approach efficient?

        Time complexity: O(n * d) or  O(n * log 10(max(nums))). 
            - This means that in the loop, conversion of individual numbers to strings is dependent on the number of digits `d` each number has
              and this costs O(d). So, `d` varies depending on the number. That's why it's O(n * d). The len() function costs O(1).

        Space complexity: O(d), not O(1). This is because the str(nums[i]) creates a brand new string object in memory, with length equal
            to how many digits the number has. It's temporary (i.e discarded during each iteration) but still counts. Big O space complexity
            counts memory used at any point, not just the ones that persist. So, a string length of `d` is `d` units of extra memory.

        So, we need to optimize the code to achieve O(1) space.

        Pseudocode:

        We'll be using // 10 to divide each number to get the number of digits each of them contains.
        Why? Because each number is a base-10 digit (0-9). Dividing by 10 strips off the last digit
        each time, because integer division discards the remainder. 

        logic step-by-step:

        nums = [12, 345, 2, 6, 7896]
                0    1   2  3    4
                                 ^

        at nums[0] = 12: 
            12 // 10 = 1
            1 // 10 = 0
            Final answer = 0; total = 2 diviiodns -> 2 digits ✅

        at nums[1] = 345:
            345 // 10 = 34
            34 // 10 = 3
            3 // 10 = 0
            Final answer = 0; total = 3 divisions -> 3 digits ❌

        at nums[2] = 2
            2 // 10 = 0
            Final amnswer = 0; total = 1 division -> 1 digit ❌

        at nums [3] = 7896
            7896 // 10 = 789
            789 // 10 = 78
            78 // 10 = 7
            7 // 10 = 0
            Final answer = 0; total = 4 divisions -> 4 digits ✅

        """
        # Helper function to get the counts digits in each number in nums
        def count_digits(x):
            digits = 0
            while x > 0:
                x = x // 10
                digits += 1
            return digits
        
        n = len(nums)
        count = 0

        for i in range(n):
            # instead of using len(string[num[i]]) to get the length of each integer, use the helper function
            digits_num = count_digits(nums[i])

            if digits_num % 2 == 0:
                count += 1

        return count

sol = Solution()
print(sol.findNumbers([12, 345, 2, 6, 7896]))
print(sol.findNumbers([555, 901, 482, 1771]))

"""
Time complexity: 0(n * d) -> unchanged from the brute force approach, because we are still doing digit
    by digit per work.

Space complexity: O(1) -> count digits only uses a couple of integer variables that don't grow with input size.
"""

        