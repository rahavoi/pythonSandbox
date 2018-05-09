#Reading from a file:

def dumbChatBot(filename):
	chatsLeft = 3
	botResponse = 'I\'m just a bot. Bear with me'
	with open(filename, 'a') as file_object:
		while(chatsLeft > 0):
			userInput = input("User:")
			file_object.write('User: ' + userInput + '\n')
			print("Bot: " + botResponse)
			file_object.write('Bot: ' + botResponse + '\n')
			chatsLeft = chatsLeft - 1
		print("We saved you fruitful conversation in the" + filename + " file.")


def printConversation(filename):
	with open(filename) as file_object:
		for line in file_object:
			print("### " + line)			


chatFile = "chat.txt"
dumbChatBot(chatFile)
printConversation(chatFile)
