// Package fizzbuzz description - https://leetcode.com/problems/fizz-buzz/
// Write a program that outputs the string representation of numbers from 1 to n.

// But for multiples of three it should output “Fizz” instead of the number
// and for the multiples of five output “Buzz”.
// For numbers which are multiples of both three and five output “FizzBuzz”.

// Example:
// n = 15,

// Return:
// [
//     "1",
//     "2",
//     "Fizz",
//     "4",
//     "Buzz",
//     "Fizz",
//     "7",
//     "8",
//     "Fizz",
//     "Buzz",
//     "11",
//     "Fizz",
//     "13",
//     "14",
//     "FizzBuzz"
// ]

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
