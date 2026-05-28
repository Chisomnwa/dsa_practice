// Using a custom method

// func DefangIPaddr(address string) string {
//     return strings.ReplaceAll(address, ".", "[.]")
//     //return defangedAddress
// }

// Time complexity = O(n) because it's looping through more than one dots
// Space Complexity = 0(n)

// Using the rune method

package gosolutions

func DefangIPaddr(address string) string {
	var cleanedAddress []rune

	for _, char := range address {
		if char == '.' {
			cleanedAddress = append(cleanedAddress, '[', '.', ']')
			// cleanedAddress = append(cleanedAddress, '.')
			// cleanedAddress = append(cleanedAddress, ']')
		} else {
			cleanedAddress = append(cleanedAddress, char)
		}
	}
	return string(cleanedAddress)
}
