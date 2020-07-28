# All Occurrences of an Element in a List
# https://edabit.com/challenge/jwzgYjymYK7Gmro93

def get_indices(lst, el):
	result = []
	for idx, item in enumerate(lst):
		if (item == el):
			result.append(idx)

	return result
