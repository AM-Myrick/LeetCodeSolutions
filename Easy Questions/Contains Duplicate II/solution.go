// Package containsduplicate2 - https://leetcode.com/problems/contains-duplicate-ii/
package containsduplicate2

func containsNearbyDuplicate(nums []int, k int) bool {
	copy := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if val, ok := copy[num]; ok {
			if i-val <= k {
				return true
			} else {
				copy[num] = i
			}
		} else {
			copy[num] = i
		}
	}
	return false
}
