class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Input: nums - an array of integers

        e.g nums = [2, 1, 5, 0, 4, 6]
            We need to find three indices:

            i < j < k and nums[i] < nums[j] < nums[k]

        Output:
        - true if such triplets exists
        - false if they don't exist

        For example:
        nums = [2, 1, 5, 0, 4, 6]
        Output = True

        Because:
        index: 0 1 2 3 4 5 
        nums = 2 1 5 0 4 6
                 ↑     ↑ ↑

        So (1, 4, 5) is a valid triplet

        Goal: The goal here is to determine whether we can find three numbers in increasing order while also respecting their positions in the array.

        The two requirements are important:
        1. Position requirement

            i < j < k

            The first number must appear before the second, and the second before the third

        2. Value requirtement

            nums[i] < num[j] < nums[k]

            The values must also be increasing, and we're looking for :
            FIRST < SECOND < THIRD where they appear in that same order in the array

        Edge Cases:

        1. When Array has fewer than 3 elements
        e.g [1, 2] -> return False

        2. When we have strictly decreasing elements
        e.g [5, 4, 3, 2, 1] -> return False

        3. When we have duplicates
        e.g [1, 1, 2] -> return False

        4. When we have an increasing triplet that isn't obvious/isn't contiguous
        e.g [2, 1, 5, 0, 4, 6] - > return True
        because the test says we are looking for a subsequence, not necessarily three adjacent elements

        Walkthrough:
        nums = [2, 1, 5, 0, 4, 6]

        We need to find: i < j < k and nums[i] < nums[j] < nums[k]

        A brute force way to think about it:
        "let me choose a first number, then look for a larger second number after it, then look for a larger third number after that"

        Starting with index 0:
                0  1  2  3  4  5
        nums = [2, 1, 5, 0, 4, 6]
                ↑     ↑        ↑
                i     j        k

        Our first nuumber is 2, then we look for something greater tha 2
        We find 5, and we look for something greater than 5
        We find 6

        Therefore 2 < 5 < 6 and nums[0] < nums[2] < nums[5]

        We have orther truplets in the array but because we only to to find a valid one, we stop here.

        - - -

        Brute Force Approach
        Intuition:
        The most straightfprward thing we can do is to try every possiible combination of three indices

        We choose:

        1. A first index i
        2. A second index j after i
        3. A third index k after j

        Then check that: nums[i] < nums[j] < nums[k]

        If we find one, immediately return true
        if we've checked every posssible triplet and haven't found one, return false.

        Algorithm:
        1. If the array has fewer than three elments, return False
        2. Choose the first index i
        3. Choose a second index j after i
        4. Choose a third index k after j
        5. Check wether nums[i] < nums[j] < nums[k]
        6. if it is true, return true
        7. Continue checking all possible triplets
        8. If no valid triplet is found, return false

        Pseudocode:
        if length of nums < 3:
            return false

        for i from 0 to length of nums - 2
            for j from i + 1 to length of nums - 1
                for k from j + 1 to length of nums

                    if nums[i] < nums[j] AND nums[j] < nums[k]
                        retun true
        return false

        Time complexity: O(n^3) which is factorial becuase we are examining combinations of three elements
        Space complexity: O(1) because we only created variables

        - - -

        Optimized approach (Greedy)
        The patter we are testing here is greedy or mainataining the smallest possible candidates

        We ask: does an increasing subsequence of length 3 exist?

        The greedy idea is: 

        "As we scan from left to right, keep track of the smallest possible first number
        and the smallest possible second number we've seen"

        We'll call them:
        - first 
        - second

        If we eventually find a number biiger than second, we've got:

        first < secooond < third

        and therefore we've found an increasiing triplet

        Intuition:
        say nums = [2,  1, 3, 0, 4, 6]

        We want to build: first < second < third

        Our first goal isn't to immediately find the triplet.

        Our goal is to find the smallest possible first number.

        At index[0]: 2
        first = 2

        At index[1]: 1
        i < 2

        first = 1

        At index[2]: 5
        5 > 1

        second = 5

        At index[3]: 0
        0 < 1
        first = 0

        At index[4]: 4
        4 <= 5

        second = 4

        At index[5]: 6

        Here: first < second < 6 -> 0 < 4 < 6

        return True

        Algorithm:
        1. Set first to infinity
        2. Set second to infinity
        3. For every number in nums:
            - If the number is smaller than or equal to first, make it the new first
            - Otherwise, if the number is smalller than or equal to second, make it the new second
            - Otherwise, if the number is both greater than both first and second, we've found an increasing triplet. So return True
        4. Return false if we reach the end without findng one.

        Pseudocode:
        first = infinity
        second infinity

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

        Time complexity: 0(n) because we only iterate through the elements in nums once.
        Space complexity: O(1) because no extra data structures, just variables created.
        """
        # Brute force Approach
        # if len(nums) < 3:
        #     return False

        # for i in range(len(nums) - 2):
        #     for j in range(i + 1,  len(nums) - 1):
        #         for k in range(j + 1, len(nums)):

        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True

        # return False

        # Optimized Approach (Greedy)
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
