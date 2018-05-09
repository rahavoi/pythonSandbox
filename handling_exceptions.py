import sys

#try except else
try:
	#sys.argv[0] is always the name of the program as it was invoked:
	#print(sys.argv[0])
	#args in Python start with 1:

	if len(sys.argv) != 3:
		raise ValueError("Illegal nunber of arguments: " + str(len(sys.argv) -1)) + "Must be 2"


	result = (float(sys.argv[1]) / float(sys.argv[2])) 
except ZeroDivisionError:
	print("You can't divide by zero!")
except ValueError as e:
	print(str(e))
	#Failing Silently with Pass
	pass	
else:
	print(result)		
