print('Enter a number to check if that is EVEN or not')

user_input = ""

while user_input != 'q':
    user_input = input('Enter a No. OR q for quit: ')
    if user_input.isdigit():
        if int(user_input) % 2 == 0:
            print('yes no. is EVEN')
        else:
            print('No. is ODD')



count = int(input('Enter the number :- '))

while 1 <= count:
    print(count)
    count -=1


count = int(input('Enter the number :- '))
abc = []
while count >= 1:
    count -=1
    abc.append(count+1)
print(sorted(abc))













