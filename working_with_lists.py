def fizzBuzz():
	for i in range(1, 100):
		if i % 15 == 0:
			print("FizzBuzz: " + str(i))
		if i % 5 == 0:
			print("Buzz: " + str(i))	
		if i % 3 == 0:
			print("Fizz: " + str(i))	
		else:
			print(i)		


def playingWithList():
	my_foods = ["beer", "steak", "sushi", "coffee"]

	#copying a list by making a slice without providing boundaries:
	copy_food = my_foods[:]

	copy_food.append("chocolate")
	copy_food.sort()

	print(copy_food)


def tupleExample():
	#tuples in Python are immutable lists:
	#Declaration: use parentheses instead of square brackets.
	languagesIKnow = ("English", "Russian", "Java", "Belarusian", "Kotlin", "Scala", "Python")

	if "Java" in languagesIKnow:
		print("java rules!")

	if "Erlang" not in languagesIKnow:
		print("You should learn erlang!")	

	for lang in languagesIKnow:
		print(lang)


	#Can't do this: tuple' object does not support item assignment
	#languagesIKnow[0] = "Erlang"

#fizzBuzz()
#playingWithList()

tupleExample()