import random

print("=== Aizen AI Chatbot ===")
print("Type 'bye' to exit.\n")

responses = {
    "hello": [
        "Hello! I am Aizen. How can I assist you today?",
        "Greetings! Aizen at your service.",
        "Hi there! What would you like to talk about?"
    ],
    "how are you": [
        "I'm functioning perfectly.",
        "All systems operational.",
        "Doing great! Thanks for asking."
    ],
    "your name": [
        "My name is Aizen.",
        "I am Aizen, your rule-based AI assistant."
    ],
    "help": [
        "I can answer simple questions and chat with you.",
        "Try asking about my name, the time, or just say hello."
    ],
    "time": [
        "I can't tell the exact time unless programmed with a clock module."
    ],
    "bye": [
        "Goodbye!",
        "See you later!",
        "Farewell!"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()

    for keyword, reply_list in responses.items():
        if keyword in user_input:
            return random.choice(reply_list)

    return "I don't understand that yet. Please teach me more rules."

while True:
    user_input = input("You: ")

    response = get_response(user_input)
    print("Aizen:", response)

    if "bye" in user_input.lower():
        break