from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage, MultiModalMessage
from autogen_core import Image as AGImage
from PIL import Image

from io import BytesIO
import requests
import asyncio

model_client = OpenAIChatCompletionClient(model='gpt-4o')

agent = AssistantAgent(
    name="image_desc_agent",
    model_client=model_client,
    description="This agent provides the description for the given image link.",
    system_message="You are a helpful assistant, answer the user query accurately"
)

async def test_multi_modal_func():
    # Get the image from this link.
    response = requests.get("https://picsum.photos/id/23/3887/4899")

    # Convert into Bytes & then into PIL image format.
    pil_image = Image.open(BytesIO(response.content))

    # Convert PIL image into Autogen Core Image.
    img = AGImage(pil_image)

    multi_modal_message = MultiModalMessage(
        content = ["Please describe the given image.", img],
        source='user'
    )

    # run the agent.
    result = await agent.run(task=multi_modal_message)

    print(result)

async def main():
    await test_multi_modal_func()

asyncio.run(main())


# TODO: Try to implement run_stream() method.

# async def assistant_run_stream() -> None:
#     # Option 1: read each message from the stream (as shown in the previous example).
#     # async for message in agent.run_stream(task="Find information on AutoGen"):
#     #     print(message)

#     # Option 2: use Console to print all messages as they appear.
#     await Console(
#         agent.run_stream(task="Find information on AutoGen"),
#         output_stats=True,  # Enable stats printing.
#     )

# # Use asyncio.run(assistant_run_stream()) when running in a script.
# await assistant_run_stream()

# ====================================================================================



