# ============LUCKY NUMBERS =======================================
# Developer: Cemil Tepecik
# Date:07.02.2021
# Write a programme to generate the lucky numbers from the range(n).
# These are generated starting with the sequence s=[1,2,...,n].
# At the first pass, we remove every second element from the sequence, resulting in s2.
# At the second pass, we remove every third element from the sequence s2,
# resulting in s3, and we proceed in this way until no elements can be removed.
# The resulting sequence are the numbers lucky enough to have survived elimination.
#------------------------INITIAL PART---------------------------------
print('Enter the lenght oft he sequence that you wish to produce (s=[1,2,...,n] sequence:')
n=int(input())

sequence=list(range(n+1))
sequence.remove(0) #sequence starting from 1 ends in n
sequence=sequence
print('sequence',sequence)
print('--------------------------------')
control=len(sequence)+1 #max number of recursion in the loop
k=1 #initial element
m=2 #amount of increasement
j=1 #for while loop
#----------------------MAIN PROGRAM--------------------------------------
while j < (control):
    temporary=sequence[k:control:m]
    seq=set(sequence) #convert to set
    tem=set(temporary)  #convert to set

    diff=seq-tem #reamining numbers in the sequence
    if len(diff)== len(seq): #cease the loop because sorting process completed
        break
    sequence=list(diff)  #convert to list again for the next loop
    k+=1
    m+=1
    j+=1

    print('Ramaining numbers:',sequence)
#------------------------FINAL PART : Printing the Lucky Numbers---------------------
print('--------------------------------')
print('Lucky numbers are:',sequence)
print('================================')
#========================================END==========================================

#=======OUTPUT========
#Enter the lenght oft he sequence that you wish to produce (s=[1,2,...,n] sequence: 30
#sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#--------------------------------
#Ramaining numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
#Ramaining numbers: [1, 3, 7, 9, 13, 15, 19, 21, 25, 27]
#Ramaining numbers: [1, 3, 7, 13, 15, 19, 25, 27]
#Ramaining numbers: [1, 3, 7, 13, 19, 25, 27]
#Ramaining numbers: [1, 3, 7, 13, 19, 27]
#--------------------------------
#Lucky numbers are: [1, 3, 7, 13, 19, 27]
#================================
#================================