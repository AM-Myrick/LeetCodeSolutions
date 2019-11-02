// Package checkrecord description - https://leetcode.com/problems/student-attendance-record-i/
package checkrecord

import "strings"

func checkRecord(s string) bool {
	if strings.Contains(s, "LLL") {
		return false
	}
	counter := make(map[string]int)

	for i := 0; i < len(s); i++ {
		letter := string(s[i])
		if _, ok := counter[letter]; ok {
			if letter == "A" {
				return false
			}
		} else {
			if letter == "A" {
				counter[letter] = 1
			}
		}
	}
	return true
}
