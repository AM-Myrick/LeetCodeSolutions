package main

func defangIPaddr(address string) string {
	copy := ""
	for i := 0; i < len(address); i++ {
		if string(address[i]) == "." {
			copy += "[.]"
			continue
		}
		copy += string(address[i])
	}
	return copy
}
