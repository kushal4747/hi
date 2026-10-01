# # # # # # # a= "hello i am vishwajeet kumar \nand i am from \"jharkhand\" \ni am a student of btech in computer science and engineering"
# # # # # # # print(a)
# # # # # # # name= input("enter your name: ")
# # # # # # # print(f"good morning , radhe radhe {name} ")


# # # # # # letter = '''Dear <|Name|>,
# # # # # # you are selected! in uniques batch 
# # # # # #          date <|Date|> '''
# # # # # # name = input("enter your name: ")
# # # # # # date = input("enter date: ")
# # # # # # print(letter.replace ("<|Name|>", name).replace("<|Date|>" , date ) )


# # # # # a= "hello  vishwajeet sahu "
# # # # # print(a.find("sahu"))

# # # # # a= int(input("enter your number: "))
# # # # # print("even" if a%2==0 else "odd")

# # # # # -------------------------------------------------------------------------------------------------------------

# # # # a= ["kushal", "sahu" , "4" , "7", "47"]
# # # # a.append("aayu")
# # # # # print(a)  
# # # # # a.pop(2)
# # # # # print(a)
# # # # # print(a[2])
# # # # # print(a.pop(3)) 
# # # # a.remove("sahu")
# # # # # print(a)
# # # # a=1
# # # # while a<=7:
# # # #     print(a ,".", "python" )
# # # #     a+=1
# # # i=1
# # # a=int(input("enter your number: "))
# # # while i<=10:
# # #     print(a,"*", i, "=", a*i)
# # #     i+=1
# # a=[1,4,9,16,25,36,49,64,81,100]
# # i=0
# # while i<=len(a)-1:
# #     print(a[i])
# #     i+=1
# a=(1,4,9,16,25,36,49,64,81,100,49)
# x=int(input("enter the no. x which you want to find?" ))
# i=0
# while i<len(a):
#     if a[i]==x:     
#         print("found at index", i)
#     i+=13
n= int ( input ( " enter your number "))
for i in range ( 1,11):
    print (n, "*",i, "=" , n*i)
