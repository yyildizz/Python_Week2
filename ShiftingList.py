#Furkan Surucu
'''
Write a program that takes two inputs; one of them is a list and the other is a number,
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative).
Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.
'''
elements = list(input("Enter list elements:\n"))
number= int(input('''Enter a number to rotate your list:
To the right (positive)
To the left (negative)
'''))
new_list = elements[-number:]+elements[:-number]
print(new_list)

