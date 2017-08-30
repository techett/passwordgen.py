
'''

Coded by Techett
passwordGen v0.02
Last update: August 23, 2017

'''

import random, sys, pyperclip, time



characters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"
#Pull characters from this string



#number = 1
#number = int(1)
#This is how many passwords will be created.



length = 16
length = int(length)
#This is how the length of the password is determined.



for pwd in range(1):
	password = ''
	for c in range(length):
		password += random.choice(characters)
	pyperclip.copy(password)



print("Your password has been generated.")
print("Your password has been copied to your clipboard")
print(password)



print("Verify your password!")
print("Do so by right clicking the screen and then hit enter.")
answer = input()



while answer != password:
	print("To close this generator paste your password to confirm accuracy.")
	print("Do so by simply right clicking the screen.")
	answer = input()
else:
	print("That's it! Goodbye!")
	print("This generator will now close.")
	time.sleep(5)
	sys.exit()
