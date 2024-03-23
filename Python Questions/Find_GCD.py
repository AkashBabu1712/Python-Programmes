'''
Program to Find GCD or HCF of Two Numbers

Note: The GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them. 

Input: a = 20, b = 28
Output: 4
Explanation: The factors of 20 are 1, 2, 4, 5, 10 and 20. The factors of 28 are 1, 2, 4, 7, 14 and 28. Among these factors, 1, 2 and 4 are the common factors of both 20 and 28. The greatest among the common factors is 4.

'''

#1: Naive Approach

# Function to find gcd of two numbers
# def gcd(a, b):

# 	# Find minimum of a and b
# 	result = min(a, b)

# 	while result:
# 		if a % result == 0 and b % result == 0:
# 			break
# 		result -= 1

# 	# Return the gcd of a and b
# 	return result


# # Driver Code
# if __name__ == '__main__':
# 	a = 98
# 	b = 56
# 	print(f"GCD of {a} and {b} is {gcd(a, b)}")

#output: GCD of 98 and 56 is 14


#2. Euclidean approach

# Python program to find GCD of two numbers


# Recursive function to return gcd of a and b
def gcd(a, b):

	# Everything divides 0
	if (a == 0):
		return b
	if (b == 0):
		return a

	# Base case
	if (a == b):
		return a

	# a is greater
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)


# Driver code
if __name__ == '__main__':
	a = 98
	b = 56
	if(gcd(a, b)):
		print('GCD of', a, 'and', b, 'is', gcd(a, b))
	else:
		print('not found')

