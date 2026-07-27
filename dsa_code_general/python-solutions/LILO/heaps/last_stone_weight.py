from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Input:
        - A list of integres; stones
        - Each integer represents the weight of a stone

        Output: Return one integer
        - which is the weight of the last remaining stone
        - 0 if all stones are destroyed

        Goal: Repeatedly
        1. Find two heaviest stones
        2. Smash them
        3. If they're equal, remove both
        4. Otherwise, insert their difference back
        5. Continue until at most one stone remains

        Edge cases:
        - only one stone
            e.g [5] -> return 5

        - all stones destroy each other
            e.g [2, 2] -> return 0

        - many equal stones
            e.g [3,3,3,3] -> return 0

        Pattern:
        This is a max-heap problem because on every turn I need to efficiently remove the two
        largest elements and possibly insert a new one. A max-heap gives me those operations in 0(log n) time.

        Walkthrough:
        Example:

        stones = [2, 7, 4, 1, 8, 1]

            largest stones = 8 and 7

            Smash: 8 -7 = 1

        stones = [2, 4, 1, 1, 1]

            largest elements = 2 and 4

            Smash: 4 - 2 = 2

        stones = [2, 1, 1, 1]

            largest elements = 2 and 1

            Smash = 2 -1 = 1

        stones = [1, 1, 1]

            largest: 1 and 1

            Smash = 1-1 = 0

        stones = [1]

        Return 1

        - - -
        Brute Force Approach:

        We do not worry about heaps yet. We repeat these steps until there's no stone left:
        1. Sort the array
        2. Remove the largest two elements
        3. If they're different, insert their difference back into the array
        4. Repeat

        Pseudocode:

        While there is more than one stone:
            sort the stones

            Remove the largest element (y)

            Remove the second largest element (x)

            if x != y:
                Add (y -x) back to the stone

        If no stones remain:
            return zero

        Otherwise:
            Return the remaining stone

        Time Complexity: O(n^2 log) in the worst case scenarion
            - You sort the list (O(n log n)) at almost every iteration
            - There can be up to n - 1 iterations

        Space complexity: O(1)ignoring the sorting algorithm's internal space since you're modifying thelist in place
        
        - - -
        Optimized Approach

        Key Insight:
        Every turn, the problem asks us to do exactly two things:
        1. Find the largest stone
        2. Find the second largest stone

        If we keep the stones in a normal array, finding the largest stones costs O(n) every round.

        A max Heap is designed exactly for this:

        - Get the largest -> O(1) to peek, O(log n) to remove
        - Insert the new stone -> O(log n)

        That's why this is a heap problem
        
        Suppose we have:

        stones = [2,7,4,1,8,1]

        Step 1: Build a Max Heap

                      8
                    /   \
                   7     4
                  / \   /
                  1  2  1
        
        Step 2: 
        
        Extract the largest: 8, 7
        Smash them: 8 - 7 = 1

        Heap = [2, 4, 1, 1, 1]

        Extract the largest: 4, 2
        Smash them: 4 - 2 = 2

        Heap = [2, 1, 1, 1]

        Extract the largest: 2, 1
        Smash them: 2 - 1 = 1

        Heap = [1, 1, 1]

        Extract the largest: 1, 1
        Smash them = 1 - 1 = 0

        Heap = [1]

        Return 1

        Pseudocode:
        Build a max heap from the stones

        while heap has more than one stone

            first = remove largest
            second = remove second largest

            if first != second
                insert(first - second)

        if heap is empty
            return 0

        return remaining stone

        Time complexity: Building the heap: O(n)
            - Each smash:
                - 2 removals -> O(log n)
                - 1 insertion -> O(log n)

        There can be at most n - 1 smash operations. S, overall: O(n log n)

        Space complexity: O(n) because the heap stores all the stones.
        """

        # # Brute force Python Implementation
        # while len(stones) > 1:
        #     stones.sort()

        #     y = stones.pop()
        #     x = stones.pop()

        #     if x != y:
        #         stones.append(y - x)

        # if stones:
        #     return stones[0]

        # return 0

        #  Optimized approach Python Implementation
        import heapq

        # Convert to a max heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))

        if heap:
            return -heap[0]

        return 0
