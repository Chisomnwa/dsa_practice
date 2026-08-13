"""
There is s acircle of red abd blue tiles. You are given an array of integers 'colors'. 
The color of the tile 'i' is represented by colors[i]:
    - colors[i] == 0 means that tile i is red
    - colors[i] == 1 means that tile i is blue

Every 3 contigous tiles in the circle with alternating colors (the middle tile has a 
different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

"""

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        """
        input: an array of colors representing tiles in a circle
        0 = red
        1 = blue

        e.g colors = [0, 1, 0, 0, 1]
                      0  1  2  3  4

        neighbours:
        0 is next to 4
        4 is next to 0

        alternating group: when you have 3 contigous tiles and the middle 
        tile has a different color from the left and from its right.

        i.e left != middle and middle != right

        output: return the number of alternating groups in a circle.

        goal: is to count and return the number of alternating groups in a circle.

        edge cases:
            - contraints has explained that an array cannot be empty i.e 3 <= colors.length <= 100
            - 'i' will always be 0 or 1 -> so need to take care of any other number that migth be 
                received as one of the inputs i.e 0 <= colors[i] <= 1

        Walkthrough using an example:
        colors = [0, 1, 0, 0, 1]
                  0  1  2  3  4 

        n = 5

        count = 0 9the value to be returned.

        at index 0: colors[4], colors[0], colors[1] -> [1, 0, 1] ✔
        at index 1: colors[0], colors[1], colors[2] -> [0, 1, 0] ✔
        at index 2: colors[1], colors[2], colors[3] -> [1, 0, 0] 𐄂
        at index 3: colors[2], colors[3], colors[4] -> [0, 0, 1] 𐄂
        at index 4: colors[3], colors[4], colors[0] -> [0, 1, 0] ✔

        what we are ding here is getting each index as the middle, and checking its left and right, 
        then at the end, we return the number of the alternating groups which is 3 in this case.

        Is the brute force and straightfoward solution efficient;
            - The time complexity is already 0(n) because i am inspecting each tile once
            - The space complexity stays  at O(1) - no new data structure was created, so no need forn optimization.

        Pseudocode:
            n = len(colors)

            count = 0

            for i in range(n):
                left = colors[(i - 1) %  n]
                middle = colors[i]
                right = colors[(i + 1) % n]

                if left != middle and middle != right:
                    count += 1

            return count

        ---
        Why am I dividing by modulo operator? This helps us wrap around the circle.

        colors = [0, 1, 0, 0, 1]
                  0  1  2  3  4 
        
        Say at index = 0

        n = 5

        left = (i - 1) % 5 -> (0 - 1) % 5 -> -1 % 5 = 4

        | | | | |
        |

        left = colors[4]
        """
        n = len(colors)

        count = 0

        for i in range(n):
           left = colors[(i - 1) % n]
           middle = colors[i]
           right = colors[(i + 1) % n]

           if left != middle and middle != right:
               count += 1

        return count
    
sol = Solution()

colorsA = [1, 1, 1]
colorsB = [0, 1, 0, 0, 1]

print(sol.numberOfAlternatingGroups(colorsA))
print(sol.numberOfAlternatingGroups(colorsB))