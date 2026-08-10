import heapq
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        Input:
        - nums: an array of integers
        - k: how many elements wwe must select

        for example:
        nums = [2, 1, 3, 3]
        k = 2

        Output: Return a subsequence of exactly k elements whose sum is as large as possible
        for example: 
            [3, 3]

        sum = 6

        Goal:Choose the k largest values from nums, but return them in their original order

        for example:
        nums = [-1, -2, 3, 4]
        k = 3

        The three kargest values are: -1, 3, 4

        And their original order in nums was stll -1, 3, 4

        Edge cases: 
        - k = 1 -> return the single largest element
        - k = len(nums) -> return the entire array
        - Negative numbers -> still choose the largest values, even if they are negative
            e.g nums = [-5, -2, -8]
                k = 2

            return [-5, -2]

        - Duplicate values -> duplicates are allowed and can both be selected

        - - -
        # Brute Force Approach
        ## Intuitiom
        1. Pair each number with its original index
        2. Sort these pairs by value from the largest to smallest
        3. Take the first k elements -nthese are the k largest values
        4. Sort those selected elements back by their original indices
        5. Return their values

        for example:
        nums = [2, 1, 3, 3], k = 2

        (index, value)
        (0, 2)
        (1, 1)
        (2, 3)
        (3, 3)

        Soer by value:
        (2, 3)
        (3, 3)
        (0, 2)
        (1, 1)

        Take the first 2:
        (2, 3), (3, 3)

        They are already in original order -> [3, 3]

        ## Algorithm:
        - Create pairs of (value, original_index)
        - sort pairs by value descending
        - Take the first k pairs
        - Sort those k pairs by original_index
        - Extract and return their values

        ## Pseudocode
        pairs = []

        for i, value in enumrate(nums):
            pairs.append((value, i))

        sort pairs by value descending

        selected = first k pairs

        sort selected by original index

        result = values from selected

        return result

        - - -
        # Optimized (Min-Heap Approach)
        ## Intuition
        1. Put (value, index) into the min-heap
        2. If the heap grows beyond k, remove the smallest value
        3. At the end, the heap contains the k largest elements
        4. Sort those k elements by their original indices to restore subsequence order
        5. Return their values

        ## Pseudocode:
        Create an empty min-heap

        For each value and index in nums:
            Add (values, index) to the heap

            If heap size > k:
                Remove the smallest value

        Now, the heap contains the k largest values

        Sort those k elemts by thir original index

        Extract their values

        Return the result

        """
        # # Brute Force Code Implementation

        # #1. store each number together with its original index
        # pairs = []

        # for i, value in enumerate(nums):
        #     pairs.append((value, i))

        # # 2. sort by value from largest to smallest
        # pairs.sort(reverse=True)

        # # 3. take the k largest elements
        # selected = pairs[:k]

        # # 4. put the selected elements back =in. their origginal order
        # selected.sort(key=lambda pair: pair[1])

        # # 5. extract just the values
        # result = []

        # for value, index in selected:
        #     result.append(value)

        # return result

        #########################################################
        # Optimized Approach Code Implementation
        heap = []

        for i, value in enumerate(nums):
            heapq.heappush(heap, (value, i))

            if len(heap) > k:
                heapq.heappop(heap)

        # Restore original porder
        heap.sort(key=lambda pair: pair[1])

        result = []

        for value, index in heap:
            result.append(value)
        
        return result
