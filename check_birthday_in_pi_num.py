filename = "3.14.txt"

with open(filename) as file_obj:
	lines = file_obj.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

#print(pi_string)
birthdate = 'ddmmyyyy'
attempts = 0

while(birthdate not in pi_string):
	if attempts > 0:
		print('Your birthday does not appear in the first million digits of pi. Try again :)')
	attempts += 1	
	birthdate = input("Enter your birthday in mmddyy format: ")

print("Your birthday " +  birthdate + " appears in the first million digits of pi!")
print("It took you " + str(attempts)  + " attempt(s).")