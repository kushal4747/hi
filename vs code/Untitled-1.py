# # i=0
# # while i<=20:
# #     if i%2!=0:
# #         i+=1
# #         continue
# #     print(i)
# #     i+=1
# # a=(1,4,9,16,25,36,49,64,81,100)
# # x=16
# # idx=0
# # for i in a:
# #     if i==x:
# #         print("found" , i , a.index(i))
# #         print(idx)
# #     idx+=1
# # a= int(input("enter the no." ))
# # for i in range(1,11):
# #     print(a,"*", i ,"=", a*i)
# # a= int(input("enter the no." ))
# # i=1
# # while i<=10:
# #     print(i*a)
# #     i+=1
# # a=int(input("enter no."))
# # sum =0
# # for i in range(a+1):
# #     sum+=i #sum = sum + i
# # print ("total sum is :", sum)

# # a=int(input("enter no."))
# # i=1
# # sum=0
# # while i<=a:
# #     sum+= i
# #     i+=1
# # print ("total sum:" , sum)

# # # #factorial

# # a=int(input("enter no."))
# # sum=1
# # for i in range(1,a+1):
# #     sum=sum*i
# # print ("factorial", sum)

# # a=int(input("enter no."))
# # i=1
# # sum = 1
# # while i<=a:
# #     sum = sum*i
# #     i+=1
# # print ("factorial is :" , sum )
# # a=int(input ("enter no."))
# # sum =0
# # i=0
# # while i<=a:
# #     sum += i
# #     i+=1
# # print ("total sum: ", sum)
# #
# # a=int(input("enter no."))
# # sum =1
# # i=1
# # while i<=a:
# #     sum = sum*i
# #     i+=1
# # print("factorial:", sum)
# # for i in range (1 ,51):
# #     # if i!=7 or i==21 or i==45:
# #     #     continue
# #     # else:
# #     #     print(i)



# # a= int(input("enter no."))
# # for i in range(1,a+1):
# #     for j in range (a-i):
# #         print(" ", end="")
# #     for j in range(2*i-1):
# #         if j==0 or j==2*i-2:
# #             print("*", end="")
# #         else:
# #             print(" ", end="")
# #     print()
# # for i in range (a-1,0,-1):
# #     for j in range(a-i):
# #         print(" ", end="")
# #     for j in range(2*i-1):
# #         if j ==0 or j==2*i-2:
# #             print("*",end="")
# #         else:
# # #             print(" ", end="")
# #     print()


# # a=int(input("enter no."))
# # for i in range (a):
# #     for j in range(a):
# #         if i==0 or i==a-1 or j==0 or j==a-1:
# #             print("radhe", end=" ")
# #         else:
# #             print(" ", end="     ")
# #     print()


# # for i in range(a,0,-1):
# #     for j in range(i):
# #         print("*",end="")
# #     print()
# # for i in range(0,a):
# #     for j in range(0,i+1):
# #         print("*",end="")
# #     print()

# # n = int(input ("enter your number "))
# # for i in range (1,n+1):
# #     for j in range (n-1):
# #         print (" ", end=" ")
# #     for j in range (i):
# #         print("*", end = " ")
# #     print()

# # print(pow(5,3))
# # print((abs(-0.57))
# # to find leap year  
# # a=int(input("enter any year: "))
# # if a%4==0:
# #     print("leap year")
# # elif a%400==0:
# #     print("leap")
# # elif a%100==0:
# #     print("not leap")
# # else:
# #     print("not leap")
# # a=int(input(""))
# # print(not(a>=20 and a<=50))


# # for i in range(a,0,-1):
# #     for j in range (a-i):
# #         print("*",end=" ")
# #     for j in range(2*i-1):
# #         print(" ", end=" " )
# #     print()

# # a= int(input("enter no of rows "))
# # for i in range (1,a+1):
# #     for j in range (a-i):
# #         print(" ",end=" ")
# #     for j in range (2*i-1):
# #         print("*",end=" ")
# #         # if j==0 or j==2*i-2:
# #         #     print("*",end=" ")
# #         # else:
# #         #     print(" ", end=" ")
# #     print()
# # # print("* "*(2*a-1))
# # for i in range (a-1,0,-1):
# #     #space
# #     for j in range (a-i):
# #         print(" ",end=" ")
# #         #star 
# #     for j in range(2*i-1):
# #         print("*",end=" ")
# #         # if j==0 or j==2*i-2:
# #         #     print("*",end=" ")
# #         # else:
# #         #     print(" ", end=" ")
# #     print()


# """
# 6 = out of 4 /4 marks
# 7 marks each 3 out of 2 (projects)"""
# # a=int(input("enter no"))
# # for i in range (a,0,-1):
# #     for j in range (a-i):
# #         print(" ",end=" ")
# #     for j in range(1,i+1):
# #         print("*",end=" ")
# #     print()


# # # a=int(input("enter no"))
# # for i in range (a,0,-1):
# #     for j in range(i):
# #         print("*",end=" ")
# #     print()
# # a=int(input("enter no"))
# # for i in range(1,a+1):
# #     for j in range(a-i):
# #         print(" ",end=" ")
# #     for j in range (2*i-1):
# #         print("*",end=" ")
# #     print()
# a=int(input("enter no"))
# for i in range(1,a):
#     for j in range (a-i):
#         print(" ", end=" ")
#     for j in range (2*i-1):
#         if j==0 or j==(2*i-2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print("* "*(2*a-1))


# name = "abhinav"
# rev =""
# for i in range(len(name)-1,-1,-1):
#     rev+=name[i]
# print(rev)
# if name == rev:
#     print("p")
# n= input("enter no")
# b=n.index()
# print(b)
# num = input("Enter number: ")

# i = 0
# count = 0

# while num[i:]:
#     if num[i].isdigit():
#         count += 1
#     i += 1

# print("Number of digits:", count)
# a=int(input("enter no"))
# sum=1
# for i in range(1,a+1):
#     sum*=i
# print(sum)
# a=int(input("enter no"))
# sum=0
# while a>0:
#     digit=a%10
#     sum=(sum*10)+digit
#     a//=10
# print(sum)

n=int(input("enter no. of patients: "))
for p in range(1,n+1):
    print("patent",p)
    ward=input("""
    1: General Rs.1000/day
    2: Private Rs.3000/day
    choose """)
    days=int(input("enter no. of days : "))
    if (ward=="1"):
        bill=days*1000
        if days>10:
            dis=bill-(bill*(15/100))
        elif days>=5 and days<=10:
            dis=bill-(bill*(10/100))
        print(dis)
    elif (ward=="2"):
        bill=days*3000
        if days>10:
            dis=bill-(bill*(15/100))
        elif days>=5 and days<=10:
            dis=bill-(bill*(10/100))
        print(dis)
    else:
        print("choose correct option ")
    meal_c=input("enter Y or N for meal ")
    c=meal_c.lower()
    if c=="y":
        meal=float(input("enter price of meal "))
        no_meal=int(input("enter no. of meal "))
        price=meal*no_meal
        di=dis+price
        gst= 12*(di/100)
        print(di, "total final price ")
        print(gst,"12% gst of final bill")
    else:
        c=dis
        gst=12*(c/100)
        print(c, "final bill ")
        print(gst,"12% gst of final bill")
        print("thank you ")