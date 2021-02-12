"""Example:

Inputs>>> [1, 2, 3, 4, 5], 2

Output>>> [4, 5, 1, 2, 3]

Inputs>>> [1, 2, 3, 4, 5], -2

Output>>> [3, 4, 5, 1, 2]"""

my_list=list(input("please input list"))
number=int(input("please input for rotate number"))
print(my_list)
print(number)

new_my_list= my_list[-number:]+my_list[:-number]
print(new_my_list)
