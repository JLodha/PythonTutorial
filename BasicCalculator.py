num_1 = input("Enter your first number: ")
num_2 = input("Enter your second number: ")

result_string = num_1 + num_2
print(result_string) #This will concatenate the string since input() basically takes the input given as string

#To make the addition works we need to typecaste the input to int/float

print("After typecasting:")
result_string = float(num_1) + float(num_2)
print(result_string)
