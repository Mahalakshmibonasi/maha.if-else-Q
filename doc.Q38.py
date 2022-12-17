# age=int(input("enter the age"))
# if age>=60:
#     print("senior citizen")
# else:
#     print("no senior citizen")



# a="my name is sunitha"
# b=""
# c=[]
# for i in a:
#     if i!="":
#         b+=i
#     else:
#         break    
#     c.append(b)
# print(c)
# a="my name is sunitha"
# b=[]
# b.extend(a)
# d=[]
# print(b)

# # for i in range(len(b)):
# for j in range(len(b)):
#       if b[j]!=" ":
#         d.append(b[j])
#     #   else:
#     #      d.pop(b[j])
# print(d)


i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end='')
        b+=1
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1