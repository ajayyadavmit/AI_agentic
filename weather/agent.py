from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
from pydantic import BaseModel, Field

load_dotenv()

client = OpenAI()
import os

def run_cmd(value:str) -> None:
    res = os.system(value)
    return res


def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city.lower()}?format=%C+%T"
    response = requests.get(url)

    if response.status_code == 200:
        return f"the weather in the city: {city.lower()} has {response.text}"
    
    return "Not able to get data from API 😎"


SYSTEM_PROMPT = """
use chain of thought for AI Queries
work with steps: Start, Plan, and Output steps. 
    First you need to do the detailed planning, and then give the output steps. 
    You can also call a TOOL if required from list of TOOLS. 
    For every TOOL Call-> wait for the observe steps and output. 

Rule: 
    Strictly follow the JSON output format given here: 
    Only Run the one step at a time 
    The sequence of step is START where user gives an input, PLAN (that can be multiple times), 
    and finally OUTPUT ( which is going to be displayed to the User). 

Output JSON Format: 
    {{ "step": "START" | "PLAN" | "OUTPUT" | "OBSERVE" | "TOOL", "content": "string", "tool":"string", "input":"string"}}

Available Tools: 
    - get_weather(city: str): Takes City name as an input and gives weather information
    - run_command(value: str): Takes command as the string and execute in the Terminal 

Example 1: 
START. Can you write solve 2 + 3 * 16 / 4
PLAN: {"step": "PLAN", "content": "seems user interested in Math problem"}
PLAN: {"step": "PLAN", "content": "Looking at problem user should be solving using BODMAS method"}
PLAN: {"step": "PLAN", "content": "BODMAS is correect method to implement here"}
PLAN: {"step": "PLAN", "content": "we should first divide 16 by 4 "}
PLAN: {"step": "PLAN", "content": "we should mutiply 3 * 4"}
PLAN: {"step": "PLAN", "content": "we should add 2 and 12"}
OUTPUT: {"step": "OUTPUT", "content": "Total is 14"}

Example 2: 
START. what is the weather of Kathmandu
Plan: {"step": "plan", "content": "seems user interested in knowing the weather of kathmandu"}
Plan: {"step": "plan", "content": "let me check with any available TOOLS"}
Plan: {"step": "plan", "content": "Hooray! we have a weather tools 😙"}
Plan: {"step": "plan", "content": "I need to call get_weather tool with input as Kathmandu "}
Plan: {"step": "TOOL", "tool": "get_weather", "input": "kathmandu"}
Plan: {"step": "OBSERVE", "tool": "get_weather", "output":" The weather in kathamndu is Centrigrate"}
PLAN: { "step": "PLAN": "content": "Great, I got the weather info about delhi" }
Plan: {"step": "OUTPUT", "content": "💦 The weather at Kahtmandu is 💦💦💦💦"}

"""
from typing import Optional
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The Id of step are Plan Tool Observe etc.")
    content: str = Field(None, description="The optional string for the content")
    tool: Optional[str] = Field(None, description="list the tool to call External data")
    input: Optional[str] = Field(None, description="About User Query")
    output: Optional[str] = Field(None, description="The output from LLM")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

available_tools = {
    "get_weather": get_weather,
    "run_command": run_cmd,
}

print("\n\n\n")


while True: 
    user_query = input("👉")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o", response_format=MyOutputFormat, messages=message_history
        )
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("🔥", parsed_result.content)
            continue

        if parsed_result.step == "PLAN":
            print("🧠", parsed_result.content)
            continue
        
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🛠️: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🛠️: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({ "role": "developer", "content": json.dumps(
                { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            ) })
            continue


        if parsed_result.step == "OUTPUT":
            print("🤖", parsed_result.content)
            break


    print("\n\n\n")
