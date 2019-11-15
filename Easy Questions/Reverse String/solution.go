// Package reversestring description - https://leetcode.com/problems/reverse-string/
package reversestring

func reverseString(s []byte) {
	if len(s) == 0 || len(s) == 1 {
		return
	}
	i, j := 0, len(s)-1
	for j > i {
		s[i], s[j] = s[j], s[i]
		i, j = i+1, j-1
	}
}
