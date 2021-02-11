# Furkan Surucu
'''
Write a programme to generate the lucky numbers from the range(n).
These are generated starting with the sequence s=[1,2,...,n].
At the first pass, we remove every second element fromthe sequence, resulting in s2.
At the second pass, we remove every third element from the sequence s2, resulting in s3,
and we proceed in this way until no elements can be removed.
The resulting sequence are the numbers lucky enough to have survived elimination.
'''

n = int(input("Enter a number"))
original_sequence = list(range(1,n+1))
print(original_sequence)
i=1
while i < n+1:
    del original_sequence[i:n:i+1]
    i+=1
print("Lucky numbers are",original_sequence)