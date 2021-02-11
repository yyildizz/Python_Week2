"""Kullanıcıdan bir cümle girerken, sonra her harfin oluşum sayısını özetlemek için bir sözlük
kullanan bir kod parçacığı yazın. Büyük/küçük/küçük harf yoksay, boşlukları yoksay ve kullanıcının
herhangi bir noktalama işareti girmediğini varsayın. Harflerin ve sayılarısıralanmış sırayla
harflerin iki sütunlu bir tablosunu görüntüleyin.
 [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7),
 ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1),
 ('w', 4), ('x', 2)]"""
a= input("PLEASE ENTER THE TEXT : ").lower()
b= []
c= ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş",	"t", "u", "ü", "v", "y", "z"]
for i in a:
    if i not in b and i in c:
        b.append(i)
b.sort()
d=[]
for i in b:
    count = 0
    d.append(i)
    for e in a:
        if i == e:
            count += 1
    d.append(count)
print(d)