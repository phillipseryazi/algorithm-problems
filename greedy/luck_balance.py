contests_list = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]


# def luckBalance(k, contests):
#     important_list = []
#     unimportant_list = []
#
#     for value, importance in contests:
#         if importance == 1:
#             important_list.append(value)
#         else:
#             unimportant_list.append(value)
#
#     important_list.sort(reverse=True)
#
#     return sum(important_list[0:k]) + sum(unimportant_list) - sum(important_list[k:])

def luckBalance(k, contests):
    contests.sort(reverse=True)

    total_luck = 0

    for val, importance in contests:
        if importance == 1 and k > 0:
            total_luck += val
            k -= 1
        elif importance == 0:
            total_luck += val
        else:
            total_luck -= val

    return total_luck


if __name__ == "__main__":
    print(luckBalance(3, contests_list))
