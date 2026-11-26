import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
 
model = "openai/gpt-oss-120b"

def llm_answer(prompt):
    message ={
        "role": "user",
        "content": prompt
    }
    messages=[message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

bad_prompt="""
#Role: You're a support assistant at a  mobile/laptop coampany.
#TASK: You've to classify the issue in a category.
#CONSTRAINTS: You have to classify the issue in one of the three categories namely billing, technical, return
#OUTPUT FORMAT: you're answer should be in one word only. The one word should be one of the the categories given in constraints 
#example: for instance if a user complaint says he wants a refund than the category is Return.
#fallback: If the complaint is not related to any of the three categories than you should say "other"
This is a user complaint:
my laptop is not working
"""
print(llm_answer(bad_prompt))