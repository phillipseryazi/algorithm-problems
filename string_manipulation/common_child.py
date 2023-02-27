# def commonChild(s1, s2):
#     grid = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
#
#     for i in range(len(s1) - 1, -1, -1):
#         for j in range(len(s2) - 1, -1, -1):
#             if s1[i] == s2[j]:
#                 grid[i][j] = 1 + grid[i + 1][j + 1]
#             else:
#                 grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])
#
#     for i in range(len(grid)):
# #         print(grid[i])
#
#     return grid[0][0]


def commonChild(s1, s2):
    lcs = 0

    grid = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i - 1] == s2[j - 1]:
                grid[i][j] = 1 + grid[i - 1][j - 1]
                if lcs < grid[i][j]:
                    lcs = grid[i][j]
            else:
                grid[i][j] = 0

    # print(grid)

    for i in range(len(grid)):
        print(grid[i])

    return lcs


if __name__ == "__main__":
    print(commonChild("ABCD", "ABDC"))
    # print(commonChild("HARRY", "SALLY"))
