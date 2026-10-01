a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for multiplication")
print("enter 4 for division")
c= int(input("Enter your choice: "))
if c==1:
    print("The sum is: ", a+b)
elif c==2:
    print("the subtraction is: ", a-b)
elif c==3:
    print("the multiplication is: ", a*b)
elif c==4:
    print("the division is: ", a/b)
else:
    print("Invalid choice")
    