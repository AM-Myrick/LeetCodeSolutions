//https://leetcode.com/problems/palindrome-number/
package main

import "strconv"

func isPalindrome(x int) bool {
	// convert int to str
	copy := strconv.Itoa(x)

	// checks if each element matches the corresponding element
	// required for the int to be a palindrome
	for i, j := 0, len(copy)-1; i < j; i, j = i+1, j-1 {
		if copy[i] != copy[j] {
			return false
		}
	}
	return true
}
