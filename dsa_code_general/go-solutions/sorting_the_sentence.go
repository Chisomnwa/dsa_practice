package gosolutions

import "strings"

func SortSentence(s string) string {
	// loop through the sentence
	// split them with a space
	// confirm if each word ends with a digit
	// check their index position
	// And return themn accordingly as string and join them bak

	words := strings.Fields(s)
	result := make([]string, len(s))

	// get the last character in each word
	for _, word := range words {
		position := int(word[len(word) - 1] - '0')

		// remove the digit and place each word in a correct position
		result[position - 1] = word[:len(word) - 1]
	}
	return strings.Join(result, " ")
}
