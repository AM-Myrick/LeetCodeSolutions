package main

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
			count += 1
		}
	}
	return count
}
