#Simple Calculator for Sum, Subtract, Divide, and Multiply 
print ("Enter only numbers or decimals")
first_num = (input("Enter the first number: "))
sign = input("enter the operator sign: '\n+ for addition', '\n- for subtraction', '\n* for multiplication', '\n/ for division': ")
second_num = (input("Enter the second number: "))

# if first_num is not float:
#     print ("you can only enter a number")
# elif sign is not ("+" or "-" or "/" or "*"):
#     print ("you can only enter one of the listed sign")
# elif second_num is not float:
#     print ("you can only enter a number")

if sign == "+":
    sum= float(first_num) + float(second_num)
    print("The Sum of both numbers: "+ str(sum))

elif sign == "-":
    sub = float(first_num) - float(second_num)
    print("The result of the first number minus the second number is: "+ str(sub))

elif sign == "/":
    div = float(first_num) / float(second_num)
    print("The division of the first number by the second number is: "+ str(div))

elif sign == "*":
    mult = float(first_num) * float(second_num)
    print("The product of both numbers is : "+ str(mult))