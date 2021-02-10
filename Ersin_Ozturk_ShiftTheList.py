'''
Developer: Ersin ÖZTÜRK
Porgram Name: Shift The List
Date: 07.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the list and the shifting number.
And it rotate the list acording to shifting number.
'''

list_lenght=int(input("How many input item will you enter the list for shifting?\n")) # Specify lenght of list
list=[input("Enter the "+str(i+1)+". item for list:\n") for i in range(list_lenght)]  # List filled by for loop
shift=int(input("How many times do you need to shift (Pozitive is for right, Negative for left)?\n")) # Specify shift
if shift<0:                                                                           # change from negative to positive
    shift=list_lenght+shift                                                           # pos_shift = lenght + neg_shift
list2=[list[(i-shift)%list_lenght] for i in range(list_lenght)]                       # produce a new list with shit
print(list2)                                                                          # print the new list

