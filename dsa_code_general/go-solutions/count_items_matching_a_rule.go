package gosolutions

func CountMatches(items [][]string, ruleKey string, ruleValue string) int {
    count := 0

    for i := 0; i < len(items); i++ {
        if ruleKey == "type" && items[i][0] == ruleValue {
            count = count + 1
        } else if ruleKey ==  "color" && items[i][1] == ruleValue {
            count = count + 1
        } else if ruleKey == "name" && items[i][2] == ruleValue {
            count = count + 1
        }
    }
    return count
}