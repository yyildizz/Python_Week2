"""This code takes two parameters: first is a list, second is an integer
Then rotates the list in both side; forward - backward"""


def list_shifter(l, n):
    return l[n:] + l[:n]


test = [1, 2, 3, 4, 5, 6]

print(list_shifter(test, -2))
