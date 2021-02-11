# Developer: Furkan Turkmen
# Date     : 11.02.2021
# Purpose of Software: Reinforcement of learned Python Code and Self improvement.
# What does program do:The program takes in 2 words as input and finds same letter and Shared letters between two words.
# Letters unique to word 1. Letters unique to word 2. Each element of the output should have unique letters,
# and make alphabetically sorted.




text1 = input("Enter first word: ")
text2 = input("Enter second word: ")
newlist1 = []
newlist2 = []
thislist = []
thatlist = []
thoselist = []
for i in text1:         # this code puts it in alphabetical order and cancels repeating characters
    if not(i in newlist1):
        newlist1.append(i)
newlist1.sort()

for i in text2:         # same as above
    if not(i in newlist2):
        newlist2.append(i)
newlist2.sort()

for i in newlist1:      #this code finds common elements of first input and second input
    if i in newlist2:
        thislist.append(i)

    elif i not in newlist2: #this code finds different elements of first input from second input
        thatlist.append(i)
for a in newlist2:
    if a not in newlist1:   #this code finds different elements of second input from first input
        thoselist.append(a)
str1 = ''
str2 = ''
str3 = ''
for s in thislist:  # This code convert array to string
    str1 += s
for w in thatlist:
    str2 += w
for q in thoselist:
    str3 += q


print("'"+str1+"'," "'"+str2+"'," "'" + str3+"'")