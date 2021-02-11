#===========================WORD ANALYSIS PROGRAM=================================
#Write a program that takes in two words as input and returns a list containing three elements, in the following order:
#Shared letters between two words. Letters unique to word 1. Letters unique to word 2. Each element of the output should
#have unique letters, and should be alphabetically sorted. Useset operations.
#The strings will always be in lowercase and will not contain any punctuation.
#Example: #Input1>>> "sharp" #Input2>>> "soap" #Output>>> ['aps', 'hr', 'o']
#================INITIAL PART================================
first_word=input('Enter the first word:').lower()
second_word=input('Enter the second word:').lower()
#===============MAIN PART======================================
first_list=[i for i in first_word] #convert first word to string into list
second_list=[i for i in second_word] #convert second word to string into list

first_set=set(first_list) #convert first word to a set
second_set=set(second_list) #convert second word to a set

first_unique=first_set.difference(second_set)
second_unique=second_set.difference(first_set)
intersection_set=first_set.intersection(second_set)
#================LAST PART========================================
#printing the
print('unique letters of first word:',first_unique)
print('unique letters of second word:',second_unique)
print('common letters ot he words:',intersection_set)
#=============END==================================================

#=============OUTPUTS==============================================
#Enter the first word:Afyonkarahisar
#Enter the second word:Kahramanmaras
#unique letters of first word: {'o', 'y', 'f', 'i'}
#unique letters of second word: {'m'}
#common letters ot he words: {'a', 'n', 'k', 'h', 'r', 's'}
#--------------------------------------------------------------------