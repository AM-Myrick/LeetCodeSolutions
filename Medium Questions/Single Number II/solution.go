// https://leetcode.com/problems/single-number-ii/
package singlenumber

func singleNumber(nums []int) int {
	copy := make(map[int]int)
	// iterate over nums and count how many times
	// each num appears while adding its count
	// to copy
	for i := 0; i < len(nums); i++ {
		num := nums[i]

		if _, ok := copy[num]; !ok {
			copy[num] = 1
		} else {
			copy[num]++
		}
	}
	// find the only element with a value of 1
	// and return the key
	for k, v := range copy {
		if v == 1 {
			return k
		}
	}
	// return statement at end of func to satisfy linter
	return nums[0]
}
