"""
Developer: Ersin ÖZTÜRK
Program Name: Set Operations of 2 Words (We assumed no punctuations)
Date: 07.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes two string word.
Specify the intersection and differences of letters in list that has three items by using set operations.
"""
word1 = input("Write the word 1: \n").lower()        # take the first word from user
word2 = input("Write the word 2: \n").lower()        # take the second word from user

general_list = []                                    # we created a general list to show the result with none

list1 = [i for i in word1]                           # list1 is produced with each letter of word1
list2 = [i for i in word2]                           # list2 is produced with each letter of word2

set1 = set(list1)                                    # convert list1 to set1 with set function
set2 = set(list2)                                    # convert list2 to set2 with set function

list_intersection = list(set1 & set2)                # find the intersection of two set and convert them to list
list_intersection.sort()                             # sort the intersection list

list_dif_w1 = list(set1-set2)                        # find the difference of set1 from set2 and convert them to list
list_dif_w1.sort()                                   # sort the list

list_dif_w2 = list(set2-set1)                        # find the difference of set2 from set1 and convert them to list
list_dif_w2.sort()                                   # sort the list

str_intersection = ''                                # create the string of intersection as none
str_dif_w1 = ''                                      # create the string of difference set1 as none
str_dif_w2 = ''                                      # create the string of difference set2 as none

for i in list_intersection:                          # produce the intersection string from intersection list
    str_intersection += i

for i in list_dif_w1:                                # produce the dif_w1 string from dif_w1 list
    str_dif_w1 += i

for i in list_dif_w2:                                # produce the dif_w2 string from dif_w2 list
    str_dif_w2 += i

general_list = [str_intersection, str_dif_w1, str_dif_w2]      # produce the general list with three items

print(general_list)                                  # print the general list


