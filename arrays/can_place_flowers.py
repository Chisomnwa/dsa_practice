class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Input:
        - flowerbed : a list of integers containing 0's and 1's
            - O's are empty plot in the flowerbed
            - 1's are nin-rmpty plots in the flowerbed (contains flowers)

        - n: an interger i.e the numbe rof flowers we can plant in the flowerbed plots.

        Output: to return a boolean:
        - True if we can plan n flowers without having flowers adjacent to each other 
        - False otherwise

        Goal: to return True if we plant flowers and have no flowers planted adjacent to each other, and False otherwise.

        eg.

        flowerbed = [1, 0, 0, 0, 1] and n = 1
                        ⬇
        flowerbed = [1, 0, 1, 0, 1] which is valid.

        Edge  cases:
        1. When n = 0:
            eg. flowerbed = [1, 0, 0] and n = 0
                We are being asked to plant zero flowers -> return True

        2. When we have a single empty plot.
            e.g flowerbed = [0] and n = 1 
                flowerbed = [1] -> return True

        3. When we have a single non-empty plot.
            e.g flowerbed = [1] and n = 1
            There is no space to plant the new flower -> return False

        4. When we have all empty plots
            e.g flowerbed = [0, 0, 0, 0, 0] and n = 3
                flowerbed = [1, 0, 1, 0, 1] -> return True

        5. When there's enough space
            e.g flowerbed = [1, 0 0, 0, 1] and n = 2
            But we can only plant 1 -> return False

        Walkthrough:

        flowerbed = [1, 0, 0, 0, 1] and n = 1

                [1, 0, 0, 0, 1]
                 0  1  2  3  4
                 ↑

        At index[0] -> already contains a flower -> can't plant
        At index[1] -> has an empty plot, but left neighbor is planted -> can't plant
        At index[2] -> has an empty plot, left & right neighbors are empty -> plant
        
        And we've planted everything we needed -> return True

        - - -

        Brute Force Approach

        Intution:
        We can use a very natural greedy simulation approach.

        We scan from left to right and at each plot, we ask:

        "Can I plant a floer here?"

        With that approach, we plant flowers as early as possible and that is okay because 
        a flower we plant at the current position only blocks its immediate neighbors and we've already passed the left neighbor.

        Algorithm:
        For every index i:

        1. check whether flowerbed[i] == 0
        2. Check left neighbor
            - either i is the first position or flowerbed[i - 1] == 0
        3. Check right neighbor
            - either i is the last position or flowerbed[i + 1] == 0
        4. if all three conditions are satisfied:
            - plant a flower : flowerbed[i] = 1
            - decrease n
        5. If n becomes 0, return True
        6. After checking everything, return whether == 0

        Pseudocode:
        For each i in flowerbed

            if flowerbed[i] == zero
                AND left plot is empty or doesn't exist
                AND right plot is empty or doesn't exist

                plant a flower
                decrease n by 1

                if n == 0
                    return True

        return False
        
        Time complexity: O(n) because we may scan every plot once.
        Space complexity: O(1) because we only crete constant variables and modify the array in place.

        - - -

        Optimized approach:
        The above approach is already an optimized approach in terms of time complexity.
        We have to potentially look at every plot, so we can't do better that O(n) time.

        So, I'll scan the flowerbed from left to right. At each empty plot, I'll check whether both neighbprs are empty, treating the boundaries as empty. If the position is valid, I'll plant a flower there and decreament n. Planting greedily from left to right is safe because a newly planted flower only affects its immediate neighbors, and we've already processed the left side. If n reaches zero, I'll return True, otherwise., after the scan, I'll return False.
        """
        if n == 0:
            return True

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True
                
        return False
