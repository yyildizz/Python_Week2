"""Write a program that takes two inputs; one of them is a list and the other is a number,
and returns the list obtained by shifting the elements in the list n places to the right (left)
when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list,
then continue to shift starting at the beginning of the list.
Example:
Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3]
Inputs>>> [1, 2, 3, 4, 5], -2
Output>>> [3, 4, 5, 1, 2]"""
x= []
while True:
    a = input("What Kind Of Do You Want To Create List (String or Number) : ")
    cevap1 = str.lower(a)
    if cevap1 == "string" :
        b= int(input("How Many List Elements Do You Want to Add : "))
        for c in range(b):
            print(c+1, ". Element : ", end=" ")
            d= input()
            x.append(d)
            if len(x)==b:
                break
        break
    elif cevap1 == "number":
        print("Enter The Number List Range...", end=" ")
        b = int (input("Small Number : "))
        c = int (input("Big Number : "))
        if b<c :
            for d in range(b,c+1):
                x.append(d)
            break
        else:
            print("İncorrect İnput. Please Again Log İn")
            continue
    else:
        continue
print("Your List = ",x)
while True:
    f= input("Do You Want to Scroll The List From The Top or Backwards : ")
    cvp = str.lower(f)
    if cvp == "top":
        g = int (input("From Item : "))
        son1= x [:g]
        son2= x [g:]
        son3 = son2+son1
        print("Your List:",son3)
        break
    elif cvp == "backwards":
        g = input("From Item : -")
        l= int("-" + g)-1
        son1= x[:l]
        son2= x[l:]
        son3 = son2+son1
        print("Your List:",son3)
    else:
        continue