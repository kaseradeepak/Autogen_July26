# Structured Output
# JSON -> Key-Value Pair

# {
#     "user_id" : 1234,
#     "name" : "Sohel",
#     "age" : 20,
#     "designation" : "Software Engineer"
# }

# Pydantic -> Data Validation
# class User: 
#     user_id
#     name
#     age
#     designation,
#     is_married 

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from pydantic import BaseModel

class CityInfo(BaseModel):
    name: str
    state: str
    distance_from_delhi: int
    population: int

model_client = OpenAIChatCompletionClient(
    model='gpt-4o',
    response_format=CityInfo
)

agent = AssistantAgent(
    name="structured_output_agent",
    model_client=model_client,
    description="This agent gives the information about the given city.",
    system_message="You are a helpful agent, that provides the information about the given city."
)

async def test_agent():
    task = TextMessage(content="Please provide the information about Mumbai, provide the details like its population, distance from Delhi etc", source='user')

    result = await agent.run(task=task)

    response = result.messages[1].content

    print(response)

asyncio.run(test_agent())
