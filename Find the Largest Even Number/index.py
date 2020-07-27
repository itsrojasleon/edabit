# Find the Largest Even Number
# https://edabit.com/challenge/ksZrMdraPqHjvbaE6

# Write a function that finds the largest even number in a list. Return -1 if not found. 
# The use of built-in function max() is prohibited.

def largest_even(lst):
  	n = -1
	for i in range((len(lst))):
		if (lst[i] > n and lst[i]%2==0):
			n = lst[i]
	return n
