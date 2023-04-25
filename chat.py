#!/usr/bin/python3

# TODO 
# - Dodać enkrypcje wiadomosci wysylanej i odbieranej

import openai

# Initialize OpenAI API with your API key
openai.api_key = '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'

# Define a function to generate a response from GPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Main loop for the chat
while True:
    user_input = input("User: ")  # Get user input
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break  # Exit the loop if user enters 'exit'
    else:
        prompt = f"User: {user_input}\nChatbot:"
        response = generate_response(prompt)
        print("Chatbot:", response)  # Generate and print chatbot's response
