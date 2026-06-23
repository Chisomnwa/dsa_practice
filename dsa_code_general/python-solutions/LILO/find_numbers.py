class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        input: array of nums

        output: the number of integers with an even number of digits

        goal: to return an int, which represents how many integers are made of even digits

        edge cases:
            - No need to treat an empty array since constraints asssured us that array can never  be empty. i.e 1 <= nums.lenth <= 500
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
            digits_num = lenstr((nums[i]))
            if digits_num % 2 == 0:
                count += 1
        return count

        ---

        Is this brute force approach efficient?

        Time complexity: REWRITE HERE

        Space complexity:

        This is efficient because we already have O(n) time complexity. We definitely have to do a one time pass on each of the elements in the array.

        No extra data structures, so no need for further optimizations.


        """
        # REWRITE THIS TO OPTIMIZED APPROACH
        n = len(nums)

        count = 0

        for i in range(n):
            digits_num = len(str(nums[i]))

            if digits_num % 2 == 0:
                count += 1

        return count
        