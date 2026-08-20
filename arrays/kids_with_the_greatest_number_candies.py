class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Input: 
        - candies : array of integers e.g [2,3,5,1,3]
        - extraCandies: an interger e.g 3

        We give all the extra candies to one kid at a time

        Output: return a boolean array of the same length of candies

        For each kid:
        - True -> after receiving all extracandies, that kid has the greatest number of candies
        - False -> if they don't

        e.g [True, True, False, True]

        Goal: for each kid, determine:

        "if I give this kid all the extra candies, will their total be at least as large as the greates number of any candies any kid currently has"

        Notce the word "at least"

        If the maximum is 5, having 5 is enough. They don't need to have more thatn 5.

        Edge cases:
        - When a kid already has the maximm number of candies
            e.g candies = [5, 2, 3]
                extraCandies = 1

            The kid with 5 will remain the greatest: 5 + 1 = 6 -> True

        - Multiple kids can be greatest
            e.g candies = [5, 2, 3]
                extraCandies = 2

            Here, several kids might reach or exceed the current maximum, so multiple True values are allowed

        - When a kid still doesn't reach the maximum
            e.g candies = [2, 3, 5]
                extraCandies = 1

            For the kid with 2: 2 + 1 = 3
            3 < 5, so that kid is False

        Walkthrough:

        candies = [2, 3, 5, 1, 3]
        extraCandies = 3

        First, we identify the kid who currently has the greatast number of candies

        candies = [2, 3, 5, 1, 3]
                         ↑
                      greatest

`       Now, we examine each kid one by one:

        candies = [2, 3, 5, 1, 3]
                   ↑

        kid 1: 2 + 3 = 5 -> True
        kid 2: 3 + 3 = 6 -> True
        kid 3: 5 + 3 = 8 -> True
        kid 4: 1 + 3 = 4 -> False
        kid 5: 3 + 3 = 6 -> True

        The skill this problem is testing against is one pass arrray traversal + maintaining a useful aggregate value.
        It's a good fundamental array problem because it tests whether you can identify a value that you need to comapre every element against.

        - - -
        Brute force Approach

        Intuituion:
        For each kid, we are saing:
        1. Give that kid all extracandies
        2. Look through all other kids to find the greatest number of candies
        3. Compare the new kid's total against the greatest number
        4. Append True or False

        So, we're essentially saying: "For every kid, I'll check everyone else to determine whether this kid can become the greatest."

        Algorithm:
        - Calculate candies[i] + extraCandies
        - Find the maximum value among all candies
        - if the new value>= maximum:
                append True
            otherwise:
                append False

        Pseudocode:
        create an empty result list

        for each kid:
            new_candies = candies[i] + extraCandies

            maximum = 0

            for each kid j:
                if candies[j] > maximum:
                    maximum = candies[j]

            if new_candies >= maximu:
                append True to result
            else:
                append False to result

        return result

        Time complexity: O(n^2) because the outer and inner loop runs (n x n) times.
        Space complexity: O(n) because we creaed result which contains n boolean values.

        NB: The problem with this approach is that we search for the maximum frm scratch for every kid.

        - - -

        Optimized Approach

        iIntution:
        The problem is not testing any speacial DSA pattern. The optimization comes from noticing something very simple:
            "The maximum number of candies doesn't change while we are checkimg each kid"

        In brute force approach, we kept doing this:
        kid 1: serach the entire array for maximum
        kid 2: serach the entire array for maximum
        kid 3: serach the entire array for maximum
        ...

        But the rray hasn't changed.

        For this: candies = [2, 3, 5, 1, 3]

        maximum is always 5.

        Why calculate 5 over and over again????

        We can just calculate it once: using 
        
        max_candies = max(candies)

        Algorithm:
        1. Find the maximum candie
        2. Loop through each kid
        3. Give them extra candies
        4. Compare their new_total with maximum
        45 If their new total is greater than maximum
                append True to result
            otherwise
                append False to result
        6. Return result

        Pseudocode:
        create an empty result list

        Find the maximum candy

        for each kid in candies
            give each kid extracandies and calculate their new total

            compare their new total to the maximum
                if their new total >= maxium
                    append True to result
                otherwise
                    append False to result

        return result

         Time complexity: O(n) becasue we loo through each kid's candies exactly once.
         Space complexity: O(n) because we created an n array of booleans with equal size on candies.

      
        """
        # Brute Force Implemetationdef kidsWithCandies(candies, extraCandies):
        # result = []

        # for i in range(len(candies)):
        #     new_candies = candies[i] + extraCandies

        #     maximum = 0

        #     for j in range(len(candies)):
        #         if candies[j] > maximum:
        #             maximum = candies[j]

        #     if new_candies >= maximum:
        #         result.append(True)
        #     else:
        #         result.append(False)

        # return result

        # Optimize Approach Implementation
        result = []

        maximum_candy = max(candies)

        for candy in candies:
            new_candies = candy + extraCandies

            if new_candies >= maximum_candy:
                result.append(True)
            else:
                result.append(False)

        return result
