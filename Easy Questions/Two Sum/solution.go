// Package twosum description - https://leetcode.com/problems/two-sum/
package twosum

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for index, num := range nums {
		if val, ok := numMap[target-num]; ok {
			if val == index {
				continue
			}
			return []int{index, val}
		}
		numMap[num] = index
	}
	return []int{0, 0}
}
