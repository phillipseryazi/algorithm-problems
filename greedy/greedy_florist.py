flowers = [2, 5, 6]


def getMinimumCost(k, c):
    c.sort(reverse=True)
    total = 0

    for i in range(len(c)):
        total += (int(i / k) + 1) * c[i]

    return total


if __name__ == "__main__":
    print(getMinimumCost(3, flowers))
    print(getMinimumCost(2, flowers))
