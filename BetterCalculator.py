num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
operator = input("Please Enter Operator: ")

if operator=='+':
    print(num1+num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
elif operator=='-':
    print(num1-num2)
else:
    print("Invalid Operator!")

