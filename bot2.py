#Ask for user's name
user_name = input('Hello. My name is Daya. What is your name?')

#Make user response a function
def user_name_response(name, emoji):
  print(f'Nice to meet you {user_name}{emoji}')

#Add emoji for warm welcome
user_name_response({user_name}, '😃')

#Introdcuing the bot
print('My name is D.A.Y.A. I am known as a Digital Automated Yoc3 Artificial Intelligence.Here to offer services')

#Asking a question
game_question = input('Can I ask you a question? (Yes/No) ')

# Function to prompt user response
def user_response():
    print('Type "Yes" or "No".')

if game_question.lower() == "yes":
    # Introducing the game
    print('Would you like to play a game of "Truth" or "Dare"?')

    # Asking for response
    user_response()
else:
    print('Alright! Let me know if you need anything else.')

