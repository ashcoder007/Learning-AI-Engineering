import os
import re
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
 
model = "openai/gpt-oss-120b"

def get_product_price(product):
    if product == "iphone 17":
        return 1000
    elif product == "iphone 16":
        return 600
    elif product == "macbook pro":
        return 4999.9
    else:
        return 0

def calculator(expression):
    try:
        return eval(expression)
    except Exception:
        return "calc error"

tools ={
    "get_product_price": get_product_price,
    "calculator": calculator
}
system_prompt = """
You are a shopping assistant.
You have access to the following tools:
get_product_price(product)
calculator(expression)

Important: 
call tools exactly like these examples:
Action: get_product_price("iphone 17")
Action: calculator("5000 - 1000")

Never write:
get_product_price(product = "iphone 17")

Never write:
calculator(expression = "5000 - 1000")
Follow these rules:
1. Decide what you need to do next.
2. Call ONLY ONE tool at a time.
3. After witing an Action, stop immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an observation.
6. Then decide your next action.
7. When the task is complete, give the final anser.
8. If the user asks for the price of a product, ALWAYS call get_product_price first.
9. Never say you don't know the price without calling get_product_price.
10. For iPhone 16 and iPhone 17, always use get_product_price().

Format:
Thought: what you need to do
Action: tool_name(argument)

When finished:
Final Answer: your Answer
"""

def run_agent(question):
    messages =[
        {
        "role": "system",
        "content": system_prompt
    },
    {
         "role": "user",
         "content": question
    }
    ]
    for step in range(5):

        print("\n----------------")
        print("STEP", step + 1)
        print("----------------")

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.2,
        )

        answer = response.choices[0].message.content
        print(answer)

        if "Final Answer:" in answer:
            break

        match = re.search(
            r"Action: (\w+)\((.*)\)", 
            answer
        )

        if match:

            tool_name = match.group(1)
            tool_input = match.group(2)

            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            if tool_name in tools:
                tppl = tools[tool_name]
                observation = tppl(tool_input)
            else:
                observation = "Error: Tool not found."

            print("Observation:", observation)

            messages.append({"role": "assistant", "content": answer})
            messages.append({"role": "user", "content": "Observation: " + str(observation)})
            sleep(5)

prompt="""
I have 5000 rupees. I want to buy a macbook pro. How much money will I have left after buying it?
"""
run_agent(prompt)



