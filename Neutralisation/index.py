# Neutralisation
# https://edabit.com/challenge/3wLZvWf4sFerNQmo7

def neutralise(s1, s2):
	a=''
	for i in range(len(s1)):
		if s1[i]=='+' and s2[i]=='+':
			a+='+'
		if s1[i]=='-' and s2[i]=='-':
			a+='-'
		if s1[i]=='+' and s2[i]=='-':
			a+='0'
		if s1[i]=='-' and s2[i]=='+':
			a+='0'
	return a
