"""This program inputs two words from user and outputs the intersection of words
and also remainder from words in a sorted list format"""

str1 = input("please enter your first string ").replace(" ", "")
str2 = input("please enter your first string ").replace(" ", "")


def intersection(str1, str2):
    intersect = ""
    diff1 = ""
    diff2 = ""

    for i in str1:
        if i in str2 and not i in intersect:
            intersect += i
        intersect = sorted(intersect)

    for i in str1:
        if i in str1 and not i in intersect:
            diff1 += i
        diff1 = sorted(diff1)

    for i in str2:
        if i in str2 and not i in intersect:
            diff2 += i
        diff2 = sorted(diff2)

    print(["".join(intersect), "".join(diff1), "".join(diff2)])


intersection(str1, str2)
