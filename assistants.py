from openai import AzureOpenAI
import os
import time
from dotenv import load_dotenv
load_dotenv()



client = AzureOpenAI(
    azure_endpoint=os.getenv("endpoint"),
    api_key=os.getenv("subscription_key"),
    api_version=os.getenv("api_version")
)

deployment = os.getenv("deployment")



assistant = client.beta.assistants.create(
    name="ThreadDemoAssistant",
    instructions=(
        "You are a helpful assistant"
    ),
    model=deployment
)

print("Assistant created:", assistant.id)


