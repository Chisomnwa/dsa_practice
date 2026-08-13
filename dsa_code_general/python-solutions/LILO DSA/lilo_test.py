# ==========================================
# 🧪 STUDENT TESTING SANDBOX
# ==========================================
# Use this file to "stress test" your code before submitting.
#
# HOW TO USE:
# 1. Import your class (e.g., from arraylist import ArrayList)
# 2. Uncomment the example test function for your current project.
# 3. Add the function name to the 'USER_TESTS' list at the bottom.
# ==========================================

# --- 1. GENERIC TEST EXAMPLE (Start Here) ---
def test_generic_logic():
    """
    A simple example showing the 'Arrange, Act, Assert' pattern.
    """
    print("--- Running Generic Test ---")
    
    # 1. ARRANGE: Set up the variables
    expected_value = 10
    actual_value = 5 + 5
    
    # 2. ACT & ASSERT: Check if they match
    # Format: assert <condition>, <error_message>
    assert actual_value == expected_value, f"Math failed! Got {actual_value}"
    
    print("✅ Generic Test Passed!")


# --- 2. PROJECT-SPECIFIC EXAMPLES (Uncomment the one you need) ---

# 🔹 PROJECT 1: ARRAYLIST
# from arraylist import ArrayList
# def test_arraylist():
#     print("--- Testing ArrayList ---")
#     arr = ArrayList()
#     arr.add("A")
#     arr.add("B")
#     arr.add("C")
#     
#     assert arr.get(0) == "A", "Index 0 should be 'A'"
#     assert arr.size() == 3, "Size should be 3 after additions"
#     print("✅ ArrayList Passed!")

# 🔹 PROJECT 2: LINKED LIST
# from linked_list import LinkedList
# def test_linked_list():
#     print("--- Testing Linked List ---")
#     ll = LinkedList()
#     ll.append("Node1")
#     ll.append("Node2")
#     
#     # Assuming standard head/next structure
#     assert ll.head.value == "Node1", "Head should be Node1"
#     assert ll.head.next.value == "Node2", "Second node should be Node2"
#     print("✅ Linked List Passed!")

# 🔹 PROJECT 3: HASHTABLE
# from hashtable import Hashtable
# def test_hashtable():
#     print("--- Testing Hashtable ---")
#     ht = Hashtable()
#     ht.put("key", "value")
#     ht.put("key", "updated")  # Collision/Update check
#     
#     assert ht.get("key") == "updated", "Value should update on duplicate key"
#     assert ht.get("missing") is None, "Missing key should return None"
#     print("✅ Hashtable Passed!")

# 🔹 PROJECT 4: HEAP (Binary Heap)
# from heap import MinHeap  # Check your actual class name
# def test_heap():
#     print("--- Testing Heap ---")
#     h = MinHeap()
#     h.push(10)
#     h.push(5)
#     h.push(20)
#     
#     # In a MinHeap, pop() should return the smallest element (5)
#     assert h.pop() == 5, "Heap did not pop the smallest element first"
#     assert h.peek() == 10, "Next smallest should be at the top"
#     print("✅ Heap Passed!")

# My Own Min_Heap Test
from heaps.min_heap_implementation import MinHeap

def test_heap_milestone():
    print("--- Testing Heap Milestone 1 ---")

    # Arrange
    heap = MinHeap()
    heap.data = [1,5,2]

    # Assert
    assert heap.peek() == 1, "peak() should return 1"
    assert heap.size() == 3, "size() should rteurn 3"
    assert heap.is_empty() is False, "Heap should not be empty"

    print("✅  Heap milestone 1 is Passed!")

# 🔹 PROJECT 5: GRAPH
# from graph import Graph
# def test_graph():
#     print("--- Testing Graph ---")
#     g = Graph()
#     g.add_vertex("A")
#     g.add_vertex("B")
#     g.add_edge("A", "B")
#     
#     neighbors = g.get_neighbors("A")
#     assert "B" in neighbors, "Vertex B should be connected to A"
#     print("✅ Graph Passed!")

# 🔹 PROJECT 6: TRIE (Prefix Tree)
# from trie import Trie
# def test_trie():
#     print("--- Testing Trie ---")
#     t = Trie()
#     t.insert("apple")
#     t.insert("app")
#     
#     assert t.search("apple") is True, "Should find exact word 'apple'"
#     assert t.search("app") is True, "Should find prefix word 'app'"
#     assert t.search("ap") is False, "Should not find incomplete word 'ap' if not inserted"
#     print("✅ Trie Passed!")


# ==========================================
# 🚀 REGISTER YOUR TESTS HERE
# ==========================================
# Add your test function names to this list so the system runs them.
USER_TESTS = [
    test_generic_logic,
    # test_arraylist,
    # test_linked_list,
    # test_hashtable,
    # test_heap,
    test_heap_milestone
    # test_graph,
    # test_trie
]

if __name__ == "__main__":
    for test in USER_TESTS:
        test()