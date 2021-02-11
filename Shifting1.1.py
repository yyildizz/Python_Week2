# Developer: Furkan Turkmen
# Date     : 11.02.2021
# Purpose of Software: Reinforcement of learned Python Code and Self improvement.
# What does program do: This Program takes two inputs; one of them is a list and the other is a number,
# and returns the list obtained by shifting the elements in the list n places to the right (left)
# when n is positive (negative).
thislist = []
newlist = []
x = int(input("Enter the number of elements :"))

for i in range(0, x):                               # making array
    item = input("Please enter your "+str(i+1) + " element:")
    thislist.append(item)
    newlist.append(item)
print("The list is created succesfully", thislist)

shiftfactor = int(input("Enter shifting number: "))
for a in range(0, len(thislist)):
    if (a + shiftfactor) < len(thislist):
        newlist[a+shiftfactor] = thislist[a]

    elif (a + shiftfactor) >= len(thislist):
        newlist[(a + shiftfactor)-len(thislist)] = thislist[a]

    else:
        print("!!!")
print("Your shifted list:", newlist)
