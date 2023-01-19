# naive solution
def substrCount(n, s):
    count = 0

    for i in range(len(s)):
        for x in range(i + 1, len(s)):
            if len(set(s[i:x+1])) == 1:
                count += 1

            if abs(i - x) == 2:
                if len(set(s[i:x + 1])) == 2:
                    count += 1

    return n + count


if __name__ == "__main__":
    print(substrCount(5, "asasd"))
    print(substrCount(7, "abcbaba"))
    print(substrCount(4, "aaaa"))
