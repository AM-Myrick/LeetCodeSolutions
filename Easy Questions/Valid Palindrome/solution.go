// Package ispalindrome description - https://leetcode.com/problems/valid-palindrome/
package ispalindrome

import "unicode"

func isPalindrome(s string) bool {
	var copy string
	for _, rune := range s {
		if unicode.IsLetter(rune) || unicode.IsNumber(rune) {
			copy += string(unicode.ToLower(rune))
		}
	}
	rs := []rune(copy)
	for i, j := 0, len(rs)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	rc := string(rs)
	return copy == rc
}
