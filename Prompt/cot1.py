from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
# Few Prompt Gives an Examples also the AI Tool  wit SYSTEM PROPMPT
# Zero prompt: Directly Get answer from AI with SYSTEM
# COT : Chain of thinking prompt Embedding

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
    {{ "step": "start" | "plan" | "output", "content": "string"}}

Example: 
START. Can you write solve 2 + 3 * 16 / 4
Plan: {"step": "plan", "content": "seems user interested in Math problem"}
Plan: {"step": "plan", "content": "Looking at problem user should be solving using BODMAS method"}
Plan: {"step": "plan", "content": "BODMAS is correect method to implement here"}
Plan: {"step": "plan", "content": "we should first divide 16 by 4 "}
Plan: {"step": "plan", "content": "we should mutiply 3 * 4"}
Plan: {"step": "plan", "content": "we should add 2 and 12"}
Plan: {"step": "plan", "content": "Total is 14"}
"""
import json

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": "write a code to add n number in javascript"},
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "start",
                    "content": "Can you write code to add n numbers in JavaScript?",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "plan",
                    "content": "User is interested in writing code for adding multiple numbers.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "plan",
                    "content": "To achieve this, we can create a function that takes an array of numbers as input.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "plan",
                    "content": "We will use the JavaScript 'reduce' method to sum up all the numbers in the array.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "plan",
                    "content": "The function should return the total sum after processing the array.",
                }
            ),
        },
    ],
)


print(response.choices[0].message.content)
print("⌨️🧠 💋"*9)