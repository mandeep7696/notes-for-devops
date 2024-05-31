
if 10>8:
    print('hey it is true')
else:
    print('hey it is false')

print(10>5)
print(10==9)
print(10==10)


# even and odd number program

print('Enter a number to check if that is EVEN or not')
num= int(input('Enter a no -'))
if num % 2 == 0:
    print('yes no. is EVEN')
else:
    print('No. is ODD')



# user name finding

users = ['paul', 'raju','mohit', 'ravi']

if 'pauly' in users:
    print('user exist')
else:
    print('user does not exist')



# list is empty or not empty

users = ['paul', 'raju','mohit', 'ravi']

if  users:
     print('List is not empty')
else:
     print('list is empty')




# elif  program  for marks check

marks = int(input('Enter total marks: '))

if marks >= 80:
    print('A Grade')
elif marks >= 60:
    print('B Grade')
elif marks >= 40:
    print('c Grade')
else:
    print('!!!!!!! FAILED !!!!!!!!')

# nested if-else
age = int(input('Enter your age :- '))
voter_id = False

if age >= 18:
    if voter_id:
        print('Yes!! you can vote')
    else:
        print('Please apply for Voter ID first')
else:
    print('you cannot vote !!! ')