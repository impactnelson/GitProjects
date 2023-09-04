'''This program is to print a welcome message that is personalized for the user:

print("Testing Python")
'''
print("PROMPT:")
print('')
print("Write a Python program that takes the user's name as input and displays a personalized welcome message.")
print('')
#REQUIREMENTS:

print("•       Requirements:")
print('')
print("•       Prompt the user to enter their name")
print("•       Use the input to create a personalized greeting.")
print("•       Print the customized welcome message.")
print('')
print('')
userName = input('Please, Enter your name: ')

print('')
print("Hello, %s! You are welcome to this Platform! Feel free and comfortable, we hope to have a great time with you on this journey. Once more, you are welcome, %s" %(userName, userName))
print("")
print("Ok, %s. These are the various things we will be looking at in this journey. But before that,  %s we will like to know your age." % (userName, userName))
print('')
age = input('How Old are you?  ')
print('')
print(userName, 'You are %s years old!' % age)
print('')
print('::::::::::::::::::::::::')
print('')
print("Ok, Let's Proceed to the crux of this Journey!")
print('')
