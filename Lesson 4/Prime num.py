num=int(input("Enter a number: "))
flag = False
for i in range(2,num):
    if num%i==0:
        flag=True
 
if flag:
     print(num, "is not prime")       
else:
    print(num, "is prime")