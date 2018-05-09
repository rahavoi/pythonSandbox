people = ['John Doe', 'Bill Gates', 'Donald Duck']
print(people)
print(people[0])

people[0] = 'chuck norris'
print(people)

people.append('chuck norrisX2')
print(people)

#Removing items from list with del:
del people[2]
print(people)


#Removing the last item from the list with pop:
popped = people.pop()
print(popped + " has been popped, as it was the last item in the list")

# You can pop an element at any position:
popSecond = people.pop(1)
print(popSecond)
print(people)

people.pop()

print(people)

people.append("Illia")
people.remove("Illia")
print(people)

#Cannot pop from empty list:emptypop = people.pop()

cars = ['subaru', 'bmw', 'audi', 'mercedes', 'tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


cars.reverse()
print(cars)
print(len(cars))


#  -1 returns the last item
print("Last item in the list: " + cars[-1])
