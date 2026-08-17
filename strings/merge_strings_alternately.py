class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Input: 
        - word1: str
        - word2: str

        Output: A new merged string

        Goal:
        - Take one character from word1, then one from word2, alternating 
        - if one string finishes first, append the remaining characters of the other string

        Edge cases:
        - Both strings have the same length -> return the alternatively merged string of both
        - word1 is longer -> return the merged string with the remainning character of word1 appendd at the end of the merged string
        - word2 is longer, repeat same
        - one sring has only one character -> append the character and then append the remaing character of the other word

        Walkthrough:
        word1 = "ab"
        word = "pqrs

        result = ""

        Take:

        'a' -> "a"
        'p' -> "ap"
        "b" -> "apb"
        'q' -> "apbq"
        'r' -> "apbqr"
        's' -> "abpqrs"

        - - -


        Brute Force Aproach:
        Intuition:
        We need to merge the strings one character at a time. The simplest approach is:
        - Walk through both strings from left to right
        - Add one character from word1
        - Add one character from word2
        - When one string finishes, append the remaining characters from the other string

        Algorithm:
        1. Create an empty string called result
        2. Find the shorter length of the two strings
        3. Loop from 0 to the shorter length
            - Append word[i]
            - Append word[2]
        4. If word1 is longer, append its remaining characters
        5. Otherwise, append the remaining characters from word2
        6. Return result

        Pseudocode:
        create a empty string called result

        find the minimum length of word1 and word2

        for each index from 0 to minimum length - 1
            append word1[index] to result
            append word2[index] to result

        if word1 has remaining characters
            append the remaining part of word1

        if word2 has remaining characters
            append the remainaing part of word2

        return result 

        Time complexity: 
        - Looping through the shorter string: O(min(m, n))
        - Appending the remaining characters: O(|m-n|)

        Overall: O(m+n)

        where:
            - m = len(word1)
            - n = len(word2)

        Space complexity:
        - The result string stores every character once -> O(m+n)

        - - -
        Optimized Approach (Two Pointers)
        Intution: instead of:
        - finding the shorter length
        - looping to that
        - then appending the remaining characters afterward

        We use pointers.

        - One pointer tracks word1
        - One pointer tracks word2

        As long as either pointer hasn't reached the end of its word, we keep going.

        Algorithm:
        1. Create an empty result
        2. Create two ponters
            i = 0
            j = 0
        3. While either pointer hasn't reached the end
            if i is valid, append word[i] and increment i
            if j is valid, append word[j] and increment j
        4. Return the result

        Pseudocode:
        Create an empty result

        i = 0
        j = 0

        while i < length of word1 OR j < length of word2

            if i < length of word1
                append words[i]
                i = i + 1

            if j < length of word2
                append word2
                j = j + 1

        return result

        Time complexity: O(m + n) because each character from both strings is visited exactly once.

        Space complexity: O(m + n) because the output string contains all the characters
    
        """
        # Brute Force Implementation
        result = ""

        len_word1 = len(word1)
        len_word2 = len(word2)

        limit = min(len_word1, len_word2)

        for i in range(limit):
            result += word1[i]
            result += word2[i]

        if len_word1 > limit:
            result += word1[limit:]

        if len_word2 > limit:
            result += word2[limit:]
        
        return result

        # Optimized approach implementation (Two Pointers)
        result = ""

        i = 0
        j = 0

        while i < len(word1) or j < len(word2):

            if i < len(word1):
                result += word1[i]
                i += 1

            if j < len(word2):
                result += word2[i]
                j += 1

        return result

