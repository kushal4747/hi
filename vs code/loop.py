# # # # n=int(input("enter your number "))
# # # # for i in range (1,11 ): 
# # # #     print(n,"*", i , "=" , n*i )
# # # total=0
# # # a=int(input("enter no."))
# # # for i in range (0,a+1):
# # #     total=total+i
# # # print ("sum=",total)
# # # # n = int (input ( "enter your number "))
# # # # for i in range (1 , n+2):
# # #     # print(i)
# # # # for i in range (1,6):
# # #     # print(i,  end= " ")
# # # for i in range(1,6):
# # #     print(i, end=",")
# # # total=1
# # # a=int(input("enter no."))
# # # for i in range (1,a+1):
# # #     total=total*i
# # # print ("factorial=",total)
# # # total=1
# # # i=1
# # # a=int(input("enter no.")) #a=5
# # # while i<=a:
# # #     total=total*i
# # #     i+=1
# # # print ("factorial=",total)
# # # for i in range (1,6):
# #     # print (i ** 2 , end = " ")
# # # for i in range (1,11):
# #     # if i%2==0:
# #         # print(i,end= " ")
# # #
# # # total=0
# # # for i in range (1,11):
# # #     total+=i
# # # #     print(f"sum of all numbers {total}")
# # # for i in range (1,5):
# #     # print(i.reverse ())
# # # for i in range (1,34):
# #     # print("*"* i)
# # # for i in range (1 , 8):
# #     # print("*" * i)
# # # for i in range (1,6):
# #     # for  j in range (1 ):
# #         # print(j, end = "")
# #     # print()
# # # while True:
# #     # print("hello")
# i=1
# n= int( input("enter no "))
# for i in range (1,n+1):
#     for j in range (i):
#         print ("*",end =" ")
#     print()

# # n = int(input("enter number :"))
# # fact = 1
# # i = 1

# # for i in range(1, n+1):
# #     fact = fact * i
# #     i = i+1

# # print(fact)




# # fact= 1
# # i=1
# # a= int(input("enter no."))
# # while i<=a:
# #     fact = fact*i
# #     i+=1
# # print(fact)

# # b = int(input("enter number:"))#b = 6
# # fact = 1
# # while i

# # r = 6
# # for i in range(1,6):
# #     for j in range(1,6):
# #         print("*",end=" ")
# #     print()

# b = int(input("enter number:"))

# fact = 1
# i = 1

# while b>=i:
#     fact = fact * i
#     i = i+1
# # print(fact)



# import pyjokes:
#     print(pyjokes.get_joke())

#a=16
# nums=(1,4,9,16,25,36,49,64,81,100)
# a=int(input("enter the number"))#a=36
# i=0
# while i<len(nums):
#     if a==nums[i]:
#         print("the no. found", i )
#     i+=1

# # print("computer"[: :-2] + "ai"[1: ])
# s="MISSISSIPPI"
# print(s.count("ISS"),s.find("SIP"),s.replace("I","1",2))


"""
name= input("enter name")
age=int(input("enter your age"))
student_status = input("enter your status pass or fail")
print("your name is : ",name , "\n your age is : ", age ,"\n student_status is : ",student_status)
print(type(name) ,"\n",type(age) ,"\n",type(student_status) )
"""

# x=int(input("enter no."))
# i=1
# while (i**2)<=x:
#     print(pow(i,2))
#     i+=1
# x= int(input("enter no."))
# while x>=0:
#     print()

            #Q to check wether elements are same or not 
# arr = (1,2,3,5,5,4,4)

# code here
# count=0
# for i in range(0,len(arr)+1):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print("False")
#             count+=1
#             break
#     if count>0:
#         # break
#         pass
# else:
#     print("True")
"""
x=10
def Add(a,b):
    sum=a+b
    global x
    x=x+10
    print(x)
    return sum

m=5
n=4
c=Add(m,n)
d=c/4
print(d)
def subs(a,b):
    subs=a-b
    return subs
k=subs(d,30)
print(k)
"""
# a=input("enter anythingh")
# b= len(a)
# print(f"length {b} \nuppercase{a.upper()} \nlowercase{a.lower()} \n{a.count("k")} \n{a.find("a")}")