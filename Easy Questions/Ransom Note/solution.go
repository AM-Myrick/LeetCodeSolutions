// Package ransomnote description - https://leetcode.com/problems/ransom-note/
package ransomnote

import "strings"

func createCounter(str string) map[string]int {
	counter := make(map[string]int)

	for _, letter := range str {
		letter := string(letter)
		if _, ok := counter[letter]; ok {
			counter[letter]++
		} else {
			counter[letter] = 1
		}
	}
	return counter
}

func canConstruct(ransomNote string, magazine string) bool {
	noteCounter := createCounter(ransomNote)

	for k, v := range noteCounter {
		count := strings.Count(magazine, k)
		if count-v < 0 || count == 0 {
			return false
		}
	}
	return true
}
