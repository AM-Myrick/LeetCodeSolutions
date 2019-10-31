// Package ishappy description - https://leetcode.com/problems/happy-number/
package ishappy

import "strconv"

func isHappy(n int) bool {
	copy := strconv.Itoa(n)
	total := 0
	seen := make(map[int]int)

	for true {
		for _, value := range copy {
			value := (value - '0')
			total += int(value * value)
		}

		if _, ok := seen[total]; ok {
			return false
		} else if total == 1 {
			return true
		}
		seen[total] = 0

		copy, total = strconv.Itoa(total), 0
	}
	return true
}
