def makeAnagram(a, b):
    s1 = a + b
    memo = {}

    for i in s1:
        memo[i] = 0

    for x in a:
        memo[x] += 1

    for x in b:
        memo[x] -= 1

    deletions = 0
    for v in memo.values():
        deletions += abs(v)

    return deletions


if __name__ == "__main__":
    print(makeAnagram("cde", "abc"))
