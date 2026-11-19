def get_reply(user_input):
    message = user_input.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    if "how are you" in message:
        return "I'm fine, thanks!"
    if message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    if "your name" in message:
        return "I'm a simple Python chatbot."
    if "thank" in message:
        return "You're welcome!"

    return "Sorry, I don't understand. Try saying hello, how are you, or bye."


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print(f"Chatbot: {reply}")

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    run_chatbot()
