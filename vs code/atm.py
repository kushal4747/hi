# balance= 50000 b 
# while True:
#     option=input(""" ----ATM----
# (1) Withdraw
# (2) Check Balance
# (3) Deposit 
# (4) EXIT
# Enter """)
#     if option=="3":
#         deposit= int(input("Enter Amount To Deposit "))
#         print(f"UPDATED BALANCE IS {balance+deposit}")
#     if option=="2":
#         print(f"your current balance is {balance}")
#     if option=="1":
#         max=10000
#         pin= 1234
#         count=0
#         withdrawl=int(input("enter withdrawal amount "))
#         if withdrawl>0:
#             while count<3:
#                 pin_1=int(input("enter your pin "))
#                 if pin_1==pin:
#                     if balance>=withdrawl:
#                         remain=balance-withdrawl
#                         if remain<500:
#                             print("Minimun Balance must be 500")
#                             break
#                         if withdrawl>max:
#                             print(f"WARNING MAXIMUM WITHDRAWL LIMIT 10,000 ONLY")
#                             print(f"want to withdraw enter ")
#                             a=input("'Y OR N'")
#                             if a.lower()=="y":
#                                 balance= balance-max
#                                 print(f"remaining balance= {balance}")
#                             else:   
#                                 print("please exit your card")
#                             break   
#                         else:
#                             balance= balance-withdrawl
#                             print(f"the remaining balance = {balance}")
#                             break
#                 else:
#                     count+=1
#                     print(f"enter correct pin")
#                     if count==3:
#                         print(f"card blocked")
#         else:
#             print(f"Invalid withdrawal amount")
#     if option=="4":
#         print("exit")
#         break

# n=int(input("entter "))
# for i in range (n):
#     for j in range (n):
#         print("*",end=" ")
#     print()

# text = "abCdeF"
# for i in range(len(text)):
#     if text[i].islower():
#         print(text[i].upper(), end="")
#     else:
#         break

# a=int(input("enter no. "))
# count=0
# if a==0 or a==1:
#     print("not P nor NP")
# else:
#     for i in range (1,a+1):
#         if a%i==0:
#             count+=1
#     if count==2:
#         print("p")
#     else:
#         print("np")

# n=int(input("enter no."))
# for i in range(1,11):
#     print(n,"*",i,"=", i*n)


for i in range (5,0,-1):
    for j in range(5-i):
        print("", end="")
    for j in range(1,i+1):
        print(j, end=" ")
    print() 