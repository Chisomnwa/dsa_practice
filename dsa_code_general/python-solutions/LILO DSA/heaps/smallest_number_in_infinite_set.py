import heapq

class SmallestInfiniteSet:
    """
    Input: {1, 2, 3, 4, 5, 6, ...}

    And we have two operations:
    - popSmallest() -> remove and return the smallest available number.
    - addBack(num) -> put num back if it isn't already in the set.

    Output:
    - popSmallest() returns an integer
    - addBack() returns nothing

    Goal: need to make both operations efficient especially because the set is conceptually inifinite.

    Important observation: The set starts with every positive integer

    So initially:
    
        1, 2, 3, 4, 5, 6, 7, ...
        |
    smallest

    When we pop:
    popSmallest() -> 1

        2, 3, 4, 5, 6,...
        |
    smallest

    Then:
    popSmallest() -> 2

        3, 4, 5, 6, ...
        |
    smallest

    But, if we later do:
    addBack(1)

    then:
        1, 3, 4, 5, 6, ...
        |
    smallest

    The key challenge is:
    How do we efficiently keep track of numbers that were removed and then added back, while also continuing through the infinite sequence?

    Constraints:
    - num is at most 1000
    - At most 1000 operations total

    Those constraints are small, but the infinite set is the importatnt part - you obviously can't actually create [1, 2, 3, ...]
    """
    def __init__(self):
        self.next_num = 1 # -> the smallest untouched number is initially 1
        self.min_heap = [] # -> this wil eventually hold numbers that were removed and then added back

    def popSmallest(self) -> int:
        """
        The key decision: is the smallest number the next untouched number, or is there
        a smaller number waiting in our min-heap? So, we'll eventually use heapq and compare the two.
        """
        if self.min_heap and self.min_heap[0] < self.next_num:
            return heapq.heappop(self.min_heap)

        smallest = self.next_num
        self.next_num += 1
        return smallest

    def addBack(self, num: int) -> None:
        """
        Put num into the min-heap only if it has actualy been removed already.
        """
        if num < self.next_num and num not in self.min_heap:
            heapq.heappush(self.min_heap, num)
