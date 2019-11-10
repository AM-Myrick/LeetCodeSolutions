// Package lastwordlength description - https://leetcode.com/problems/length-of-last-word/
package lastwordlength

import "strings"

func lengthOfLastWord(s string) int {
	copy := strings.Split(s, " ")
	i := 0

	for i < len(copy) {
		if copy[i] == "" {
			copy = append(copy[:i], copy[i+1:]...)
			continue
		}
		i++
	}

	if len(copy) < 1 || s == "" {
		return 0
	}
	return len(copy[len(copy)-1])
}
