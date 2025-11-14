from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()



client = AzureOpenAI(
    azure_endpoint=os.getenv("endpoint"),
    api_key=os.getenv("subscription_key"),
    api_version=os.getenv("api_version")
)

deployment = os.getenv("deployment")



assistant = client.beta.assistants.create(
    name="assistant1",
    instructions="You are a helpful assistant.",
    model=deployment
)
print("Assistant created:", assistant.id)


thread = client.beta.threads.create()
print("Thread created:", thread.id)


client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="whats 1+1"
)


print("\n \n Streaming Output: \n")

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id
) as stream:

    for event in stream:
        if event.event == "response.output_text.delta":
            print(event.delta, end="", flush=True)

    final_run = stream.get_final_run()

print("\n\nRun finished:", final_run.status)
