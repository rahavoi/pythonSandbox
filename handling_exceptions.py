import sys

#try except else
try:
	#sys.argv[0] is always the name of the program as it was invoked:
	#print(sys.argv[0])
	#args in Python start with 1:
	result = (float(sys.argv[1]) / float(sys.argv[2])) 
except ZeroDivisionError:
	print("You can't divide by zero!")
except ValueError:
	#Failing Silently with Pass
	pass	
else:
	print(result)		
