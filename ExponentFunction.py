def power_f(base,exponent):
    result =1
    for index in range(exponent):
        result = result * base
    return result

base = int(input("Enter Base: "))
exponent = int(input("Enter Exponent: "))
ans = power_f(base,exponent)
print(ans)
