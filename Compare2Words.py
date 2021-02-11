set1 = set(input("Enter the first word:\n"))
set2 = set(input("Enter the second word:\n"))
myList = [''.join(sorted(set1 & set2)), ''.join(sorted(set1 - set2)), ''.join(sorted(set2 - set1))]
print(myList)

########################################################################################################################
# Write a program that takes in two words as input and returns a list containing three elements, in the following order:
#
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element of the output should have unique letters, and should be alphabetically sorted.
# Use set operations. The strings will always be in lowercase and will not contain any punctuation.
#
# Example:
# Input1>>> "sharp"
# Input2>>> "soap"
# Output>>> ['aps', 'hr', 'o']
