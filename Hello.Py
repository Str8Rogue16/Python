# This is a small conversational program in python that asks for your name and date of birth.

print('Hello!')
print() # This will create some space between the question to replicate a pause.

print('What is your name?')  # Asks for your name

myName= input()
print()

print('It is nice to meet you, ' + myName + '!') 

print()

print('The length of your name is: ') # This measures the length of the name given.
print(len(myName))

print()


print('What is your birth month? ')  # Asks for your birthdate
myBirthdate = input()

print()

print('I would like to know your favorite color,'+ "" + myName + "?") # This asks what their favorite color is. 
myColor = input()

print()

print(myColor + " " + 'That is a nice color! I prefer DodgerBlue myself!') # This is to create a more personal feel with the user.

print()

print('What do you do for a living' + "  "+ myName + "  " + '?') # This asks what profession the user does.
myProfession = input()

print()

print('How well do you like your job and do they pay you well enough,' + " "+ myName + '?') # This asks the user how well they like their job and pay.
myMoraleAndPay = input()

print()

print('Have you considered other jobs to make you happier,' + "  "+ myName + '?') # This asks if the user looked for newer jobs to make them even happier. Assuming they said they were happy.
myOtherOffer = input()

print()

print('It was great talking to you' + "  " + myName )

# Need to add more personal touches to this as I go on. 
