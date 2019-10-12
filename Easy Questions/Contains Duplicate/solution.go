package main

func containsDuplicate(nums []int) bool {
	// create a map of structure {int: int}
	// loop over nums and add each num to the map
	// if there's a collision, return true
	// else return false
	copy := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if _, ok := copy[num]; ok {
			return true
		}
		copy[num] = 0
	}
	return false
}
