age={'Han': 24, 'Prag': 23, 'Bunyod': 18}
print(age)
print(age['Han'])
change ={'Prag': 30}
age.update(change)
print(age['Prag'])
del age['Bunyod']
print(age)