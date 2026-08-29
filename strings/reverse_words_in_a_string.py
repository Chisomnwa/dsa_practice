class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Input: We receive a string s containing:
        - English letters
        - digits
        - spaces

        For example: s = "the sky is blue"

        A word is any sequence of non-space characters.

        Output: We need to:
        1. Reverse the order of the words
        2. Remove leading spaces
        3. Remove trailing spaces
        4. Replace multiple spaces between words with one space

        Example:
        "  hello   world  " -> "world hello"

        Goal: we need to return the string with the words reversed.

        Edge Cases:
        - when there are leading spaces
            e.g "   hello world" -> return "world hello"

        - when there are trailing spaces
            e.g "hello world   " -> return "world hello"

        - when there are multiple spaces between words
            e.g "hello   world" -> "world hello"

        - when there are leading, trailing and multiple spaces between words
           e.g "   a   good   example   " -> return "example good a"

        - when there is only one word
            e.g "hello" -> return "hello"


        Walkthrough
        Let's use :

        s = "a  good   example"

        s = "a   g o o d     e x  a  m  p  l  e"
             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
               ↑       ↑     ↑
             space      spaces

        We want: "exampla a good"

        We are not concerned with the individual characters once we've identified the words.

        - - -

        Brute Force Approach

        Intuition 
        The simplest solution here will be to use Python's built-in string operations.

        The key operation is: s.split()

        This automatically:
        - ignores leading spaces
        - ignores trailing spaces
        - treats multiple spaces as seperators
        - gives us the words

        For example: 
        s = " a   good   example "

        We'll get:
        ["a", "good", "example"]

        Then, we reverse the list:
        ["example", "good", "a"]

        Then, we join them exactly with one space:
        "example good a"

        Algorithm:
        1. Split s into words
        2. Reverse th elist of words
        3. Join the reversed words using one space
        4. Return th eresult


        Pseudocode:
        words = split s into words

        reverse the list

        result = join the words using a space

        return result

        Time complexity: O(n) because we need to processs the characters to:
        - split the string
        - reverse the words
        - construct the result

        Space complexity: O(n) because we created an addition space or data structures called words.
        
        - - -
        About the Follow Up:
        Which asks "If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?"

        Eve thogh i am not able to mainupate the string in place, but it was possible, the idea would be:

        Say s = "the   sky   is blue"

        "the   sky   is blue"
                ⬇
        reverse the entire string
                ⬇
         "eulb si yks eht"
                ⬇
            reverse each word
                ⬇
            "blue is sky the

        And we'll also have to compact the extra space in-place
                
        - - - 

        Optimized Approach (Two pointers)
        Intuition:

        Instead of immediately creating a list of all the words with split(), we can scan the string and build words ourselves.

        However, because Python strings are immutable, we still need some storage for the result. o in Python, this won't give us true O(1) space.

        The approach is going to be in three steps

        Say s = "the   sky   is blue"

        remove/normalize spaces
            "the sky is blue"
                ⬇
        reverse the entire string
                ⬇
         "eulb si yks eht"
                ⬇
            reverse each word
                ⬇
            "blue is sky the

        Time complexity: O(n) becasue we still scan and reverse the characters a constant number of times

        Space complexity: If the language provides a mutable string/character array and we're allowed to modify it, then it's O(1) extra space.

        But in Python, strings are immutable, so to determine the true O(1) extra space solution, I'd need to wrk with a mutable character array. Converting the string to a list itself requires O(n) space.
        """
        # # Brute force Aproach
        # words = s.split()

        # words.reverse()

        # result = " ".join(words)

        # return result


        # Optmized Approach (Two pointers)
        chars = list(s)

        # Remove leading/trailing spaces and reduce multiple spaces
        write = 0
        read = 0

        while read < len(chars):

            # Skip spaces
            while read < len(chars) and chars[read] == " ":
                read += 1

            # Copy the word
            while read < len(chars) and chars[read] != " ":
                chars[write] = chars[read]
                write += 1
                read += 1

            # Add one space after the word, if there are more words
            if read < len(chars):
                chars[write] = " "
                write += 1

        # Remove the extra space at the end
        if write > 0 and chars[write - 1] == " ":
            write -= 1

        chars = chars[:write]

        # Reverse the entire string
        left = 0
        right = len(chars) - 1

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        # Reverse each individual word
        start = 0

        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == " ":

                left = start
                right = i - 1

                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1

                start = i + 1

        return "".join(chars)
