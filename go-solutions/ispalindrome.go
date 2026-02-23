package gosolutions

import (
	//"fmt"
	//"strings";
	"unicode"
)

// func IsPalindrome(s string) bool {

// 	// Create a sloice of rune to hold the string 
// 	// This enables us to manipulate the string later
// 	var cleaned []rune

// 	// Now, chnage the string to lowercase and make sure we
// 	// have only alphanumeric characters
// 	for _, char := range strings.ToLower(s) {
// 		if unicode.IsLetter(char) || unicode.IsDigit(char) {
// 			cleaned = append(cleaned, char)
// 		}
// 	}

// 	left := 0
// 	right := len(cleaned) - 1

// 	for left < right {
// 		if cleaned[left] != cleaned[right] {
// 			return false
// 		}

// 		left ++
// 		right --
// 	}

// 	return true
// }


// Optimized version to decrease space complexity to O(1)
func IsPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left < right {

		// Move left pointer until it points to alphanumeric
		for left < right && !unicode.IsLetter(rune(s[left])) && !unicode.IsDigit(rune(s[left])) {
			left++
		}

		// Move right pointer until it points to alphanumeric
		for left < right && !unicode.IsLetter(rune(s[right])) && !unicode.IsDigit(rune(s[right])) {
			right--
		}

		// Compare lowercase versions
		if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])) {
		return false
		}

		left ++
		right --
	}

	return true
}

