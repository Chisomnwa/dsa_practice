from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Input: 
        - points: a list of coordinate pairs
            e.g [[[x1, y1], [x2, y2], ...]]
        - k: the number of closest points we should return

        Output: return exactly k points that are closeest to the orign (0, 0).
            The order doesn't matter.

        Goal: Find the k closest points to the origin. Not the single closest.
            Not the distance. Return the actual points.

        Edge cases:
        - only point: [[5, 2]], k = 1
            return -> [[5, 2]]

        - k equals the number of points: [[1,2], [3,4]], k = 2
            return both

        - Negative coordinates
            still compute its distance normally

        Walkthrough

        Points = 
            [[3, 3],
             [5, -1],
             [-2, 4]]

        k = 2

        Find and compute each points distance from origin using √x^2 + y^2

        - (3, 3) = √18
        - (5, -1) = √26
        - (-2, 4) = √20

        The two smallest are √18 and √20

        So, we return [[3, 3], [-2, 4]]

        - - -
        Brute Force Approach:

        Intuition:
        We don't actually need a heap to solve this problem. Instead:
        1. Compute the distance of every point from the origin
        2. Store each distance together with its point
        3. Sort all the points by their distance
        4. Return the first k points

        This works because after sorting, the closest points will always be at the beginning.

        Walkthrough
         [[3, 3],
             [5, -1],
             [-2, 4]]

        k = 2

        Compute squared distance:
        - (3, 3) = √18
        - (5, -1) = √26
        - (-2, 4) = √20

        Pair each points with its distance:
        [
            (18, [3, 3]),
            (26, [5, -1]),
            (20, [-2, 4])
        ]

        Sort:
        [
            (18, [3, 3]),
            (20, [-2, 4]),
            (26, [4, -1])
        ]

        Take the first k = 2

        [[3, 3], [-2, 4]]

        Algorithm:
        1. Create an empty list called distances
        2. For every point
            - compute its squared distance: √x^2 + y^2
            - store (distance, point) in the list
        3. Sort the list by distance
        4. Create an empty answer list
        5. Take the first k points from the sorted list
        6. Return the answer

        Pseudocode:
        Create an empty list called distances

        for each point in points
            compute distance = x^2 + y^2
            store (distance, point) in distances

        Sort distances

        Create an empty result list

        For the first k elements in distances
            Add the point to result

        Return result
        
        Time complexity:
        - Compute distances: O(n)
        - Sort: O(n log n)
        - Take first k:  O(k)

        Overall: O(n log n)

        Space complexity: O(n) because we store every point with its distance

        -  - -
        Optimized approach

        Intuition: We only need the k closest points. Instead of:
        - calculating every distance
        - sorting all of them (O(n log n))

        We can use a MinHeap.

        The heap automatically keeps the point with the smallest distance at the top.
        Then, we simply remove the smallest point k times.

        Why do we know it's a heap problem? 
        Because the problem asks for: "the k closest".
        Whenever you hear:
        - k smallest
        - k largest
        - closest k
        - top k

        a heap should immediately come to mind.

        Algorithm:
        1. Create an empty minheap
        2. For every point
            - Compute its squared distance: x^2 + y^2
            - Push (distance, point) into the heap
        3. Repeat k times:
            - Pop the smallest distance from the heap
            - Add its point to the answer
        4. Return the answer

        Walkthrough:
        points = [[3,3], [5,-1], [-2,4]]
        k = 2

        Build the heap:
        Distances:
            (18, [3,3]),
            (26, [5,-1]),
            (20, [-2,4])

        Heap:
                18
               /  \
              26  20

        The exact internal array may differ, but the smallest distance is always at the root.

        First pop: (18, [3,3])
        Result: [[3,3]]

        The heap repairs itself.

        Second pop: (20, [-2,4])
        Result: [[3,3], [-2,4]]

        We've popped k = 2 points

        Return: [[3,3], [-2,4]]

        Pseudocode:
        Create an empty heap

        For every point:
            Compute its distance
            Push (distance, point) into heap

        Create an empty result list

        Repeat k times:
            Pop the smallest distance
            Add its point to the result

        Return result

        Time complexity: Build the heap: O(n log n)
        """
        # # Brute force implementation
        # distances = []

        # for point in points:
        #     x = point[0]
        #     y = point[1]

        #     distance = (x * x) + (y * y)
        #     distances.append((distance, point))

        # distances.sort()

        # result = []

        # for distance, point in distances[:k]:
        #     result.append(point)

        # return result

        # - - - - - - - -

        # Optimized apprach (MinHeap) implementation
        import heapq

        heap =  []

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (distance, [x, y]))

        result = []

        for _ in range(k):
            distance, point = heapq.heappop(heap)
            result.append(point)

        return result
