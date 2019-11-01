// Package containsduplicate2 - https://leetcode.com/problems/contains-duplicate-ii/
package containsduplicate2

// Given an array of integers and an integer k, find out whether there are two distinct indices
// i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

// Example 1:
// Input: nums = [1,2,3,1], k = 3
// Output: true

// Example 2:
// Input: nums = [1,0,1,1], k = 1
// Output: true

// Example 3:
// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false

func containsNearbyDuplicate(nums []int, k int) bool {
	copy := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if lastIndex, ok := copy[num]; ok {
			if i-lastIndex <= k {
				return true
			}
		}
		copy[num] = i
	}
	return false
}
