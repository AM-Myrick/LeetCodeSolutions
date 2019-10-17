// Package fizzbuzz description - https://leetcode.com/problems/fizz-buzz/
package fizzbuzz

import "strconv"

func fizzBuzz(n int) []string {
	var resultSlice []string

	for i := 1; i <= n; i++ {
		result := ""
		if i%3 == 0 {
			result += "Fizz"
		}
		if i%5 == 0 {
			result += "Buzz"
		}
		if result == "" {
			resultSlice = append(resultSlice, strconv.Itoa(i))
			continue
		}
		resultSlice = append(resultSlice, result)
	}
	return resultSlice
}
