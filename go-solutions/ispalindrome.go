package piscine

import (
	"strings";
	"unicode"
)

func IsPalindrome(s string) bool {

	// Create a sloice of rune to hold the string 
	// This enables us to manipulate the string later
	var cleaned []rune

	// Now, chnage the string to lowercase and make sure we
	// have only alphanumeric characters
	for _, char := range strings.ToLower(s) {
		if unicode.IsLetter(char) || unicode.IsDigit(char) {
			cleaned = append(cleaned, char)
		}
	}

	left := 0
	right := len(cleaned) - 1

	for left < right {
		if cleaned[left] != cleaned[right] {
			return false
		}

		left ++
		right --
	}

	return true
}
