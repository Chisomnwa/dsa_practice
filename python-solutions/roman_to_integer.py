def romanToInt(s: str):
    # Step 1: Define what roman numerals mean

    roman_map = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

    # Putting the thinking together
    result = 0
    i = 0

    for char in s:
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result = result - roman_map[s[i]]
        else:
            result = result + roman_map[s[i]]

        i = i + 1

    return result

print(romanToInt("IV"))