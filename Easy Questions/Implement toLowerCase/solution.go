// Package tolowercase - https://leetcode.com/problems/to-lower-case/
package tolowercase

import "unicode"

func toLowerCase(str string) string {
	copy := ""
	for _, letter := range str {
		copy += string(unicode.ToLower(letter))
	}
	return copy
}
