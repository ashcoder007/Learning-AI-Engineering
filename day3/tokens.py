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
prompt1 ="HI!"
prompt2 ="Explain AI."
prompt3 ="Write a 50 word essay on Machine Learning."

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message ={
        "role": role, 
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=1000)
    usage = response.usage
    print(f"Prompt: {prompt} --> your token: {usage.prompt_tokens}, completion token: {usage.completion_tokens}, total token: {usage.total_tokens}  Finish Reason:{response.choices[0].finish_reason}")
     
    finish_reason = response.choices[0].finish_reason
    answer = response.choices[0].message.content
    print(f"  --> Finish Reason: {finish_reason}")
    print(f"  --> Answer: {answer}")
    print("-" * 60)





#prompt = "Who is Virat Kohli?"
#message ={
 #   "role": role, 
 #   "content": prompt
#}
#messages = [message]
#response = client.chat.completions.create(model=model, messages=messages)
#print(response)

#print("##########################")
#answer = response.choices[0].message.content
#print(answer)