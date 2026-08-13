class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """
        I DECIDED TO SOLVE THIS PROBLEM BY MYSELF

        [Problem Number 1773]
        [Problem LInk]:(https://leetcode.com/problems/count-items-matching-a-rule/description/)

        input: a list of lists -> a list of items

        output: the number of items that match a given rule

        goal: check wether each item matches a ruleKey or ruleValue of type,  color or name

        So, for an example:
 
            items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]

            items[i] = ["phone","blue","pixel"] -> represents type, color and name

            There are two rules that are also passed to the function:
            ruleKey -> could be type, color or name

            ruleValue -> which must match the rule key could also be type, color, or name

            e. g ruleKey == type, ruleValue == type
                 ruleKey == color, ruleValue == color
                 ruleKey == name, ruleValue == name

            So, I have to return the number of items that matches the ruleKey and the ruleValue passed

        edge cases:
            - items can never be empty, can have at least 1 item i.e there is no possibility of receving an empty list
            - item[i] cannot be empty as well acoording the constarint, it will have at least one character.

        Walthrough an example:

        Example 1:Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"

        ruleKey = "color", ruleValue = "silver"

        count = 0

        at index[0]:
            items[0][1] -> "blue" -> doesn't match the ruleValue: "silver" ❌
        at index[1]:
            items[1][1] -> "silver" -> matches the ruleValue: "silver" ✅
        at index[2]:
            items[2][1] -> "gold" -> doesn't match the ruleValue: "silver" ❌

        return count = 1

        Pseudocode:

        n = len(items)

        count = 0

        for i in range(n):
            item_type = items[i][0] 
            item_color = items[i][1]
            item_name = items[i][2] 
            
            if ruleKey == "type" and ruleValue == items_type:
                count += 1
            elif ruleKey == "color" and ruleValue == items_color:
                count += 1
            elif ruleKey == "name" and ruleValue == item_name:
                count += 1

        return count

        Time complexity: O(n) because there is one pass through each item.
        Space complexity: O(1) because no extra data structure was created, only variables which doesn't add to growth.
        """
        n = len(items)

        count = 0

        for i in range(n):
            item_type = items[i][0]
            item_color = items[i][1]
            item_name = items[i][2]

            if ruleKey == "type" and ruleValue == item_type:
                count += 1
            elif ruleKey == "color" and ruleValue == item_color:
                count += 1
            elif ruleKey == "name" and ruleValue == item_name:
                count += 1

        return count
        