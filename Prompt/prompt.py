#zero short promopting
from dotenv import load_dotenv
from openai import OpenAI
import os 

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),  #this is to get API KEYS
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" # to set the URL for application Get
)

# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY")
# )

SYSTEM_PROMPT = " YOU SHOULD ANSWER IN ONLY Nepali text "
response = client.chat.completions.create(
    # model="gemini-3.5-flash",
    model="gemini-3.1-flash-lite",
    # model="gpt-5-mini",

    messages=[
        {"role": "user", "content":"What is History"},
        {"role": "system", "content": SYSTEM_PROMPT }
    ]
)


print(response.choices[0].message.content)


