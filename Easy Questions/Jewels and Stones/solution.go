// Package numjewelsinstones - https://leetcode.com/problems/jewels-and-stones/
// You're given strings J representing the types of stones that are jewels,
// and S representing the stones you have.  Each character in S is a type of stone you have.
// You want to know how many of the stones you have are also jewels.

// The letters in J are guaranteed distinct, and all characters in J and S are letters.
// Letters are case sensitive, so "a" is considered a different type of stone from "A".

// Example 1:
// Input: J = "aA", S = "aAAbbbb"
// Output: 3

// Example 2:
// Input: J = "z", S = "ZZ"
// Output: 0
// Note:

// S and J will consist of letters and have length at most 50.
// The characters in J are distinct.
package numjewelsinstones

func numJewelsInStones(J string, S string) int {
	// create a map with string keys and int values to keep track of the jewels
	// setting value for all jewels to 0 since value doesn't really matter here
	jewels := make(map[string]int)
	for i := 0; i < len(J); i++ {
		jewels[string(J[i])] = 0
	}

	count := 0
	for j := 0; j < len(S); j++ {
		// if the key exists in jewels, we increment count by one
		// maps have O(1) search whereas strings have O(n) search
		// if I wrote the same code iterating through J and S and comparing each element
		// I'd end up with slower code
		if _, ok := jewels[string(S[j])]; ok {
			count++
		}
	}
	return count
}
