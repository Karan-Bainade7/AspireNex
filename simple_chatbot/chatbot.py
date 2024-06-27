# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitive matching

    # Define responses for different patterns
    responses = {
        "greetings": ["hello", "hi", "hey", "good morning", "good evening", "howdy"],
        "farewells": ["bye", "goodbye", "see you", "take care"],
        "about": ["what can you do", "who are you", "tell me about yourself", "what are you"],
        "thanks": ["thank you", "thanks", "appreciate it", "grateful"]
    }

    # Matching user input with patterns
    if any(greeting in user_input for greeting in responses["greetings"]):
        return "Hello! How can I help you today?"
    elif any(farewell in user_input for farewell in responses["farewells"]):
        return "Goodbye! Have a great day!"
    elif any(about in user_input for about in responses["about"]):
        return "I am a simple chatbot. I can respond to basic queries and hold a simple conversation."
    elif any(thank in user_input for thank in responses["thanks"]):
        return "You're welcome! If you have more questions, feel free to ask."
    else:
        return "I'm not sure how to respond to that. Can you please rephrase your question?"

def main():
    print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
