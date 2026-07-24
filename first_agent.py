from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio

model_client = OpenAIChatCompletionClient(model = 'gpt-4o')

assistant = AssistantAgent(name="our_first_autogen_agent", model_client=model_client, description="First Autogen agent.")

# await - to call asyn function.
async def main():
    result = await assistant.run(task="Explain me what Agentic AI is in a beginner friendly manner. Keep the answer short and technical.")

    print(result.messages[1].content)

asyncio.run(main())
