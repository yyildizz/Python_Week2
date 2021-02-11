#==============SENTENCE LETTERS ANALYSIS DICTIONARY=======================================
# Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter.
# Ignore case, ignore blanks and assume the user does not enter any punctuation.
# Display a two-column table of the letters and their counts with the letters in sorted order.
#Example:
#Input >>> "This is a sample text with several words This is more sample text with some different words"
#Output >>> [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4),
# ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
#===========================INITIAL PART=======================================000
sentence=input('Enter the sentence:').lower() #The most important thing in the World is to love God and People
all_letters=[i for i in sentence]  #cut down the sentence into letters
number_char=len(all_letters) #how many different character exists
#Determine which letters exist int sent.
all_letters_set=set(all_letters)
all_letters_unique=list(all_letters_set)
all_letters.sort() # order alphabetically all
all_letters_unique.sort() #order alphabetically only unique
all_letters_unique.remove(' ') # remove ' ' from the list
print('All_letters:',all_letters)
print('Unique letters:',all_letters_unique)

#=====================MAIN PROGRAM========================================
counter_1=len(all_letters)
counter_1_list=list(range(counter_1))
counter_2=len(all_letters_unique)
counter_2_list=list(range(counter_2))
final_list=[]
# Determine repetations
for x in counter_2_list: #unique
    adet = 0
    for y in counter_1_list: #all
        if all_letters_unique[x]==all_letters[y]:
            adet+=1
    final_list.append(adet) #repetation list
print(final_list)

#==============FINAL PART: PUT IN ORDER, DİSPLAY
sentence_the=[]
sentence_final=[]
for x in counter_2_list:
    num=all_letters_unique[x]
    let=final_list[x]
    sentence_the=[num,let]

    sentence_dict=tuple(sentence_the)
    sentence_final.append(sentence_dict)
print('sentence_final',sentence_final)
#================END========================================

#=================OUTPUT====================================
#Enter the sentence:The most important thing in the World is to love God and People
#All_letters: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'p', 'r', 'r', 's', 's', 't', 't', 't', 't', 't', 't', 't', 'v', 'w']
#Unique letters: ['a', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'v', 'w']
#[2, 3, 5, 2, 3, 4, 3, 2, 4, 7, 3, 2, 2, 7, 1, 1]
#sentence_final [('a', 2), ('d', 3), ('e', 5), ('g', 2), ('h', 3), ('i', 4), ('l', 3), ('m', 2), ('n', 4), ('o', 7), ('p', 3), ('r', 2), ('s', 2), ('t', 7), ('v', 1), ('w', 1)]



