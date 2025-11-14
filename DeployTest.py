import os
from openai import AzureOpenAI

endpoint = "https://vinay-me2jz5pg-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-5-nano"
deployment = "gpt-5-nano-2"

subscription_key = "5LzC7nxdTjdpLRsI8JO9W0Zcui4THwSt16xEfcZ7fp6iFDimCf6VJQQJ99BHACHYHv6XJ3w3AAAAACOGZBos"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

'''response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=16384,
    model=deployment
)

print(response.choices[0].message.content)'''

