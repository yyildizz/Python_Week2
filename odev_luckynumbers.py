
# Lucky number

n=int(input("Write the number: "))

number=[i for i in range (1, n+1)]
print(number)
x=1
while (x<len(number)):
        del number[1:len(number):(x+1)]
        print ("Remove {} elements {} ".format(x+1,number))
        x+=1
    
print("Lucky numbers are {}".format(number))







