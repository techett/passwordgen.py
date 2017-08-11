#Created by Techett/Anthemius

import random, sys, pyperclip
#end of imports

print('Hello, who are you?')
myName = input()
print('Oh, hello ' + myName + '!')
#end of greeting

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321*&^%$#@!'
#end of character list

number = 1
number = int(1)
#how many passwords to generate

length = 16
length = int(16)
#how long the password will be

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    pyperclip.copy(password)
#end of random module

print(myName + ', your password has been created.')
print(password)
print('Your password has been copied to your clipboard!')
#end of notification

answer = ''
while answer != password:
    print('To close this program please paste the password and hit enter.')
    print('Do so by right clicking the screen.')
    answer = input()
else:
    print('Goodbye.')
    sys.exit()
#end of program close
