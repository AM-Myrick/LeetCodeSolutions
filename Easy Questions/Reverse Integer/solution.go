// Package reverseinteger description - https://leetcode.com/problems/reverse-integer/
package reverseinteger

import "strconv"

func reverse(x int) int {
	if x-int(int32(x)) > 0 {
		return 0
	}

	strx := strconv.Itoa(x)
	var copy string

	if x < 0 {
		copy += "-"
	}

	for i := len(strx) - 1; i >= 0; i-- {
		letter := string(strx[i])
		if letter == "-" {
			continue
		}
		copy += letter
	}

	result, _ := strconv.Atoi(copy)

	if result != int(int32(result)) {
		return 0
	}
	return result
}
