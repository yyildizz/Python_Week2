#==============SHIFTING A LIST RIGHT OR LEFT=========================
# Write a program that takes two inputs; one of them is a list and the other is a number,
# and returns the list obtained by shifting the elements in the list m places
# to the right when m is positive; to the right when m is negative. Use wrap-around: if an element is shifted beyond
# the end of the list, then continue to shift starting at the beginning of the list.
# Example:
# Inputs>>> [1, 2, 3, 4, 5], 2
# Output>>> [4, 5, 1, 2, 3]
# Inputs>>> [1, 2, 3, 4, 5], -2
# Output>>> [3, 4, 5, 1, 2]
#=============INITIAL PART================================
print('Enter the number of element in your list:')
n=int(input())
my_numbers=list(range(n))
print(my_numbers)
print('Enter how many shift you want: \nEnter a positive number for right shifting '
      '\nEnter a negatine number for left shifting')
k=int(input())
#===========MAIN PROGRAM==================================
#-----------Shift Right-----------------------------------
if k>0:
    print('Orjinal list:\n',my_numbers)
    my_numbers[:k],my_numbers[k:]=my_numbers[n-k:],my_numbers[:n-k]
    print('Shifted version',k,'times riht:\n',my_numbers)
#-----------Shift Left-----------------------------------
elif k<0:
    l=abs(k)
    print('Orjinal list:\n',my_numbers)
    my_numbers[n-l:],my_numbers[:n-l]=my_numbers[:l],my_numbers[l:]
    print('Shifted version',l,'times left:\n',my_numbers)
#-------------no shift
else:
    print('You entered zero. This means no shift.')
    my_numbers=list(range(n))
    print(my_numbers)
#=================END=====================================
#===========AN EXAMPLE OUTPUT=============================
# left shifting
#Enter the number of element in your list:10
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Enter how many shift you want: Enter a positive number for right shifting. Enter a negatine number for left shifting.
#-3
#Orjinal list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Shifted version 3 times left:
# [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

# right shiftting
# Enter how many shift you want:
# Enter a positive number for right shifting
# Enter a negatine number for left shifting
# 6
# Orjinal list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Shifted version 6 times riht:
# [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]


