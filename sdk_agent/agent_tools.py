from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool

load_dotenv()

hello_agent = Agent(
    name="Greet_agent",
    handoff_description="Agent greeting people",
    instructions="you are an Greeting Agent who is supposed to greet People by using EMOJI SMILES ",
    tools=[WebSearchTool()],
)

result = Runner.run_sync(hello_agent, "what is there on website https://ajayyadav.com.np/ ")

print(result.final_output)
print("**"*33)
print(result.raw_responses)