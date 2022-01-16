num=int(input("Enter the term u want to see"))
a=1
b=1
c=1
for i in range(1,num+1):
    print(a)
    d=a+b+c
    a=b
    b=c
    c=d
print(a)


    