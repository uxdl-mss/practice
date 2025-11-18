from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.getenv("endpoint"),
    api_key=os.getenv("subscription_key"),
    api_version=os.getenv("api_version"),
    azure_deployment=os.getenv("deployment"),
)


text = "an apple a day keeps the doctor away."

vector = embeddings.embed_query(text)

print("Embedding vector length:", len(vector))
print("Embedding sample:", vector[:10])
