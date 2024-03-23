'''
Given an array of integers nums and an integer
target, return indices of the two numbers such
that they add up to target.

Testcase #1.
6 1 2 3
nums = [ 2, 7, 11, 15 ]
target = 9
O/p: [0,1]

Testcase #2.
012
nums = [ 3,2,4]
target = 6
O/p: [1,2]

'''
def two_sum_hashing(nums, target):
    # Create a dictionary to store the elements and their indices
    num_dict = {}

    for i in range(len(nums)):
        # Get the complement using the target value
        complement = target - nums[i]

        # Search the dictionary for complement, if found, we got our pair
        if complement in num_dict:
            return [num_dict[complement], i]

        # Put the element in dictionary for subsequent searches.
        num_dict[nums[i]] = i

    # If no solution found, raise an exception
    raise ValueError("No two sum solution")


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum_hashing(nums, target)
print("Indices:", result[0], ",", result[1])

