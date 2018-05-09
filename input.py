import webbrowser

attempts_left = 3

def goTo(attempts_left):
	website = input("Pick a website:\n")
	print("Going to " + website)
	webbrowser.open(website)



while attempts_left > 0:
	goTo(attempts_left)
	attempts_left = attempts_left - 1
	print("attempts_left: " + str(attempts_left))

print("Game over")