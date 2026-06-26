class Node:
    def __init__(self, data=None):
        """
        Initialize a Node with data and a reference to the next node.
        """
        self.data = data    # Store the actual data
        self.next = None    # Pointer to the next Node object (None by default)

    def __repr__(self):
        """
        Helper to print the Node's data instead of its memory address.
        """
        return f"Node({self.data})"

class MyLinkedList:  # UPDATED: Matches the write-up name
    def __init__(self):
        """
        Initialize the LinkedList with head, tail, and size.
        """
        self.head = None
        self.tail = None    # UPDATED: Required for O(1) adds to end
        
        # INSTRUCTOR NOTE: We use _size (underscore) to store the data 
        # so it does not conflict with the size() method below.
        self._size = 0      

    def add(self, element):
        """
        Add an element to the end of the LinkedList.
        Updates tail and size.
        """
        newNode = Node(element)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self._size += 1

    def insert(self, index, element):
        """
        Insert an element at the specified index.
        Valid indices: 0 to size (inclusive).
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        newNode = Node(element)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            if self._size == 0:
                self.tail = newNode
        elif index == self._size:
            self.tail.next = newNode
            self.tail = newNode
        else:
            prev = self.head
            for _ in range(index -1):
                prev = prev.next
            newNode.next = prev.next
            prev.next = newNode

        self._size += 1

    def get(self, index):
        """
        Retrieve the element at the specified index.
        Valid indices: 0 to size-1.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next

        return current.data


    def remove(self, index):
        """
        Remove the element at the specified index.
        Returns the removed element.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        removed_data = None

        if index == 0:
            # Removing the head
            removed_data = self.head.data
            self.head = self.head.next
            # If we removed the only element, tail must also become None
            if self._size == 1:
                self.tail = None
        else:
            # For any other index, traverse to the node before target
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next

            removed_data = prev.next.data
            prev.next = prev.next.next

            # If we just removed the last element, update tail
            if index == self._size - 1:
                self.tail = prev

        self._size -= 1
        return removed_data

    def size(self):
        """
        Return the current number of elements in the LinkedList.
        """
        return self._size

    def is_empty(self):
        """
        Check if the LinkedList is empty.
        """
        return self._size == 0

# Example Usage (for testing)
ll = MyLinkedList()
ll.add(5)
ll.add(10)

ll.insert(1, 7)

print(ll.get(1))
## print(ll.get(5)) - should return index out of range error (if the list doesn't have a node at that index position)

print(ll.remove(1))
print(ll.size())
#print(ll.data())