package gosolutions

func Interpret(command string) string {

	cleaned := make([]byte, 0, len(command))

	for i := 0; i < len(command); {

		if command[i] == 'G' {
			cleaned = append(cleaned, 'G')
			i++
		} else if command[i] == '(' && command[i+1] == ')' {
			cleaned = append(cleaned, 'o')
			i += 2
		} else { // must be "(al)"
			cleaned = append(cleaned, 'a', 'l')
			i += 4
		}
	}

	return string(cleaned)
}