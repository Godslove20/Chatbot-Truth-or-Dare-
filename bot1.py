def get_user_name():
    """Prompt user for their name and return it."""
    return input("Hello. My name is Daya. What is your name? ")

def greet_user(name, emoji="😃"):
    """Greet the user with their name and an optional emoji."""
    print(f"Nice to meet you, {name} {emoji}")

def introduce_bot():
    """Introduce the bot to the user."""
    print("My name is D.A.Y.A. I am known as a Digital Automated Yoc3 Artificial Intelligence.")
    print("I am here to offer services.")

def ask_question():
    """Ask the user if they are open to a question and return their response."""
    return input("Can I ask you a question? (Yes/No) ").strip().lower()

def prompt_game_choice():
    """Prompt the user to choose between 'Truth' or 'Dare'."""
    print('Would you like to play a game of "Truth" or "Dare"?')

def main():
    """Main function to handle user interaction."""
    user_name = get_user_name()
    greet_user(user_name)

    introduce_bot()

    game_question = ask_question()

    if game_question == "yes":
        prompt_game_choice()
    else:
        print("Alright! Let me know if you need anything else.")

if __name__ == "__main__":
    main()
