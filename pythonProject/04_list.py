# list stor multi value
user_list = ['alex', 'raju', 'sham', 'baburao']
print(user_list)
print(user_list[0])
print(user_list[1])
print(user_list[-1])

# add new name for list
user_list.append('paul')
print(user_list)

# delete value from a list

user_list.remove('alex')

print(user_list)

# modify value from a list

user_list[2] = 'Baburao'

print(user_list)

# adding item to a list at given position

user_list.insert(1, 'shanu')
print(user_list)

# sorting the items in list
user_list.sort()
print(user_list)

user_list.sort(reverse=True)
print(user_list)

# poping the items in list
user_list.pop()
print(user_list)

user_list.pop(2)
print(user_list)

####
print(user_list.pop())


###
removed_value = user_list.pop(1)

print(removed_value)
print(user_list)

# range of value

print(user_list[0:3])


###

marks = [42, 56, 55, 96, 56.2, 24, 84.5, 78, 45, 97]

print(marks)
print (min(marks))
print(max(marks))
print(sum(marks))
print(sorted(marks))
