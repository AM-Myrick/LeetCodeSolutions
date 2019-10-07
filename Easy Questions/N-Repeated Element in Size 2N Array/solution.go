package main

func repeatedNTimes(A []int) int {
	// creates a map with int keys and values
	elements := make(map[int]int)

	// only one element repeats
	// so we can immediately return upon finding an existing key
	for i := 0; i < len(A); i++ {
		num := A[i]
		if _, ok := elements[num]; ok {
			return num
		} else {
			elements[num] = 1
		}
	}
	// if there's no repeating element, return -1
	return -1
}
