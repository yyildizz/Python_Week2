# Developer: Furkan Turkmen
# Date     : 11.02.2021
#Purpose of Software: Reinforcement of learned Python Code and Self improvement.
#What does program do: Display a two-column table of the letters and their counts with the letters in sorted order.
text = input(" Please enter text:")
thislist = []

for x in text:                          # eleminate ' ', repeated items and sorted
    if not(x in thislist) and x != ' ':
        thislist.append(x)
thislist.sort()

newlist = []
for i in thislist:          # Make two column list , shows item and counts
    count = 0
    newlist.append(i)
    for a in text:
        if i == a:
            count += 1
    newlist.append(count)
print(newlist)