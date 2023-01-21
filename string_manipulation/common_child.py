def commonChild(s1, s2):
    count = 0

    joinedString = s1 + s2
    s2Idx = len(s2)

    for i in range(len(s1)):
        if joinedString[i] == joinedString[s2Idx]:
            print(joinedString[i], joinedString[s2Idx])
            count += 1
        s2Idx += 1

    return count


if __name__ == "__main__":
    print(commonChild("ABCD", "ABDC"))
    print(commonChild("HARRY", "SALLY"))
