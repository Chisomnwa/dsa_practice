def find_sum(nums, target):
    """
        Finds the sum of consecutive numbers in an array
        that sum to a target.

        Args:
            nums: The input array list of numbers
            target: the rarget sun to find

        Returns a list of the consecutive numbers indices.
    """
    index_pos = []

    # iterate up to the second to last element
    # because the last element don't have a number to pair with
    for i in range(len(nums)-1):
        num_sum = nums[i] + nums[i + 1]

        # check if the consecutive numbers sum to target
        if num_sum == target:
            # we return their indices as a list
            return index_pos.append(nums[i], nums[i + 1])
        else:
            print("No matching number")


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    find_sum(nums, target)


