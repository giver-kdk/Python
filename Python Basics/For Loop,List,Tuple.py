# num=int(input("Enter a number"))
# ans=1
# if num<0:
#     print("Math Error")
# else:
#     for i in range(1,num+1):
#        ans=ans*i
#     print(ans)



# a=[1,2,3,4,5,6]                           #This is List
# for i in range(0,len(a)):
#     print(i)
# print(sum(i**2 for i in a))
# a.append(5)
# print(a)
# a.clear()
# print(a)
# del a
# print(a)



# a=(1,2,3,4,5,6)                           #This is Tuple
# del a
# print(a)


a=[1,1,3,4,5,6]
b=[1,2,3,4,5,6,7,8]
c=[]
for i in range(0,len(a)):
    if a[0] in b:
        c.append(a[0])
        b.remove(c[-1])
    a.remove(a[0])
print(c)


