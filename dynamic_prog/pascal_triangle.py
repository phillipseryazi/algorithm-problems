from typing import List


def generate(numRows: int) -> List[List[int]]:
    aList = []
    for row in range(numRows):
        temp_list = []
        for col in range(row + 1):
            if col == 0 or col == row:
                temp_list.append(1)
            else:
                temp_list.append(aList[row - 1][col - 1] + aList[row - 1][col])

        aList.append(temp_list)

    return aList


if __name__ == "__main__":
    print(generate(5))
