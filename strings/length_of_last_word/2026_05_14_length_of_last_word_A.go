package lengthoflastword

/*
[Problem Number 58]
[Problem LInk]:(https://leetcode.com/problems/length-of-last-word/)

Given a string `s` consisting of words and spaces, return the length of the last word
in the string.

A word is a maximal sunstring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5


Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
*/

import (
	"strings"
)

func LengthOfLastWordA(s string) int {
	// Split the string and remove all spaces
	words := strings.Fields(s)

	// Make sure the string is not empty
	if len(words) == 0 {
		return 0
	}

	// Get the last word in the string
	lastWord := len(words) - 1

	// Get the length of that last word
	lenLastWord := len(words[lastWord])

	return lenLastWord
}


/*
Intuition:
The solution here involves using the strings.Fields to strip all spaces both
at the end and split by the empty spaces in between the words in the string. Then, 
as I'm concerened only with the last word, I get the last word of the string, 
and get the length. Kapich!!

Approach (Step by Step):

s = "luffy is still joyboy"

strings.Fields strips leading/trailing spaces and splits on any whitespace:
	words = ["luffy", "is", "still", "joyboy"]

Last element : words[3] = "joyboy"
len("joyboy") = 4

Return : 4

Note: strings.Fields is prefreed over strings.Split(s, " ") here because
it correctly handles multiple consecutive spaces and leading/trailing spaces
without producing empty strings.

Time complexity: O(n) - must traverse the entire string to split it
Space Complexity: O(n) - creates a new sliceof substrings
*/
