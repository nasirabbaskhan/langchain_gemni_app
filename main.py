from typing import Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()



# load the GOOGLE_API_KEY
google_api_key =  os.getenv("GOOGLE_API_KEY")

# Initialize an instance of the ChatGoogleGenerativeAI with specific parameters
llm =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.2,            # Set the randomness of the model's responses (0 = deterministic, 1 = very random)
)


prompt= PromptTemplate(template="create the story of two friends who are ging to the market to buy some fruits? the charachers are {characters}, yor response should be start from character name after the name add the colon e.g character_name:", input_variables=["characters"])
chain = prompt | llm
response= chain.invoke({"characters":"Nasir and Ahmad"})
# print(response.content)


#Invoking LangChain Model with Structured Messages for AI Responses
message : list[Dict] = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Which open source AI Model is best so far"},
]

ai_msg = llm.invoke(message)
# print(ai_msg.content)


# Example conversation with system message
conversation:list= [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Can you help me with my homework?"),
    AIMessage(content="Of course! What subject do you need help with?"),
    HumanMessage(content="I am struggling with math"),
    AIMessage(content="I acan help with taht, Whatspacific math problem are you working on? ") 
]

conversation.append(HumanMessage(content="Can you help me with my homework?"))

for message in conversation:
    if isinstance(message, HumanMessage):
        print(f"User:{message.content}")
    elif isinstance(message, AIMessage):
        print(f"AI:{message.content}")
    elif isinstance(message, SystemMessage):
        print(f"system:{message.content}")
