def say_hi(name,age):
    print("Hello "+name+", you are "+age +" years old.")

name = input("Enter your name: ")
age = input("Enter your age: ")
say_hi(name,age)
#say_hi("Professor",10) --> because in say_hi fucntion age is taken as string but for int it is not typecasted to string
say_hi("Professor","10")
