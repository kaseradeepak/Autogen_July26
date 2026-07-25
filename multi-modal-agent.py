from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage, MultiModalMessage
from autogen_core import Image as AGImage
from PIL import Image

from io import BytesIO
import requests

model_client = OpenAIChatCompletionClient(model='gpt-4o')

agent = AssistantAgent(
    name="image_desc_agent",
    model_client=model_client,
    description="This agent provides the description for the given image link.",
    system_message="You are a helpful assistant, answer the user query accurately"
)

def test_multi_modal_func():
    # Get the image from this link.
    response = requests.get("https://picsum.photos/300/200")

    # Convert into Bytes & then into PIL image format.
    pil_image = Image.open(BytesIO(response.content))

    # Convert PIL image into Autogen Core Image.
    img = AGImage(pil_image)





