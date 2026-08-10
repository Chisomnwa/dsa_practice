import heapq

from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        Input: We recieve two things
        - nums: an array of strings
        - int: tells us which largest number wwe want

        for example:
            nums = [3" "6", "7", "10"]
            k = 4

        Sorted from largest to smallest

        10,  7,  6,  3
         |   |   |   |
        1st 2nd 3rd 4th

        So, the 4th largest is 3, so we return "3".

        - Output: return the string represenying the kth largest number

        - Goal: Return the k largest inteher in nums, while returning it as a string.

        - Edge Cases:
            1. Only one number
            e.g nums = ["5"], k = 1 -> return "5"

            2. k is the length of the array, then we need the smalllest number
            e.g nums = ["3", "6", "7", "10"], k = 4

            3. Duplicate numbers
            e.g nums = ["2"., 2", "1"], k = 2 -> return 2

            4. very larg e numbers
            nums = ["9999999999999999999", "2"] -> we must compare them as integers, not lexicographycally as strings.

        - - -
        # Brute force Approach

        ## Intuition
        The most straighforward thing to do is:
        1. Convert the strings to integers.
        2. sort from largest to smallest
        3. Pick the (k - 1)th element
        4. Convert it back to string

            For example:

            ["3", "6", "7", "10"]
                     |
            [3, 6, 7, 10]
                     |
            [10, 7, 6, 3]
                    |
            k = 4 -> index 3
                    |
                    3
                    |
                   "3"

        ## Pseudocode
        function kthLargestNumber(nums, k):
            convert every number from string to integer

            sort the numbers in descending order

            answer = numbers[k - 1]

            return answer as a string

        # Brute Force Code Implementation
        nums = [int(num) for num in nums]

        nums.sort(reverse=True)

        answer = nums[k-1]

        return str(answer)
        
        Time complexity: 0(n log n) - converting the numbers is O(n), then sortin g n numbers costs O(n log n).
        Space complexity: O(n) because we created/stored the converted integers (and Python's sorting also uses extra space internally)

        - - -

        # Optmized (Min Heap) 
        
        ## Intuition
        1. Convert each string to an integer
        2. Keep a min-heap of size k
        3. For every number:
            - Add iot to the heap
            - If the heap grows biger than k, remove the smalllest
        4. At the end, the smallest number inside our heap is the kth largest overall.

        for example:
            nums = ["3", "6", "7", "10"], k = 2

            As we process:
            3 -> [3]
            6 -> [3, 6]
            7 -> [6, 7] -> remove 3
            10 -> [7, 10] -> remove 6

            The heap now contains the 2 largest numbers, [7, 10]

            Therefore: heap[0] == 7

        ## Pseudocode:
        create empty minheap

        for each number in nums:
            convert number to integer
            push number into heap

            if heap size > k:
                remove smalllest number

        return the smallest number in heap
        """
        heap = []

        for num in nums:
            num = int(num)
            heapq.heappush(heap,  num)

            if len(heap) > k:
                heapq.heappop(heap)

        return str(heap[0])
