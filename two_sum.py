# # BRUTE FORCE APPROACH - O(n2)
# nums = [2, 7, 11, 15]
# target = 9

# def two_sum_bruteforce(nums, target):
#     """
#         We assume we don't know anything so we
#         check every possible pair and see if their
#         sum equals target.
#     """
#     for i in range(len(nums)):  # picking each number as the first number in the pair
#         for j in range(i + 1, len(nums)): # getting the next element 
#             if nums[i] + nums[j] == target: # if the first element and the next element equals target
#                 return [i, j] # return their index positions
#     return None
    
# if __name__ == "__main__":
#     print(two_sum_bruteforce(nums, target))


# DICTIONARY (HASH MAP) APPROACH - O(n)
def two_sum_hash(nums, target):
    """
        Finds the sum of consecutive numbers in an array
        that sum to a target.

        Args:
            nums: The input array list of numbers
            target: the rarget sum to find

        Returns a list of the consecutive numbers indices.
    """
    seen = {}

    for i in range(len(nums)): # loop through and get each number and their indices
        num = nums[i] # get the index positions of each element
        complement = target - num # get the number that will complement target

        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

    return None

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    print(two_sum_hash(nums, target))


