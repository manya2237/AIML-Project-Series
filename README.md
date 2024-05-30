# Q&A Chatbot

## Overview
This is a basic Q&A chatbot designed to answer common questions and engage in conversation with users. It is implemented using Dialogflow for natural language understanding and interaction.

## Features
- Answers to common questions:
  - What is your name?
  - What services do you provide?
  - Is the chatbot secure?
  - Weather of any city
  - How are you?
- Engaging conversation flow:
  - The chatbot also asks questions from users to keep the conversation flowing naturally.

## Usage
### Asking Questions
Users can ask questions by typing them into the chat interface. The chatbot will respond with appropriate answers or engage in further conversation.

### Example Interactions
1. User: "What is your name?"
   Chatbot: "My name is Chatbot. What's your name?"

2. User: "What services do you provide?"
   Chatbot: "I provide information about various topics and can assist with tasks like checking the weather. What else would you like to know?"

3. User: "Is the chatbot secure?"
   Chatbot: "Yes, the chatbot is designed to prioritize user privacy and security. What other questions do you have?"

4. User: "Weather of New York"
   Chatbot: "Let me check... The current weather in New York is..."

5. User: "How are you?"
   Chatbot: "I'm doing well, thank you for asking! How about you?"

### Real-Time Weather Data
The chatbot uses a FastAPI deployed on VS Code to fetch real-time weather data for any city. Users can ask for the weather in a specific city, and the chatbot will provide the current weather information.

## Deployment
The chatbot is deployed using Dialogflow and can be integrated into various platforms such as websites, messaging apps, and more. To deploy the chatbot, import the provided Dialogflow agent and configure integration with your preferred platform.

## Dependencies
- Dialogflow: For natural language understanding and interaction.
- FastAPI: For fetching real-time weather data.
- VS Code: For development and deployment of the FastAPI.

## Acknowledgments
Special thanks to the creators of Dialogflow and FastAPI for providing powerful tools to build interactive chatbots and fetch real-time data.



