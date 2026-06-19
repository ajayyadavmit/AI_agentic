
from google import genai
from dotenv import load_dotenv
from openai import OpenAI
import os 

load_dotenv()

# client = genai.Client(
# api_key=os.environ.get("GOOGLE_API_KEY")
# )
# try: 
#     response = client.models.generate_content(
#         model="gemini-3.5-flash",
#         contents="where is Nepal",
#     )
#     print(response.text)

# except Exception as e:
#     print("Exceptions:", e)

# print(dict(os.environ))

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY")
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "user", "content":"What is History"},
        {"role": "system", "content":"you are an expert lawyer, tell the answer in legal studies"}
    ]
)


print(response.choices[0].message.content)

