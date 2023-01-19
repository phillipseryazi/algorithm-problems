def isValid(s):
    memo = {}

    for i in s:
        memo[i] = 0

    for i in range(len(s)):
        memo[s[i]] = s.count(s[i])

    count = 0
    for k, v in memo.items():
        if (v - min(memo.values())) > 0:
            count += 1

    if count > 0:
        return "NO"

    return "YES"


if __name__ == "__main__":
    print(isValid("aabbcd"))  # no
    print(isValid("aabbccddeefghi"))  # no
    print(isValid("abcdefghhgfedecba"))  # yes
    print(isValid("aaaabbcc"))  # no
