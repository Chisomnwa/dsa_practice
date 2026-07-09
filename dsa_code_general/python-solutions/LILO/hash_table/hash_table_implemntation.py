class Node:
    def __init__(self, key, value):
        """
        Initialize a Node with a key, value, and reference to the next node.
        """
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, initial_capacity=10):
        """
        Initialize the Hashtable with a fixed initial capacity.
        """
        self.capacity = initial_capacity
        self._size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        """Converts a key into a valid array index."""
        # Time complexity: O(1)
        hash_value = hash(key)
        index = hash_value % self.capacity
        return index

    def _resize(self):
        """Doubles capacity and re-inserts all existing nodes."""

        """
        Input: a hash map

        Output: a new hash map with size double that of the old has map

        Goal: When the load factor exceeds 0.75
            - Double the capacity
            - Create a new bucket array
            - Re-hash every existing node into the new array
            - Do not lose anyv data

        Why do we resize?

        The buckets might look like:
        0

        1 -> apple -> dog

        2 -> banana

        3 - orange

        There are now:
        _size = 4
        capacity = 4

        load_factor = 4/4 = 1.0

        Too many items:
        - Lots of collisions begin happening.
        - Instead of making thr linked lists longer, we double the bucket array

        Step 1:
        Old buickets:

        Capacity = 4

        0

        1 -> apple -> dog

        2 -> banana

        3 - orange

        Step 2:
        Create a new array

        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity

        Now:
        Cpacity = 8

        0
        1
        2
        3
        4
        5
        6
        7

        Everything is empty

        Step 3:
        Traverse every old bucket.

        For each bucket:
        current = bucket

        Step 4:
        Re-hash every key:

        Previously:
        hash(key) % 4

        Now:
        hash(key) % 8

        The bucket index may change

        Example:
        Aplle

        Old index = 1
        New index = 5

        So, you can't simply just copy the old linked lists.
        
        You must compute the new array index for every node.

        Step 5:
        Insert each node into the new bucket

        Exactly like put()

        current.next = new_buckets[new_index]
        new_buckets[new_index] = current

        Step 6:
        When every node has beeen moved:
        
        self.capacity = new_capacity
        self.buckets = new_buckets

        Pseudocode:
        Double the capacity.

        Create a new bucket array.

        For every old bucket:
            Traverse its linked list.

            For every node:
                Save the next node.
                Compute the new node index.
                Insert the node at the head of the new bucket

                Continue traversing

        Update capacity.
        Replace theold buckets.

        Time complexity : O(n) because every node is moved exactly once.

        Space complexity: o(n) because a new bucket array is allocated during resizing        
        """
        old_buckets = self.buckets

        self.capacity = self.capacity * 2
        self.buckets = [None] * self.capacity

        for bucket in old_buckets:
            curent = bucket

            while curent is not None:
                next_node = current.next

                index = self._hash(current, key)

                current.next = self.buckets[inde]
                self.buckets[index] = current

                current = next_node

    def put(self, key, value):
        """Add or update a key-value pair."""

        """
        - update the value if the key already exists.
        - Insert a new node if the key doesn't exist.

        Walkthrough

        Suppose in bucket 3, we have:

        buckets[index]
             |
        ("apple", 5)
             |
        ("banana", 7)
             |
            None
        - - - 

        Case 1 - Update existing key

        Say we call : put("banana", 100)

        We traverse:
        apple
          |
        banana

        Update:  banana.value = 100

        Result:
        ("apple", 5)
            |
        ("banana", 100)

        - No increasing size
        - No creating of new node
        - Return

        - - -

        Case 2: Insert a anew array

        Say we call : put("orange", 9)

        We traverse:
        apple
          |
        banana
          |
        None

        Key isn't found

        create a new node:
        new_node = Node("orange", 9)

        insert it at the head:

        Before:

        buckets[index]
             |
        ("apple", 5)
             |
        ("banana", 7)

        After:

        buckets[index]
             |
        ("orange", 9)
              |
        ("apple", 5)
              |
        ("banana", 7)

        Increament:
        self._size += 1

        Then, check the load factor:
        self._size / self.capacity

        If it's greater than 0.75:
        self._resize()

        Pseudocode:
        Find the bucket index.

        Traverse the linked list.

        if the key exists:
            Update its value
            Return

        Create a new node.

        Point the new node to the current head.

        Make the new node the new head.

        Increament size

        If load factor > 0.75:
        Resize()

        Time complexity:
            - Average : O(1).
            - Worst case: O(n) many collisions.

        Space complexity:
            - O(1) (excluding the occasional O(n) work done during resize()).
        """
        index = self._hash(key)
        current = self.buckets[index]

        # Update existing key 
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current =current.next
        
        # Insert new key at the head
        new_node = Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self._size += 1

        # Resize if the load factor exceeeds 0.75
        if self._size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        """Retrieve the value for a key. Returns None if not found."""
        
        """
        Goal: Return the value associated with key.
              If the key doesn't exists, return None.

        Walkthrough:
         0 -> None
                
         1 -> ("cat", 5)
                |
              ("dog", 8)
                |
              ("apple", 12)
                |
               None

        (A) Suppose we call -> get("dog")

        1. Find the bucket
            index = self._has("dog")
            Suppose: index = 1

        2. Start traversing

        current
            |
        ("cat, 5)

        is "cat" == "dog" -> No

        Move to the next node.

        current
            |
        ("dog", 8)

        is "dog" == "dog -> Yes

        Return 8

        (B) Suppose we serach for: get("banana")

        1. Find the bucket.
        2. We traverseand see if we will find "banana" at that bucket index.

           cat
            |
           dog
            |
          apple
            |
           None

        We reached None without finding "banana"

        Return None

        - - -

        Pseudocode:

        Find the bucket index

        Set current to the head of the bucket

        While current is not None:
            if current.key == key:
                return current.value

            Move current to current.next

        Return None
        """
        # Time complexity: O(1) because we just head straight to the index position and 
        #                  get the value if it exists or None if otherwise.
        # Space complexity: O(n) because no extra data structure was created.
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return currrent.value
            current = current.next

        return None

    def remove(self, key):
        """Remove a key-value pair. Returns the removed value, or None if not found."""

        """
        Input: key that should be removed from a hash table.

        Output:
            - Modifies the hash table with the specified key-value pair removed
            - Raises KeyError if the key is not found

        Goal:
            - Remove the key-value pair with the given key from the hash table.
            - if the key exists, update the chain and decreament the size.
            - if the key does not exist, raise a KeyError.

        Walkthrough:

        Suppose bucket 3 contains:

        bucket[3]

        buckets[index]
          |
        ("orange", 9)
          |
        ("apple", 5)
          |
        ("banana", 7)
          |
        None


        case 1: Remove the head
        remove("orange")

        Before:

        buckets[index]
          |
        orange
          |
        apple
         |
        banana

        After:

        buckets[index]
         |
        apple
         |
        banana

        We simply do:
        self.buckets[index] = current.next

        - - -

        Case 2: Remove a middle node

        remove("apple")

        Before:

        buckets[index]
         |
        orange
         |
        apple
         |
        banana

        We keep two pointers:

        prev       current
          |           |
        orange------->apple

        Delete by stitching:
        prev.next = current.next

        Result:
        orange
          |
        banana

        - - - 

        Case 3: Remove the last node
        remove("banana)

        Before:
        orange
          |
        apple
          |
        banana


        After:

        orange
         |
        apple

        Delete by stitching:
        prev.next = current.next

        Since current.next is None, the last node is removed.

        ---

        Case 4: Key not found

        Traverse until:

            Current -> None

        raise KeyError(key)

        - - -
        Pseudocode:
        Find the bucket index

        current = head of that bucket
        prev = None

        while current exists:
            if current.key = key:

                if removing the head:
                    buckets[index] = current.next

                Else:
                    prev.next = current.next

                Decrement size

                Return

            Moveprev forward
            Move current forward

        Raise KeyError

        Time complexity
        - Average: O(1)
        - Worst case: O(n)

        Space compolexity:
        - O(1)
        """
        index = self._hash(key)

        current = self._buckets[index]
        prev = None

        while current is not None:

            if current.key == key:

                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next

                self._size -= 1
                return

            prev = current
            current = current.next

        raise KeyError(key)

    def size(self):
        """Return the number of key-value pairs."""
        return self._size

    def is_empty(self):
        """Check if the hashtable is empty."""
        return self._size == 0
