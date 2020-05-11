#2D Lists

number_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_lists[1][1])
print(len(number_lists))
print(len(number_lists[1]))

#Nested For Loops

print("Printing the elements line by line of 2D List: ")
for index_row in range(len(number_lists)):
    for index_column in range(len(number_lists[index_row])):
        print(number_lists[index_row][index_column])

#OR:

# for row in number_lists:
#   for col in row:
#       print(col)


print("This is the end of the 2D Nested List")
