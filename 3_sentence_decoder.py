"""This program inputs a sentence from user and outputs the occurrence of all letters in
dictionary format"""


sentence = input("Please enter a sentence without any punctuation: \n")
sentence = sentence.replace(" ", "")

dictionary = {char: (sentence.count(char)) for char in sentence}
print(dictionary)