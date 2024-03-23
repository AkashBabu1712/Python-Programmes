'''
Find the Missing Number:

Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

Note: There are no duplicates in the list.

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
'''

# def find_missing_number(arr):
#     n = len(arr) + 1
#     total_sum = n * (n + 1) // 2  # Sum of first N integers

#     array_sum = sum(arr)  # Sum of the given array

#     missing_number = total_sum - array_sum

#     return missing_number

# # Example usage:
# arr = [1, 2, 4, 6, 3, 7, 8]
# print("Missing number:", find_missing_number(arr))

####################################################################

# Find Missing Element
def findMissing(arr, N):
  
    # create a list of zeroes
    temp = [0] * (N+1)

    for i in range(0, N):
        temp[arr[i] - 1] = 1

    for i in range(0, N+1):
        if(temp[i] == 0):
            ans = i + 1

    print(ans)

# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)

    # Function call
    findMissing(arr, N)
