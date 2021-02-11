# Furkan Surucu
'''
Write a code snippet that inputs a sentence from the user,
then uses a dictionary to summarize the number of occurrences of each letter.
Ignore case, ignore blanks and assume the user doesnot enter any punctuation.
Display a two-column table of the letters and their counts with the letters in sorted order.
'''
txt = input("Enter a sentence:\n").lower()
letters = {}
for i in txt:
    if i in letters:
        letters[i] +=1
    else:
        letters[i] = 1
print(sorted(letters.items()))
