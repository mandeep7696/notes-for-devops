# # fizz buzz
# print('Fizz Buzz program')
#
# till_num = int(input('Enter the specified number: '))
# my_list = []
#
# for num in range(1, till_num+1):
#     xyz = ""
#     if num % 3 == 0:
#         xyz = xyz + 'Fizz'
#         if num % 5 ==0:
#             xyz = xyz + 'Buzz'
#     elif num % 5 == 0:
#         xyz = xyz + 'Buzz'
#     else:
#         xyz = num
#     my_list.append(xyz)
#
# print(my_list)




















abc = int(input('Enter the number :- '))
nm_abc = []

for nm in range(1, abc+1):
    xyz = " "
    if nm % 3 == 0:
        xyz = xyz + 'fizz'
        if nm % 5 == 0:
            xyz = xyz + 'Buzz'
    elif nm % 5 == 0:
        xyz = xyz + 'Buzz'

    else:
         xyz =nm
    nm_abc.append(xyz)

print(nm_abc)














