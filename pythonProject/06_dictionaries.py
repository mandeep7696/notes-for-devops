marks ={ 'hindi':80, 'English':90, 'Math':70 }
print(marks)
print(marks['English'])
print(marks.get('science'))

marks['Science'] = 99.9
print(marks)

del marks['hindi']

print(marks)

print(len(marks))



