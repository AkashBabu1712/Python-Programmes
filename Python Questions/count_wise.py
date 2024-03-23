'''
Climbing Stairs to reach at the top.

There are n stairs, a person standing at the bottom wants to climb stairs to reach the nth stair. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.

Input: n = 1
Output: 1 There is only one way to climb 1 stair

Input: n=2
Output: 2 There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5 (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

'''

#1. Using recursion -- ways(n) = ways(n-1) + ways(n-2) ---> as fibonacci
# ways(1) = fib(2) = 1
# ways(2) = fib(3) = 2
# ways(3) = fib(4) = 3

# Python program to count
# ways to reach nth stair

# Recursive function to find
# Nth fibonacci number


def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

# Returns no. of ways to
# reach sth stair


def countWays(s):
	return fib(s + 1)


# Driver program
s = int(input('Enter your number: '))
print ("Number of ways = ",countWays(s))


#2. Math approch
# n = 5

# print("Number of ways when order "
# 	"of steps does not matter is : ", 1 + (n // 2))









