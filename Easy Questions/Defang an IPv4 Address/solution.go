package main

func defangIPaddr(address string) string {
	copy := ""
	for i := 0; i < len(address); i++ {
		letter := string(address[i])

		if letter == "." {
			copy += "[.]"
			continue
		}

		copy += letter
	}
	return copy
}
