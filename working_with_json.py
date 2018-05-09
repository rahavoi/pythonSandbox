import json

filename = "numbers.json"
numbers = [1,3,5,6,8,9,0,0,-2.1,]
with open(filename, 'w') as file_obj:
	json.dump(numbers, file_obj)


with open(filename) as file_obj:
	numbers = json.load(file_obj)

print(numbers)