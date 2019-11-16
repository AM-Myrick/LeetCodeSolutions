// Package countones description - https://leetcode.com/problems/max-consecutive-ones/
package countones

func findMaxConsecutiveOnes(nums []int) int {
	count := 0
	max := 0

	for _, num := range nums {
		switch num {
		case 1:
			count++
			if count > max {
				max = count
			}
		case 0:
			count = 0
		}
	}
	return max
}
