# Seven Boom!
# https://edabit.com/challenge/BokhFunYBvsvHEjfx

def seven_boom(lst):
  for n in lst:
	  if "7" in str(n):
	    return "Boom!"
      
  return "there is no 7 in the list"
