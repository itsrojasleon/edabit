# Letters Shared Between Two Words
# https://edabit.com/challenge/wvuk7d2mWgZEmFFYD

def shared_letters(txt1, txt2):
  c = ""
	for w in txt1:
		if w in txt2 and not w in c:
			c += w
	
	return len(c)
