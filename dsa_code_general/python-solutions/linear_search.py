# Implementation of Linear Search

def linear_search(list, target):
    '''
      This fucntion finds the index position of the target value,
      else returns none 
    '''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


num = [1,2,3,4,5,6,7,8,9, 10]
target = 12
result = linear_search(num, target)
verify(result)

num = [1,2,3,4,5,6,7,8,9, 10]
target = 6
result = linear_search(num, target)
verify(result)

'''
# TIME COMPLEXITY : O(n)
The loop runs from 0 to len(n) - 1, 
in the worst case, the target is at the last position or not in the list at all

So, it checks every element once -> proporttional to n

Best case: O(1) - target is the first element
Worst case: O(n)

Over all complexity: O(n)

# SPACE COMPLEXITY : O(1)
No extra data structures were created, and memory does not grow with input size.
'''