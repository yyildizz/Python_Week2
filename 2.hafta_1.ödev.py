"""Write a programme to generate the lucky numbers from the range(n). These are generated starting with
the sequence s=[1,2,...,n]. At the first pass, we remove every second element fromthe sequence,
resulting in s2. At the second pass, we remove every third element from the sequence s2, resulting in
s3, and we proceed in this way until no elements can be removed. The resulting sequence are the numbers
lucky enough to have survived elimination. The following example describes the entire process for n=22:
Original sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
Remove 2nd elements: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
Remove 3rd elements: [1, 3, 7, 9, 13, 15, 19, 21]
Remove 4th elements: [1, 3, 7, 13, 15, 19]
Remove 5th elements: [1, 3, 7, 13, 19]
We cannot remove every other 6th element as there is no 6th element. Input>>> 22
Output>>> Lucky numbers are [1, 3, 7, 13, 19]"""
m_1 = int(input("Which Numbers Do You Want to Find Lucky Numbers Between? (Small Number) :"))
m_2 = int(input("Big Number :"))
x = []
for a in range (m_1, m_2):
    x.append (a)
print(x)
y = 1
z = int (len (x) / 2)
for b in range (z) :
    x.remove(x[y])
    y += 1
print(x)
y = 2
z = int (len (x) / 3)
for c in range (z) :
    x.remove(x[y])
    y += 2
print(x)
y = 3
z = int (len(x)/4)
for d in range (z) :
    x.remove(x[y])
    y += 3
print(x)
y = 4
z = int (len(x)/5)
for e in range (z) :
    x.remove(x[y])
    y += 4
print(x)
y = 5
z = int (len(x)/6)
for f in range (z) :
    x.remove(x[y])
print(m_2,"-",m_1 , "lucky numbers among their numbers:", x)
