def merge_sort(list):
    '''
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide: find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n) time and O(n) space
    '''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Time complexity:
    Takes overall O(log n) time because we are splitling the
    main list into sublists and down to a single element list

    Space complexity:
    Takes O(n) space because we created two seperate lists
    '''

    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    '''
    Merges to lists (arrays), sorting them in the process
    Returns a new merged list.

    RUns in overalla O(n) time because for a list of n, we are 
    making a number of merge operations; sorting and merging 
    the single lists into sub lists and finally into one sorted and merged list
    '''

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1
    
    while i < len(left):
        l.append(left[i])
        i = i + 1

    while j < len(right):
        l.append(right[j])
        j = j + 1

    return l

# alist = [54, 26, 62, 23, 17, 77, 31]
# l = merge_sort(alist)
# print(l)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1: ])

alist = [54, 26, 62, 23, 17, 77, 31]
l = merge_sort(alist)

print(verify_sorted(alist))
print(verify_sorted(l))
