# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
      """
      input: a singly linked list

      head
        |
        ▼
        [1] -> [0] -> [1] -> None

      - each node contains either 1 or 0,
      - and the linked list itself represents a binary number
      - with the head being the most signicant bit

      output: return the decimal value of the number

      goal: to convert the binary number (base 2) to demimal (base 10)

      What's the process mathematically?

      A placed-value approach: This works if we already know the length or can look ahead

      head
        |
        ▼
        [1] -> [0] -> [1] -> None

      mathematically: [1] -> [0] -> [1] 
                    = (1 * 2^2) + (0 * 2^1) + (1 * 2^0)
                    = 4 + 0 + 1
                    = 5
      But, the place value approach will not always work in real world scenarion where we can have thousands of nodes.

      And since in linked list, we naturally move : head -> next -> next -> None

      from left to right.

      so, instead of calculating powers first, we build the number as we traverse.

      What i mean in essence: A binary number can be converted by taking each bit's place value, like done above. 
      However, since this is a linked list, I don't have direct access to the legth or indexes. I can process it 
      from left to right and build the decimal value as I traverse. Every time I see a new bit, I shift the current 
      number left by one binary poistion, which is equivalent to multiplying by 2, then add the new bit.

      Also, I traverse from left to right because the head contains the most significant bit.

      Walkthrough with an example:
      result = 0 -> stores the decimal value of the binary number built so far.
                    we keep updating it as we traverse the linked list until it becomes final.

      current = head

      head
        |
        ▼
        [1] -> [0] -> [1] -> None

      result = previous decimal value (result) * 2 + current bit

      result = 0 * 2 + 1 = 1

      binary so far: 1₂ = 1
      - - -

      current = current.next

              |
              ▼
      [1] -> [0] -> [1] -> None

      result = 1 * 2 + 0 = 2

      binary so far: 10₂ = 2
      - - -

      current = current.next.next

                    |
                    ▼
      [1] -> [0] -> [1] -> None

      result = 2 * 2 + 1 = 5

      binary so far: 101₂ = 5

      - - -
      return 5

      is this initial approach efficient?

      other possible approach could be:
      - traverse the linked list
      - store bits in an array
      - convert array to binary

      but that would be O(n) space and O(n) time.

      Pseudocode:
      result = 0

      current = head

      while current exists:
          result = result * 2 +  bit
          move to the next node
      return result
      """
      result = 0

      current = head

      while current:
        result = result * 2 + current.val
        current = current.next
      return result
