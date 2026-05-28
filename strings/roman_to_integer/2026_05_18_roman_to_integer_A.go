package romantointeger

/*
[Problem Number 13]
[Problem LInk]:(https://leetcode.com/problems/roman-to-integer/description/)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies 
to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
*/

// Optimised Approach (Using a Hash Map)
func RomanToInt(s string) int {
	// Create a lookup table for Roman Numerals
	romanMap := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	result := 0

	// Loop through the string, comparing with the next symbol
	for i:= 0; i < len(s); i++ {

		// Check if substraction rule applies
		if i + 1 < len(s) && romanMap[s[i]] < romanMap[s[i + 1]] {
			result = result - romanMap[s[i]]
		} else {
			// Otherwise add normally
			result = result + romanMap[s[i]]
		}
	}
	return result
}

/*
Intuition:
This brute force solution for converting a Roman numeral to an integer in Go involves
iterating through the string from left to right and comaring the current character value
to the next one to handle subtractive cases.

If a character value, is gretaer than the next one, then an addition is applied.

Approach (Step by Step):
s = "III"

step 1: Map value is created to store the Roman numerals values
step 2: result := 0 → Result that will be returned is initialized to 0. 
step 3: i for i:= 0; i < len(s); i++
	- We start looping through the characters starting with index 0
	- e.g s = " I I I"
                0 1 2
step 4: if i + 1 < len(s) && romanMap[s[i]] < romanMap[s[i + 1]]. 
	- i + 1 = 2 
	- len(s) = 3 and 2 < 3
	- We check if the character at index 0 is less than the next character
step 5: result = result - romanMap[s[i]]: if it's less than it gets subtracted from result
step 6: result = result + romanMap[s[i]]: else it's added to result
step 7: return result = 3

Time Complexity: O(n) - the algorithm performs a single pass through the input string of lenght n
Space Complexity: O(1) - map is a fixed-sized for the 7 roman numerals regardless of the length of input string
*/

