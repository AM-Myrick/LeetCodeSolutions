// https://leetcode.com/problems/single-number-iii/
package main

func singleNumber(nums []int) []int {
	copy := make(map[int]int)
	result := make([]int, 0, 2)

	// iterate over nums and count how many times
	// each num appears while adding its count
	// to copy
	for _, num := range nums {
		if _, ok := copy[num]; !ok {
			copy[num] = 1
		} else {
			copy[num]++
		}
	}

	// find the elements with a value of 1
	// and add to result slice
	for k, v := range copy {
		if v == 1 {
			result = append(result, k)
			if len(result) == 2 {
				return result
			}
		}
	}
	// return statement at end of func to satisfy linter
	return result
}
