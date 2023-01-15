def alternatingCharacters(s):
    deletions = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1

    return deletions


if __name__ == "__main__":
    print(alternatingCharacters("AAAA"))
    print(alternatingCharacters("BBBBB"))
    print(alternatingCharacters("ABABABAB"))
    print(alternatingCharacters("BABABA"))
    print(alternatingCharacters("AAABBB"))
