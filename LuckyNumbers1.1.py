# Developer: Furkan Turkmen
# Date     : 11.02.2021
#Purpose of Software: Reinforcement of learned Python Code and Self improvement.
#What does program do: This programme to generate the lucky numbers from the range(n).
# At the first pass, we remove every second element fromthe sequence, resulting in s2.
# At the second pass, we remove every third element from the sequence s2, resulting in s3, and
# we proceed in this way until no elements can be removed. The resulting sequence are the numbers
# lucky enough to have survived elimination.

print("Generate Lucky Numbers")
number = int(input("Please enter the range: "))
luckynumber = [x for x in range(number+1)]    
luckynumber.pop(0)

for x in range(1, len(luckynumber)+1):

    i = 1
    while i <= len(luckynumber):
        if x*i >= len(luckynumber):
            break
        luckynumber.pop(x*i)
        i += 1
print("Your Lucky Numbers are ", luckynumber)


