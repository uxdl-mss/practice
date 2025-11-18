from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import tool
load_dotenv()


llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("endpoint"),
    api_key=os.getenv("subscription_key"),
    api_version=os.getenv("api_version"),
    azure_deployment=os.getenv("deployment")
)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "what is 1+1.")
])


chain = prompt | llm | StrOutputParser()


response = chain.invoke({})
print("Response:", response)
