friends = ['Souvik','Animesh','Prince','Tamoghono']
lucky_numbers = [1,2,3,4,5,6,7,8,9,10]

print(friends)

#Extending the friends list
friends.extend(lucky_numbers)
print(friends)

#Adding individual elements to list
friends.append("Anurag")
print(friends)

#Adding individual element at specific position
friends.insert(1,"Mridul")
print(friends)

#To remove element
friends.remove("Mridul")
print(friends)

#Pop
friends.pop()
print(friends)

#Find element
print(friends.index("Animesh")) #Returns Index
#print(friends.index("Mike"))  --> Returns Value Error as mike is not present in the list

#Count of element
print(friends.count("Souvik"))

#Sort
#friends.sort() --> Works only for uni-type data list
print(friends)

#Reverse
friends.reverse()
print(friends)

#Copy
friends2 = friends[2:]
friends3 = friends.copy()
print(friends2)
print(friends3)

#To clear list
friends.clear()
print(friends)