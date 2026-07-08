from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
# Few Prompt Gives an Examples also the AI Tool  wit SYSTEM PROPMPT
# Zero prompt: Directly Get answer from AI with SYSTEM 

SYSTEM_PROMPT = """
Your Name is Ramu. Answer only the Coding question. 

Rule:
    Strictly follow the Json format in output. 
Output Format: JSON
    {
    code: string or null,
    iscodingquestion: bool,
    }
Example: 
    Q. Explain a + b whole square?
    A. {{ code: null, iscodingquestion: False}}
    Q. Python code for adding two number a and b 
    A.  {{ code:  def add(a,b):
            return a+b, iscodingquestion: True}}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content":"Who are you. write a Javascript program for findng root of number 88"},
        {"role": "system", "content": SYSTEM_PROMPT},
    ]
)


print(response.choices[0].message.content)

