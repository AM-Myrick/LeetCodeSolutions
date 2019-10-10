// https://leetcode.com/problems/remove-element/
package main

func removeElement(nums []int, val int) int {
	for i := 0; i < len(nums); {
		// if the value is found, it's moved to the end of the array
		// the array is then shifted to remove the last value
		if nums[i] == val {
			nums[i], nums[len(nums)-1] = nums[len(nums)-1], 0
			nums = nums[:len(nums)-1]
			continue
		}
		i++
	}
	return len(nums)
}
