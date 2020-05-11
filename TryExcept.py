
try:
    infinity = 10/0
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
except:
    print("Undefined Error!")


try:
    ex = int(input("Enter a number: "))    #For checking the exceptions provide a string instead of a number here
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
except:
    print("Undefined Error!")
