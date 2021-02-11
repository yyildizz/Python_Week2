#Furkan Surucu
'''
Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words. Letters unique to word 1. Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations.
The strings will always be in lowercase and will not contain any punctuation.
'''
w1 = input("Enter a word:\n").lower()
w2 = input("Enter the 2nd word:\n").lower()
l1 = [i for i in w1]
l2 = [i for i in w2]
s1 = set(l1)
s2 = set(l2)
inter_list = sorted(list(s1&s2))
str1 = "".join(inter_list)
diff1 = sorted(list(s1-s2))
str2 = "".join(diff1)
diff2 = sorted(list(s2-s1))
str3 = "".join(diff2)
result = [str1,str2,str3]
print(result)
