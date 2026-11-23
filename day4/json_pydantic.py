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
role = "user"

# structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema=Ticket.model_json_schema()

response_format ={
    "type": "json_object",
 }
system_prompt=f"""Extract the personal information from the ticket sctrictly based on this schema and give me a json output. {schema} 
"""
message_system={
    "role": "system", 
    "content": system_prompt
}
text="Hello My name is Ashish. I have an iphone whoch is not working at all. My address is delhi. My contact number is 914256955. My email is abc@gmail.com. My father is very angry, please help"
prompt = f"""This is a customer ticket. Please extract personal information from this.
{text}"""
message ={
    "role": role, 
    "content": prompt
}
messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)


answer = response.choices[0].message.content
print(answer)

# how to read the json output
import json
raw_json = answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)


#inko pass kar skte hai aage (this is a structured data now)
print(ticket.name)
print(ticket.email)
print(ticket.issue)