friends = ["Souvik", "Animesh" , "Prince", "Tamoghono"]

#For loop for list
for friend in friends:
    print(friend)

#For loop using range
for index in range(10):  #Range gives the list of numbers excluding n where range(n) from 0 to n-1
    print(index)

#For loop using len of list
for friend in range(len(friends)):
    print(friends[friend])

#For loop for some complex logic
for index in range(5):
    if index ==0 :
        print("First Iteration")
    else:
        print("Not First Iteration")
