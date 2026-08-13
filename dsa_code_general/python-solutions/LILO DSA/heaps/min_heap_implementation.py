class MinHeap:
    def __init__(self):
        """
        Initialize the MinHeap.
        Should store data in a dynamic list.
        """
        self.data = []

    def insert(self, value):
        """
        Insert a value and bubble it up to maintain the heap property.

        Input: A value to insert

        Output: None just modifies the heap in place

        Goal:
            - Add the value to the end of the array
            2. Restore the heap by bubbling it up (_heapify_up)

        Why append to the end?
        To preserve the Complete binary tree property

        e.g say current heap is:
                 2
                / \
               5   8

        Array: [2, 5, 8]

        Say we insert 1:
                 2
                / \
               5   8
              /
             1

        The, we heapify up.

        walkthrough:
        self.data = [2, 5, 8]

        inert 1:
        array = [2, 5, 8, 1]

        Now, we call _heapify_up(3) because 1 is at insex 3

        After heapify: self.data = [1, 2, 5, 8]

        Pseudocode:
        Append the value to the end of the array
        Call the heapify_up using the last index

        Time complexity: O(log n)
            - Appending is O(1)
            - _heapify_up may travel from a leaf to the root

        Space complexity: O(1)
        """
        self.data.append(value)

        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        """
        bubbling up an inserted value or patient if it;s a critical case.
        i.e if it;s a lower value than the parent.

        Input: index (the position of the newly inserted element)

        Output: nothiing. The heap is just modified in place.

        Goal: restore the MinHeap property by moving the new value upward until 
        its paret is smaller (or it reaches the root).

        Edge cases: 
            - The new node is already the root (index == 0)
            - The parent os already smaller
            - The new node bubbles all the way to the root

        Walthrough:
        Suppose we have:
                 2
                / \
               5   8

        Array = [2, 5, 8]

        The we insert 1:

                 2
                / \
               5   8
              /
             1
        
        Array = [2, 5, 8, 1]

        current index = 3

        Step 1 = calculate the parent's index:
        (3 - 1) // 2 = 1

        so parent = 5, and 1 < 5

        So, you swap their positions.

        Then array becomes: [2, 1, 8, 5]

                 2
                / \
               1   8
              /
             5

        Step 2: calculate parent index

        current index = 1

        parent index = (1 - 1) // 2 =  0

        so parent is 2, and 1 < 2

        You swap their positions again.

        Array becomes = [1, 2, 8, 5]

                 1
                / \
               2   8
              /
             5

        Now, we've reached the root, and we stop.

        Algorithm;
        1. Start from the given index
        2. While the node is not the root:
            - Find its parent
            - If the current valiue is smaller than the parent
                - swap them
                - move to the parent's index
            - otherwise
                - stop

        Pseudocode:
        heapify_up(index)
            while index > 0
                parent = (i - 1) // 2

                if current value < parent value
                    swap them

                    index = parent

                else
                    stop

        Time complexity: 
            - in the worst case, the new element bubbles from the bottom to the root.
            - A complete binary tree has height O(log n).

        Space complexity: O(1) since only used variable parent and updated index
        """
        while index > 0:

            parent = (index - 1) // 2

            if self.data[index] < self.data[parent]:

                self.data[index], self.data[parent] = (self.data[parent], self.data[index])

                index = parent

            else:
                break
                



    def extract_min(self):
        """
        Remove and return the minimum value, bubbling the new root down.
        Raises IndexError when the heap is empty.

        Input: Noe

        Output: The smallest value in the heap ;.i.e the first and the most critical case 

        Goal: Remove the root(minimum value) repair the heap, and returne the removed value

        Edge cases:
            - Heap is empty -> traise an index error
            - Heap has one element 0-> remove and return it
            - Heap has many element -> repair the heap afterwards

        Walkthrough

        SSuppose heap is:
                 1
                / \
               2   8
              /
             5

        Array = [1, 2, 8, 5]

        Step 1: 
        Save the minimum because you will return it later:
        minimum = 1

        Step 2:
        Move the last lement to the root
                 5
                / \
               2   8

        Array = [5, 2, 8]

        Now, the heap property is broken because 5 < 2

        Step 3:
        Repair the heap by calling heapify_down()

        Now compare 5 with its children

        first comparism: 5 > 2, swap them.

        The tree becomes:

                 2
                / \
               5   8

        Array beconmes = [2, 5, 8]

        Heap is now restored, return 1.

        Algorithm:
        1. If heap is empty
            - raise IndexError
        2. Save the root
        3. Move the last element to the root
        4. Remove the last elemet
        5. Call _heapify_down(0)
        6. Return the saved minimum

        Pseudocode:
        etract_min()

            if heap is emooty:
                raise InedexError

        save root value

        move last element to root

        remove last elemet

        if heap is not empty
            heapify_down(root)

        return saved value

        Time complexity: 
        - Moving the last ement to the root: O(1)
        - pop() from the end: O(1)
        - _heapify_down: O(log n)

        So, overall : O(log n)

        Space complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Heap cannot be empty")

        minimum = self.data[0]

        self.data[0] = self.data[-1]

        self.data.pop()

        if not self.is_empty():
            self._heapify_down(0)

        return minimum

    def _heapify_down(self, index):
        """
        Move down the node until the Minheap property is restored.

        Input: Index - the node that may violate the MinHeap property (usually the root after extract_min())

        Ouput: None

        Goal: Move the node doen until the MinHeap property is restored.

        Edge cases:
            - Node has no children -> stop
            - Node hs only a left child -> compare only with the left child
            - Node is already smaller than both children -> stop

        Walkthrough:
        Suppose extract_min()

                 8
                / \
               2   5
              /
             7

        Array = [8, 2, 5, 7]

        the heap property is broken because. 8 > 2

        Step 1: current node = 8

        Children:
            - left = 2
            - right = 5

        Always choose the smaller child

        Smaller child = 2

        swap with the parent

        Tre becomes:
                 2
                / \
               8   5
              /
             7
            
        Array = [2, 8, 5, 7]
        
        Step 2: continue from where 8 moved

            - left = 7
            - right = None

        But 8 > 7, so swap again

                 2
                / \
               7   5
              /
             8

        Array = [2, 7, 5, 8]

        Step 3: 8 has no children, stop.
        Heap is restored.

        Algorithm:
        1. Start at the given index
        2. Find the left child
        3. Find the right child
        4. Find the smaller child
        5. If current > smaller child:
                - Swap
                - Continue from the child's index
        6. Otherwise stop

        Pseudocode:
        _hepaify_doen(index):

            while node has at least one child
                Smallest = current node

                    if left child exists and is smaller
                        smallest = left child

                    if right child exists and is smaller
                        smalest = right child

                    if smalllest is dtill current
                        stop

                    swap current with smallest

                    move to smallest child's index

        Time complexity: O(log n) because the node moves down at most one level at a time
        space complexity: O(1) becsuase no extra data structures, just a few values used.
        """
        while True:

            smallest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.data) and self.data[left] < self.data[smallest]:
                smallest = left
            
            if right < len(self.data) and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (self.data[smallest], self.data[index])

            index = smallest

    def peek(self):
        """
        Return the minimum value without removing it.
        Raises IndexError when the heap is empty.

        Pseudocode:
        if heap is empty:
            raise index error

        return the first element in the array

        Time complexity: O(1) becuase we just access index 0
        Space complexityt: O(1)
        """
        
        if self.is_empty():
            raise IndexError("Heap is empty")

        return self.data[0]

    def size(self):
        """
        Return the number of elements in the heap.

        Pseudocode:
        Return the number of elements in the heap.
        Time complexity: 0(1)
        Space complexty: 0(1)
        """
        return len(self.data)

    def is_empty(self):
        """
        Check if the heap is empty.

        Pseudocode:
        Return wether the heap has zeero elements.

        Time complexity: O(1)
        Space complexity: 0(1)
        """
        return len(self.data) == 0


"""
Interview explanation (concise):

insert() is O(log n) because after appending the new value in O(1), it may bubble 
up from the bottom to the root. A heap is a complete binary tree, so its height is 
log n. The node can move up at most one level per swap, giving a worst-case time complexity of O(log n).

_heapify_up() restores the MinHeap property after insertion. Starting from the newly
inserted node, it repeatedly compares the node with its parent. If the node is smaller, 
they are swapped, and the process continues upward. The operation stops when the parent 
is smaller or the root is reached. Since a heap's height is O(log n), the worst-case time 
complexity is O(log n), and the space complexity is O(1)

extract_min() removes the smallest element, which is always at the root. It saves the root 
value, replaces it with the last element to maintain the complete tree structure, removes 
the last element, and then calls _heapify_down() to restore the MinHeap property. Finally, 
it returns the saved minimum. The operation runs in O(log n) time because the replacement 
node may travel down the height of the heap, and uses O(1) extra space.

_heapify_down() restores the MinHeap property after removing the root. Starting from a given 
index, it repeatedly compares the current node with its children, swaps it with the smaller 
child if necessary, and continues downward until the current node is smaller than both children 
or reaches a leaf. It runs in O(log n) time and O(1) extra space.

One thing to remember:
Unlike _heapify_up(), which compares a node with its parent, _heapify_down() compares a node with 
both children and always swaps with the smaller child. Swapping with the larger child could 
leave the smaller child violating the MinHeap property.
"""