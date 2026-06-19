from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
use chain of thought for AI Queries
work with steps: Start, Plan, and Output steps. 
    First you need to do the detailed planning, and then give the output steps. 

Rule: 
    Strictly follow the JSON output format given here: 
    Only Run the one step at a time 
    The sequence of step is Start where user gives an input, Plan (that can be multiple times), 
    and finally output ( which is going to be displayed to the User). 

Output JSON Format: 
    {{ "step": "START" | "PLAN" | "OUTPUT", "content": "string"}}

Example: 
START. Can you write solve 2 + 3 * 16 / 4
PLAN: {"step": "PLAN", "content": "seems user interested in Math problem"}
PLAN: {"step": "PLAN", "content": "Looking at problem user should be solving using BODMAS method"}
PLAN: {"step": "PLAN", "content": "BODMAS is correect method to implement here"}
PLAN: {"step": "PLAN", "content": "we should first divide 16 by 4 "}
PLAN: {"step": "PLAN", "content": "we should mutiply 3 * 4"}
PLAN: {"step": "PLAN", "content": "we should add 2 and 12"}
OUTPUT: {"step": "OUTPUT", "content": "Total is 14"}
"""
import json


print("\n\n\n")

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

user_query = input("👉")
message_history.append({"role": "user", "content": user_query})


while True:
    response = client.chat.completions.create(
        model="gpt-4o", response_format={"type": "json_object"}, messages=message_history, n=3
    )
    raw_result = response.choices[1].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")
