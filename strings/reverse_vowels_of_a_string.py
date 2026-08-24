class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Input: as which is a string that contains
        - lowercase letters
        - uppercase letters
        - other printable ASCII characters

        But we need to pay attention only to vowels:
        a e i o u 
        A E I O U

        Output: return the string with the vowels reversed but
        consonants and other chracters must stay in their original positions.

        Goal: We need to find all the vowels in a string and reverse their poitions, while leaving everything else exactly where it was.

        e.g say:
        s = "IceCreAm""

        vowels in it are: I c e e A

        reverse the string: "AceCreIm"

        Edge cases:
        1. No vowels -> return the string
            e.g s = "bcdfg"
            
            There is nothing to reverse
            So, we return "bcdfg"

        2. One vowel -> return the string
            e.g "hello"

            Revrsing the string doesn' chnge anything
            So we return "hello"

        3. Al vowels
            e.g s = "aeiou"
            return them reversed: "uoiea"

        4.  Uppercase vowels
            e.g  = "ICE"
            reversede : "ECI"

        5. When vowels are already in reversed order
            e.g s = "uoiea"
            reversing them: "aeiou"

        Walkthrough:

        s = "I c e C r e A m"
             0 1 2 3 4 5 6 7
             ↑           ↑
             L           R

        L = 0
        R = 7

        Step1 :
        L -> points to I which is a vowel
        R -> points to m which is not a vowel

        Do not reverse yet. We move R one step inward

        Now R -> points to A (which is a vowel)

        So, both are are now pointing to vowels

        You swap them:  "A c e C r e I m"

        L += 1
        R -= 1

        Step 2:

        s = "I c e C r e A m"
             0 1 2 3 4 5 6 7
                 ↑     ↑
                 L     R

        L -> points to c which is not a vowel
        R -> points to e which is a vowel

        Don't swap yet, move L forward.

        L -> points to e
        R -> points to e 

        Both are vowels, and you swap them.

        They are both the same so visually nothing changes.

        Finally return "A c e C r e a I m"

        - - -
        Brute Force Approach

        Algorithm:
        1. Find all the vowels
        2. Store them in another list
        3. Reverse that list
        4. Go through the original string again
        5. Whenver we encounter a vowel, replace it with the next vowel from our reversed list

        Pseudocode:
        Cretae an empty list of vowels

        Loop through s:
            if current character is a vowel:
                add it to vowels

        reverse vowels

        Create an empty result

        Loop through s again:
            if current character is a vowel:
                take the next vowel from vowels
                add it to result
            otherwise:
            add the original character to result

        Return result

        Time complexity: O(n) because we make a couple of passes through the string:
        - First pass -> O(n)
        - Second pass -> O(n)

        Together: O(n) + O(n) = O(n)

        Space complexity: O(n) because we create two different data structures:
        - vowels (which can contain up to n characters) and 
        - result (which contains n charactsers)

        So both O(n) + O(n) = O(n)

        - - -
        Optimized Approach (Using Two Pointers)

        The question: Do we actually need to store all vowels?

        Think about what we're doing:
        first vowel ↔ last vowel
        second vowel ↔ second-to-the-last vowel
        third vowel ↔ third-to-the-last vowel

        That's exactly what two pointers are for.

        We put:

        L -> beginning
        R -> end

        Then, we move them forward to each other.

        Algorithm:
        1. Set L = 0
        2. Set R = length of s - 1

        while L < R:
            while s[L] is not a vowel:
                move L right

            while s[R] is not a vowel:
                move R left

            swap s[L] and s[R]

            move L right
            move R left

        return the string

        Time complexity: Although we have nested-looking while loops, each pointer only moves in one direction.

        left moves from: 0 -> N
        R moves from:  N -> 0

        They don't repeatedly scan the same characters.
        So, the total work is O(n)

        Space complexity:O(n) because we created chars which is an array of N. Meanwhile the two pointers algorithms uses O(1).
        """
        # # Brute Force Implementtion
        # # Because Python strings are immutable, we'll build a list and then join it.

        # vowels = []
        # vowels_set = "aeiouAEIOU"

        # for char in s:
        #     if char in vowels_set:
        #         vowels.append(char)

        # vowels.reverse()

        # result = []
        # vowel_index = 0

        # for char in s:
        #     if char in vowels_set:
        #         result.append(vowels[vowel_index])
        #         vowel_index += 1
        #     else:
        #         result.append(char)

        # return "".join(result)

        # Optimized Approach (Using Two Pointers)
        vowels = "aeiouAEIOU"
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:

            while left < right and chars[left] not in vowels:
                left += 1

            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]

            left += 1
            right -= 1

        return "".join(chars)
