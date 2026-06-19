from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

hello_agent = Agent(name="Greet_agent", handoff_description="Agent greeting people", instructions="you are an Greeting Agent who is supposed to greet People by using EMOJI SMILES ")

result = Runner.run_sync(hello_agent, "Hey, My name is Ajay yadav, I am from Nepal")

print(result.final_output)

