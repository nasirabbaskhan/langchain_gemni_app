# from langchain_openai import OpenAI 
from typing import Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import getpass
import os


# Set the environment variable for Google Cloud application credentials
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("GOOGLE_API_KEY")



# Initialize an instance of the ChatGoogleGenerativeAI with specific parameters
model =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.2,            # Set the randomness of the model's responses (0 = deterministic, 1 = very random)
)

# Invoke the LangChain model with a prompt to generate a response
prompt= "what is generative ai?"
response = model.invoke(prompt)

print(response.content)


#Invoking LangChain Model with Structured Messages for AI Responses
message : list[Dict] = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Which open source AI Model is best so far"},
]

ai_msg = model.invoke(message)
# print(ai_msg.content)
     