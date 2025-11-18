from langgraph.graph import StateGraph, END
from langchain_openai import AzureChatOpenAI
from typing import TypedDict, Annotated
import os
from dotenv import load_dotenv
load_dotenv()

class AgentState(TypedDict):
    user_input: str
    reasoning: str
    tool_output: str
    answer: str


llm = AzureChatOpenAI(
    api_key=os.getenv("subscription_key"),
    azure_endpoint=os.getenv("endpoint"),
    api_version=os.getenv("api_version"),
)

def analyze(state: AgentState):
    text = state["user_input"]
    if "weather" in text:
        state["reasoning"] = "call_tool"
    else:
        state["reasoning"] = "answer_direct"
    return state


def weather_tool(state: AgentState):
    state["tool_output"] = "Weather today is 27°C with clear skies."
    return state

def answer(state: AgentState):
    if state["reasoning"] == "call_tool":
        state["answer"] = f"Here is the weather update:\n{state['tool_output']}"
    else:
        response = llm.invoke(state["user_input"])
        state["answer"] = response.content
    return state


graph = StateGraph(AgentState)

graph.add_node("analyze", analyze)
graph.add_node("tool", weather_tool)
graph.add_node("answer", answer)

graph.set_entry_point("analyze")


def route(state: AgentState):
    if state["reasoning"] == "call_tool":
        return "tool"
    return "answer"

graph.add_conditional_edges(
    "analyze",
    route,
)

graph.add_edge("tool", "answer")

app = graph.compile()


result = app.invoke({"user_input": "What is the weather today?"})
print(result["answer"])
