// Package poweroftwo description - https://leetcode.com/problems/power-of-two/
package poweroftwo

func isPowerOfTwo(n int) bool {
	return n != 0 && (n&(n-1)) == 0
}
