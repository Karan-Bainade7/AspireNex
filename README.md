# AspireNex
Project Outline: Simple Rule-Based Chatbot
1.	Setup: Create a project directory and a Python file.
2.	Input Handling: Capture user input and process it.
3.	Keyword Matching: Identify patterns in the user input.
4.	Predefined Responses: Provide responses based on matched patterns.
5.	Loop for Continuous Interaction: Keep the conversation going until the user decides to exit.
Explanation of the Code
1.	Function chatbot_response(user_input):
o	Lowercase Conversion: user_input = user_input.lower() ensures case-insensitivity.
o	Pattern Matching: The function checks if the user input contains any keywords from predefined patterns (greetings, farewells, about, thanks).
o	Response Selection: Returns an appropriate response based on the matched pattern.
2.	Function main():
o	Welcome Message: Greets the user.
o	Input Loop: Continuously takes user input until the user types 'exit'.
o	Exit Condition: Ends the conversation if the user types 'exit'.
o	Prints Responses: Calls chatbot_response to get the response and prints it.
3.	Entry Point:
o	if __name__ == "__main__": main() ensures that main() is called when the script is run directly.
How to Run the Chatbot
1.	Navigate to the Project Directory: Open a terminal and change to the project directory:
sh
Copy code
cd path/to/simple_chatbot
2.	Run the Script: Execute the Python script:
sh
Copy code
python chatbot.py
