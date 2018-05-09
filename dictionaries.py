person = {'name' : 'Illia', 'age': 31, 'title' : 'sde'}

print(person)

person['status']  = 'active'

#removing:
del person['title']

print(person)


#Looping through a dictionary:

#Order is not guaranteed, same as Map in Java. But you can sort keys, if you need
for key in sorted(person.keys()):
	print("A key: " + key)

for value in person.values():
	print("A value: " + str(value))	

for key, value in person.items():
	print('####' + key + ':' + str(value) + '####')