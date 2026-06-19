from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Generate a descripton in 200 words in  for a provided image"},
            {"type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/11793795/pexels-photo-11793795.jpeg"} }
        ]
        }
    ]
)

print("RESPONE CAPTION",response.choices[0].message.content)

