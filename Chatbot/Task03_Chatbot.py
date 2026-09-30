import random
from datetime import datetime

print("=" * 50)
print("             PYTHON CHATBOT")
print("=" * 50)

print("Bot: Hello! I am CodeAlpha Bot.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to exit.")

responses = {

    "hello": [
        "Hello! 👋",
        "Hi there!",
        "Hey! How can I help you?"
    ],

    "hi": [
        "Hi! 👋",
        "Hello!",
        "Hey!"
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine, thanks!",
        "I'm ready to help!"
    ],

    "name": [
        "My name is CodeAlpha Bot.",
        "You can call me CodeAlpha Bot."
    ],

    "help": [
        "You can say hello, ask my name, ask how I am, or type time."
    ],

    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ]
}


while True:

    user_input = input("\nYou: ").lower().strip()

    # Exit
    if user_input == "bye":

        print("Bot:", random.choice(responses["bye"]))
        break

    # Greeting
    elif user_input in ["hello", "hi", "hey"]:

        print("Bot:", random.choice(responses["hello"]))

    # How are you
    elif "how are you" in user_input:

        print("Bot:", random.choice(responses["how are you"]))

    # Name
    elif "name" in user_input:

        print("Bot:", random.choice(responses["name"]))

    # Help
    elif user_input == "help":

        print("Bot:", random.choice(responses["help"]))

    # Time
    elif "time" in user_input:

        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Unknown
    else:

        print(
            "Bot: Sorry, I don't understand that yet."
        )