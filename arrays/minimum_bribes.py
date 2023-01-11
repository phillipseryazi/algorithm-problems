"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n .
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
 One person can bribe at most two others.Determine the minimum number of bribes that took place to get to a given queue order.
 Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""

arr = [2, 1, 5, 3, 4]
arr2 = [2, 5, 1, 3, 4]
arr3 = [1, 2, 5, 3, 7, 8, 6, 4]


# 5= 1
# 3 = none
# 7 = 2
# 8 = 2
# 6 = 1

# Timeout solution
# def minimumBribes(q):
#     totalBribes = 0
#     isChaotic = False
#
#     for i in range(len(q) - 1):
#         currsBribes = 0
#         for x in range(i + 1, len(q)):
#             if q[i] > q[x]:
#                 currsBribes += 1
#                 totalBribes += 1
#             if currsBribes > 2:
#                 isChaotic = True
#
#     if isChaotic:
#         print("Too chaotic")
#     else:
#         print(totalBribes)


def minimumBribes(q):
    bribes = {}

    for k in q:
        bribes[k] = 0
    for i in range(len(q) - 1):
        swapped = False
        for j in range(len(q) - 1 - i):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]  # swap, or bribe
                bribes[q[j + 1]] += 1
                swapped = True
        if not swapped:
            break

    if max(bribes.values()) > 2:
        print("Too chaotic")
    else:
        print(sum(bribes.values()))


if __name__ == "__main__":
    minimumBribes(arr)
    minimumBribes(arr2)
    minimumBribes(arr3)
