package gosolutions

func IsPalindromeII (s string) bool{
	/*
		This function takes in a string (made up of lowercase English letters) 
		and returns true if the string can be palindrome after deleting at most
		one character from it.
	*/
	left := 0
	right := len(s) - 1

	for left < right {
		if s[left] == s[right] {
			left++
			right--
		} else {
			// Try skipping one character
			return IsPalindromeRange(s, left+1, right) ||
				IsPalindromeRange(s, left, right-1)
		}
	}
	return true
}

func IsPalindromeRange(s string, left, right int) bool {
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}
