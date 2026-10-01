# i=0
# while i<=20:
#     if i%2!=0:
#         i+=1
#         continue
#     print(i)
#     i+=1
# a=(1,4,9,16,25,36,49,64,81,100)
# x=16
# idx=0
# for i in a:
#     if i==x:
#         print("found" , i , a.index(i))
#         print(idx)
#     idx+=1
# a= int(input("enter the no." ))
# for i in range(1,11):
#     print(a,"*", i ,"=", a*i)
# a= int(input("enter the no." ))
# i=1
# while i<=10:
#     print(i*a)
#     i+=1
# a=int(input("enter no."))
# sum =0
# for i in range(a+1):
#     sum+=i #sum = sum + i
# print ("total sum is :", sum)

# a=int(input("enter no."))
# i=1
# sum=0
# while i<=a:
#     sum+= i
#     i+=1
# print ("total sum:" , sum)

# # #factorial

# a=int(input("enter no."))
# sum=1
# for i in range(1,a+1):
#     sum=sum*i
# print ("factorial", sum)

# a=int(input("enter no."))
# i=1
# sum = 1
# while i<=a:
#     sum = sum*i
#     i+=1
# print ("factorial is :" , sum )
# a=int(input ("enter no."))
# sum =0
# i=0
# while i<=a:
#     sum += i
#     i+=1
# print ("total sum: ", sum)
#
# a=int(input("enter no."))
# sum =1
# i=1
# while i<=a:
#     sum = sum*i
#     i+=1
# print("factorial:", sum)
# for i in range (1 ,51):
#     # if i!=7 or i==21 or i==45:
#     #     continue
#     # else:
#     #     print(i)



# a= int(input("enter no."))
# for i in range(1,a+1):
#     for j in range (a-i):
#         print(" ", end="")
#     for j in range(2*i-1):
#         if j==0 or j==2*i-2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range (a-1,0,-1):
#     for j in range(a-i):
#         print(" ", end="")
#     for j in range(2*i-1):
#         if j ==0 or j==2*i-2:
#             print("*",end="")
#         else:
# #             print(" ", end="")
#     print()


# a=int(input("enter no."))
# for i in range (a):
#     for j in range(a):
#         if i==0 or i==a-1 or j==0 or j==a-1:
#             print("radhe", end=" ")
#         else:
#             print(" ", end="     ")
#     print()


# for i in range(a,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(0,a):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()


# a=int(input("enter no."))#a=5
# for i in range(1,a):
#     for j in range (a-i):
#         print("*",end=" ")
#     for j in range (2*i-1):
#         print(" ", end=" ")
#     print()
# for i in range(a,0,-1):
#     for j in range (a-i):
#         print("*",end=" ")
#     for j in range(2*i-1):
#         print(" ", end=" " )
#     print()

# n = int(input ("enter your number "))
# for i in range (1,n+1):
#     for j in range (n-1):
#         print (" ", end=" ")
#     for j in range (i):
#         print("*", end = " ")
#     print()

# print(pow(5,3))
# print((abs(-0.57))
# to find leap year  
# a=int(input("enter any year: "))
# if a%4==0:
#     print("leap year")
# elif a%400==0:
#     print("leap")
# elif a%100==0:
#     print("not leap")
# else:
#     print("not leap")
