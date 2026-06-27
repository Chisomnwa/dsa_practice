class MyArrayList:
    def __init__(self, initial_capacity=10):
        """
        Initialize the ArrayList with an initial capacity.
        
        NOTE: In Python, instance variables and methods share the same namespace.
        To avoid 'shadowing' the size() method, use self._size for the counter.
        """
        self._size = 0  # Internal counter (The 'actual' size)
        self.capacity = initial_capacity
        self.data = [None] * self.capacity

    def add(self, element):
        """
        Add an element to the end of the ArrayList.

                  salt
                   |
        cabinet = [salt,pepper,_,_,_,_,_,_,_,_] -> capacity = 10, size = 1
                   0,     1,   2,3,4,5,6,7,8,9

        To add: pepper

        - check if there's anough space to add elements
            if there isn't enough space to addd an item -> resize the cabinet (double it)

        - place the new element into the next available slot
            - use size to correlate the index
            - add elemt to the list
            - increase size by +1
        """
        if self._size == self.capacity:
            self._resize()

        self.data[self._size] = element
        self._size += 1
 
    def insert(self, index, element):
        """
        Insert an element at the specified index.

        Add an element to the end of the ArrayList.

                  salt
                   |
        cabinet = [salt,paprika,parsely,_,_,_,_,_,_,_] -> capacity = 10, size = 3
                    0,     1,      2,  b3,4,5,6,7,8,9

        To add: oregano at index 1 -> [salt, oregano, paprika, parsely, _, _...]

        - check if everything is in bounds, if not raise error
            -> index is greater than 0 (no negative spaces)
            -> index is less than size

        - check if there's anough space to add elements
            if there isn't enough space to addd an item -> resize the cabinet (double it)

        - shift everything over one position to the right

        - insert element

        - increase size by +1
            
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
 
        if self._size == self.capacity:
            self._resize()
 
        for i in range(self._size, index, -1):
            self.data[i] = self.data[i - 1]
 
        self.data[index] = element
        self._size += 1
 
    def get(self, index):
        """
        Retrieve the element at the specified index.

                salt
                |
        cabinet = [salt,paprika,parsely,_,_,_,_,_,_,_] -> capacity = 10, size = 3
                    0,     1,      2,  b3,4,5,6,7,8,9

        To check: the item at index 1 -> [salt, oregano, oregano, paprika, parsely, _, _...]

        - check if everything is in bounds, if not raise error
            -> index is greater than 0 (no negative spaces)
            -> index is less than size

        - return element in index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self.data[index]
 
    def remove(self, index):
        """
        Remove the element at the specified index.

                salt
                |
        cabinet = [salt,parsely,_,_,_,_,_,_,_] -> capacity = 10, size = 2
                    0,     1,      2,   3,4,5,6,7,8,9

        To remove paprika -> [salt, oregano, oregano, paprika, parsely, _, _...]

        - check if everything is in bounds, if not raise error
            -> index is greater than 0 (no negative spaces)
            -> index is less than size

        - remove element from the given index - keep track of what is removed

        - shift everything to the left

        - update the size


        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
 
        removed = self.data[index]
 
        for i in range(index, self._size - 1):
            self.data[i] = self.data[i + 1]
 
        self._size -= 1
        return removed
 
    def size(self):
        """
        Return the current number of elements in the ArrayList.

        - return element in index
        """
        return self._size
 
    def is_empty(self):
        """
        Check if the ArrayList is empty.
        """
        return self._size == 0 # will either give true (for empty) and false (if not empty)
 
    def _resize(self):
        """
        Resize the internal array when capacity is reached.

        - store the double of our current capacity

        - create a new list with the capacity of double the current capacity

        - copy everything to the new list

        - set data to equal the new list

        - set the capacity equal to the new capacity
        """
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
 
        for i in range(self._size):
            new_data[i] = self.data[i]
 
        self.data = new_data
        self.capacity = new_capacity

# Example Usage (for testing)
# arr_list = MyArrayList()
# arr_list.add(5)