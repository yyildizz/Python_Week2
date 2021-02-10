'''
Developer: Ersin ÖZTÜRK
Porgram Name: Luckey  Numbers
Date: 07.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the number and it specify the luckey numbers.
'''
number=int(input("Write the number:\n"))    #Inputs are taken
list=[i+1 for i in range(number)]           #List is produced
print(list)                                 #All list is written
k=0
while(True):                                #"While Loop" is using for delete the specify item
    del list[k+1:len(list):k+2]             # for k=0, we first delete item of index number 1 and respectively two more
    print(list)                             # for k=1, we delete item of index number 2 in new list and respectively three more
    k+=1                                    # NOT: We couldn't use -1 index for last item, because we want to include it.
    if k>=len(list)-1:                      # İf we came to last item we can break the loop
        break