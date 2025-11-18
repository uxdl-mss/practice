from langgraph.graph import StateGraph, END
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()


class AgentState(BaseModel):
    messages: List[dict] = []




def llm_node(state: AgentState):
    model = AzureChatOpenAI(
        azure_endpoint=os.getenv("endpoint"),
        azure_deployment=os.getenv("deployment"),
        api_key=os.getenv("subscription_key"),
        api_version=os.getenv("api_version")
    )

    response = model.invoke(state.messages)
    state.messages.append({"role": "assistant", "content": response.content})
    return state




graph = StateGraph(AgentState)


graph.add_node("model", llm_node)


graph.set_entry_point("model")
graph.add_edge("model", END)

app = graph.compile()


state = AgentState(
    messages=[{"role": "user", "content": "Explain what LangGraph is in one paragraph."}]
)

final_state = app.invoke(state)
print("\nAssistant Response:")
print(final_state["messages"][-1]["content"])



