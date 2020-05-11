def power(base, exponent):
    count = exponent
    ans = 1
    while count!=0 :
        ans = ans * base
        count = count - 1
        continue
    return ans

result = power(4,4)
print(result)

