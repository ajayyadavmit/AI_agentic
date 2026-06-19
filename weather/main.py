from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
import requests

def get_weather(city: str) ->str:
    url = f"https://wttr.in/{city.lower()}?format=%C+%T"
    response = requests.get(url)

    if response.status_code == 200:
        return f"the weather in the city: {city.lower()} has {response.text}"
    else:
        return "Not able to get data from API 😎"

print(get_weather("hanumansdfsdfdsf"))
def main():
    msg = input(">")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user",
             "content": msg}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")

# main()