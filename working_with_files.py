#Reading from a file:


def readFile():
	with open('pi_digits.txt') as file_object:
		contents = file_object.read()
		print(contents)

#readFile()		

def dumbChatBot(filename):
	chatsLeft = 10
	botResponse = 'Errrr...'
	with open(filename, 'w') as file_object:
		while(chatsLeft > 0):
			userInput = input("User:")
			file_object.write('User: ' + userInput + '\n')
			print("Bot: " + botResponse)
			file_object.write('Bot: ' + botResponse + '\n')
			chatsLeft = chatsLeft - 1
		print("We saved you fruitful conversation in the chats.txt file.")			


dumbChatBot('chat.txt')
