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

func LengthOfLastWordB( s string) int {
	length := 0
	i := len(s) - 1

	// Skip trailing spaces from the end
	for i >= 0 && s[i] == ' ' {
		i--
	}

	// Count characters of the last word
	for i >= 0 && s[i] != ' ' {
		length++
		i--
	}

	return length
}

/*
Intuition:
This optimized approach avoids creating a new slice of strings. It starts 
from the end and skips any trailing spaces, and counts characters until it
hits another space or the begining of the string.

Approach (Step by Step):

s = "luffy is still joyboy"

length: 0 - holds the int value we will return(i.e length of the last word of the string)

i : len(s) - 1 → 21 - 1 = 20
i.e i = 20 and y is at the index position of 20


We minus 1 because indexing starts at 0, and to avoid out of range errors.

for i >= 0 && s[i] == ' ' {
	i--
	}

The above code block is skipped since the first character encountered from
the end is `y`

for i >= 0 && s[i] != ' ' {
	legth++ 
	i--
}

Because y is not an empty space:
- length++ : length increases by 1
- i-- : i becomes 19 and the loop moved to to `o`

The above increases the length as we encounter the first character of the last 
word and we keep decreasing i as we keep counting backwards.

The second for loop keeps iterating until the last word 'joyboy' is fully counted.

Then length : 6 is returned.


Time complexity: O(n) - we scan the string once
Space Complexity: O(1) - only two variables used, no extra memory like list or arrays.
*/