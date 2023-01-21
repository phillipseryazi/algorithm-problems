def isValid(s):
    if len(s) == 1:
        return "YES"

    memo = {}

    for i in s:
        memo[i] = 0

    for i in range(len(s)):
        memo[s[i]] += 1

    valueList = list(memo.values())

    valueList.sort()

    first = valueList[0]
    second = valueList[1]
    last = valueList[len(valueList) - 1]
    secondLast = valueList[len(valueList) - 2]

    # if first and last are the same
    if first == last:
        return "YES"

    # if first is 1 and second and last are the same
    if first == 1 and second == last:
        return "YES"

    # if all are the same and last just one extra
    if first == secondLast and secondLast == last - 1:
        return "YES"

    return "NO"


if __name__ == "__main__":
    print(isValid("a"))
    print(isValid("aabbcd"))  # no
    print(isValid("aabbccddeefghi"))  # no
    print(isValid("abcdefghhgfedecba"))  # yes
    print(isValid("aaaabbcc"))  # no
