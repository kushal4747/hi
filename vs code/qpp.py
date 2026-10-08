# sum_even=0
# sum_odd=0
# for i in range (2,101,2):
# 	sum_even+=i
# print(sum_even)
# for i in range (1,101,2):
# 	sum_odd+=i
# print(sum_odd)
# total=sum_odd-sum_even
# print(total)


# count=0
# word = "rhythmpalindrome"
# for i in word:
# 	if i=="a" or i=="e" or i=="i" or i=="o" or i== "u":
# 		count+=1
# print(count, "no. of vowel")
# a=len(word)-count
# print("no. of con.",a)

# word = "allochalooo"

# print(word[-1] + word[1:-1] + word[0])

# a=1
# for i in range(1,5):
# 	for j in range (1,i+1):
# 		print(a,end=" ")
# 		a+=2
# 	print()
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range (3,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# a=5
# for i in range(1,6):
#     for j in range(2*(a-i)):
#         print(" ",end="")
#     for j in range(i):
#         print("* " ,end="")
#     print()
# a , rev , s_um = int(input("enter no.")) , 0,0
# d=a
# b=str(a)
# c=len(b)
# while a>0:
#     dig=a%10
#     rev=dig**c
#     a//=10
#     s_um+=rev
# print(s_um)
# if s_um==d:
#     print("ang")
# else:
#     print("not")

# x=-17%5
# print(x)
# print(not 5)

# a= int(input("enter no. of rows"))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if j==1 or i==1 or j==a or i==a:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=int(input("enter no of rows"))
# for i in range (n,0,-1):
# 	for j in range(i):
# 		print("*", end=" ")
# 	print()


# n=5
# for i in range(5,0,-1):
# 	for j in range(1,i+1):
# 		print(j, end=" ")
# 	print()


# n=int(input("enter no. of rows "))
# a=1
# for i in range(1,n+1):
# 	for j in range(i):
# 		print(a, end=" ")
# 		a+=1
# 	print()

# x, y = 5, 2   #x=5 , y=2
# while x > 0:  #true 
#     if x % y == 0:
#         x -= 2  #x=2
#     else:
#         x -= 1  #x=4
#     print(x * y) #4*2=8
"""
    #ans :- 
    8
    4
    0

"""
#Write a code to count vowels in a string and replace all spaces with hyphens using a loop.
a=input("enter anything")
count=0
b=a.strip()
c=b.replace(" ", "-")
for i in b:
    if i=="a" or i=="e"  or i=="i" or i=="o" or i=="u":
        count+=1
print(count, "no. of vowels")
print(c)




