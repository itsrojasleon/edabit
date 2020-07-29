// Even Odd Partition
// https://edabit.com/challenge/9XtaD8onvPy6rgHdF

func evenOddPartition(_ arr: [Int]) -> [[Int]] {
	var odd: [Int] = []
  var even: [Int] = []

  for num in arr {
    if num%2 == 0 {
      even.append(num)
    } else {
      odd.append(num)
    }
  }

  return [even, odd]
}
