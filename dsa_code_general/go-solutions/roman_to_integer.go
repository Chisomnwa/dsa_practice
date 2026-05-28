package gosolutions

func RomanToInt(s string) int {

	// Step 1: Define the values of the roman numerals
	var roman_map = map[rune]int{
		'I':1, 
		'V':5, 
		'X':10, 
		'L':50, 
		'C':100, 
		'D':500, 
		'M':1000,
	}

result := 0

// Iterate over the string
for i:=0; i<len(s); i++ {
	curr := roman_map[rune(s[i])]

	// Step 3: Check if next numeral exists and is larger
	if i+1 < len(s) && curr < roman_map[rune(s[i + 1])] {
		result = result - curr
	} else {
		result = result + curr
	}
}

return result
}