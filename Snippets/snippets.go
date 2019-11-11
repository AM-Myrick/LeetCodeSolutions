// simple snippet for counting characters in an iterable
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