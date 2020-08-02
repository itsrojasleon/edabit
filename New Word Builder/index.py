# New Word Builder
# https://edabit.com/challenge/R5F99DeuhqYxbGyMM

def word_builder(ltr, pos):
	str = ''
	for i in pos:
		str += ltr[i]
	
	return str
