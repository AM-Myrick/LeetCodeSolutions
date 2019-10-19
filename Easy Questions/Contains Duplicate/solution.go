// Package containsduplicate https://leetcode.com/problems/contains-duplicate/
// Given an array of integers, find if the array contains any duplicates.
// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:
// Input: [1,2,3,1]
// Output: true

// Example 2:
// Input: [1,2,3,4]
// Output: false

// Example 3:
// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true

package containsduplicate

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
