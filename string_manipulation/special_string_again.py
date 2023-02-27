# naive solution
# def substrCount(n, s):
#     count = 0
#
#     for i in range(len(s)):
#         pointer = i + 1
#         breaker = 0
#         while pointer < len(s):
#             if s[i] == s[pointer]:
#                 count += 1
#             else:
#                 breaker += 1
#                 if breaker == 2:
#                     break
#             pointer += 1
#
#     return n + count


def substrCount(n, s):
    count = 0

    for i in range(len(s)):
        pointer = i + 1
        breaker = 0
        while pointer < len(s):
            if s[i] != s[pointer]:
                print(s[i], s[pointer])
            else:
                count += 1

            pointer += 1

    return n + count


if __name__ == "__main__":
    # print(substrCount(5, "asasd"))
    # print(substrCount(4, "aaaa"))
    # print(substrCount(7, "abcbaba"))
    print(substrCount(8, "mnonopoo"))
