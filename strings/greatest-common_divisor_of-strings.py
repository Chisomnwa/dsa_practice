class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Input: 
        - str1: string
        - str2: string

        Output:  A string that can be repeatedly concatenated to return both string one and string two. i.ethat string is a common divisor.

        Goal: To return the longest possible string 'x' that can be repeated to form both string one and string two

        Edge cases:
        1. If there are no common pattern -> return ""
            e.g "LEFT", "CODE"
        2. One string is not actually made from the same repeating pattern -> return ""
            e.g "AAAAAB", "AAA"
        2. If one string is shorter but is the repeating base of the larger one -> return the shorter pattern
            e.g "ABCABC", "ABC", "ABC"
        3. Both strings are identical -> the entire string can be the answer
            e.g "ABC", "ABC" -> "ABC"

        Walkthrough:

        Example 1:
        str1 = "ABCABC"
        str2 = "ABC"

        We can make both strings using: "ABC"

        Because "ABC" + "ABC" = "ABCABC"

        answer = "ABC"

        Example 2:
        str1 = "ABABAB"
        str2 = "ABAB"

        We can make both strings using: "AB"

        Because "AB" + "AB" = "ABAB"
        And "AB" + "AB" + "AB" = "ABABAB"

        answer = "AB"

        Example 3:
        str1 = "LEFT"
        str2 = "CODE"

        There's no common pattern between the two.

        Because of that, we return ""

        Example 4:
        str1 = "AAAAAB"
        str2 = "AAA"

        The commomn pattern could have been A, but the final B in string one destroys the pattern.

        Because of that, we rteurn ""

        - - -

        Brute Force Approach

        Algorithm:
        1. Find the shorter string because the answer cannot be more than the shorter string
        2. Starting from the largest possible length, take a prefix of the shorter string as our candidate x
        3. Check wether x can build the entire string1 by repeating it.
        4. Check wethetr x can also build the entire string2 by repeating it as well
        5. If it works for both, return it immediately becase we are checking candidate from the largest to smallest
        6. If none works, return ""

        Example

        str1 = "ABABAB"
        str2 = "ABAB"

        The shorter string is "ABAB"

        We try:

        "ABAB" -> does it build both? ❌
        "ABA" -> does it build both? ❌
        "AB" -> does it build both? ✅

        So, we return "AB"

        Pseudocode:
        gcdOfStrings(str1, str2)

            # The answer cannot be longer than the shorter string
            if length of str1 < length of str2
                shorter = str1
            else
                shorter = str2

            # Try candidate strings from longest to shortest
            for length from length of shorter down to 1

                candidate = first "length" characters of shorter

                # Check if candidate can build str1
                if candidate repeated (length of str1 // length of candidate) times
                    is NOT equal to str1
                        continue

                # Check if candidate can build str2
                if candidate repeated (length of str2 // length of candidate) times
                    is NOT equal to str2
                        continue

                return candidate

            return ""
        
        - - -

        Optimized Approach (Mathematical GCD & String Manipulation)

        If some string x divides both str1 and str2, then both strings must have the same repeating pattern:

        For example:

        str1 = "ABABAB"
        str2 = "ABAB"

        We can check wether they have the same pattern by comparing:
        
        str1 + str2

        with

        str2 + st1

        Here:
        "ABABAB" + "ABAB" = "ABABABABAB"
        "ABAB" + "ABABAB" = "ABABABABAB"

        This means they are equal, so a common divisor might exist.

        If they're different, there's definitely no common didvisor.

        Algorithm:
        1. Check whether str1 + str2 == str2 + str1
        2. If not, return ""
        3. If yes, find the GCD of the two string lengths
        4. Return the prefix of str1 whose lenghth is that GCD

        For example:
        len(str1) = 6
        len(str2) = 4

        We get:

        gcd(6, 4) = 2

        So we take the fisrt 2 characters: "AB"

        That's our answer.

        Pseudocode (Mathematical GCD & String Manipulation)):
        gcdOfStrings(str1, str2)

            if str1 + str2 is not equal to str2 + str1
                return ""

            length = GCD of len(str1) and len(str2)

            return the first length characters of str1
        """
        # Brute Force Implementation

        # # The answer cannot be longer than the shorter string
        # if len(str1) < len(str2):
        #     shorter = str1
        # else:
        #     shorter = str2

        # # Try candidate strings from longest to shortest
        # for length in range(len(shorter), 0, -1):
        #     candidate = shorter[:length]

        #     if candidate * (len(str1) // len(candidate)) != str1:
        #         continue

        #     if candidate * (len(str2) // len(candidate)) != str2:
        #         continue

        #     return candidate

        # return ""
        
        #########################################################

        # Optimized Approach Implementation
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]
