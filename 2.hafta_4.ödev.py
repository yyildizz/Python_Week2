"""Write a program that takes in two words as input and returns a list containing three
elements, in the following order:

Shared letters between two words. Letters unique to word 1. Letters unique to word
2. Each element of the output should have unique letters, and should be alphabetically sorted.
Useset operations. The strings will always be in lowercase and will not contain any punctuation.
Example:
Input1>>> "sharp"
Input2>>> "soap"
Output>>> ['aps', 'hr', 'o']"""
text1 = list(input("Enter first word: ").lower())
text2 = list(input("Enter second word: ").lower())
a=[]
b=[]
c=[]
for d in text1:
    if d in text2 and d!=" " and d not in a:
        a.append(d)
    else:
        if d not in text2 and d!=" " and d not in b:
            b.append(d)
for d in text2:
    if d not in text1 and d!=" " and d not in c:
        c.append(d)
print(a,b,c)