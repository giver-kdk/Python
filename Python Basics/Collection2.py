# num=int(input("Enter the term u want to see"))             #series
# a=1
# for i in range(1,num+1):
#     print(a)
#     a=a+i
# print(a)
# num=int(input("Enter the term u want to see"))              #8888 series
# a=8
# for i in range(1,num):
#     print(a)
#     b=(a*10)+8
#     a=b
# print(a)
# a=range(1,45)                       #list
# for i in range(0,len(a)):
#     if a[i]%3==0 or a[i]%5==0:
#         print(a[i])
# a=int(input("Enter a number to see divisor:"))                  #divisor from loop
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)


a=[1,2,3,4,5,6]                     #sum of squares
b=0
for i in range(0,len(a)):
    b=a[i]**2+b
print(b)   