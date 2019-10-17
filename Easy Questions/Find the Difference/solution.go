// Package findthedifference description - https://leetcode.com/problems/find-the-difference/
package findthedifference

import (
	"strings"
)

func findTheDifference(s string, t string) byte {
	for _, char := range t {
		char := string(char)

		// compares the number of times a char appears in t
		// to the number of times it appears in s
		if strings.Count(t, char) > strings.Count(s, char) {
			return string(char)[0]
		}
	}
	return string("Avoiding compile error")[0]
}
