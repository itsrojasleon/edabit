# Emphasise the Words
# https://edabit.com/challenge/K5277r6RmsJRSz27t

def emphasise(txt):
	s=''
	for w in txt.split(' '):
		s+=w.capitalize() + ' '
	
	return s.strip()
