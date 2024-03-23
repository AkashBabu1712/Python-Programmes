'''
Farthest distance of a 0 from the center of a 2-D matrix

Given a matrix of odd order mat, the task is to find the farthest distance of a 0 from the center of the matrix. Distance between two elements at locations (i1, j1) and (i2, j2) of the matrix is calculated as |i1- i2| + |j1-j2|. If no 0 occurs in the matrix then print 0 as the result.

Examples: 

Input: mat[][] = {{2, 3, 0}, {0, 2, 0}, {0, 1, 1}} 
Output: 2

Input: mat[][] = {{2, 3, 4, {0, 2, 0}, {6, 1, 1}} 
Output: 1

'''

# Python3 program to find the farthest distance
# of a 0 from the center of the matrix

n = 3

# function to return farthest distance
# of zero from center of the matrix
def farthestDistance(matrix):
	result = 0

	# traverse the matrix
	for i in range (0, n): 
		for j in range (0, n):
			if (matrix[i][j] == 0):
				result = max(result, abs(i - n // 2) +
									abs(j - n//2))
		
	# return result
	return result

# Driver Code
matrix = [[1, 2, 3], 
		[0, 1, 1],
		[0, 0, 0]]

print(farthestDistance(matrix))

