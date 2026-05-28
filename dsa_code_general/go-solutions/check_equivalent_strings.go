package gosolutions

import "strings"

func ArrayStringsAreEqual(word1 []string, word2 []string) bool {
	wordOne := strings.Join(word1, "")
	wordTwo := strings.Join(word2, "")

	if strings.Compare(wordOne, wordTwo) == 0 {
		return true
	} else {
		return false
	}
}