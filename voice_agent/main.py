import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
def main():
    r = sr.Recognizer()

    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        print("Speak Now >> 🔉")
        audio = r.listen(source)
        print("Processing S2T")
        stt= r.recognize_google(audio)

        SYSTEM_PROMPT = """
                You're an expert voice agent. You are given the transcript of what
                user has said using voice.
                You need to output as if you are an voice agent and whatever you speak
                will be converted back to audio using AI and played back to user.
            """

        print("YOu Said: ",stt)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content":stt}
            ]
        )

        print("AI Response", response.choices[0].message.content)

main()