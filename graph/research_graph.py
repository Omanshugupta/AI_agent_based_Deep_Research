from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableConfig

from agents.research_agent import research_agent
from agents.answer_drafter import answer_drafter_agent

from typing import TypedDict, List

# 1. Define the state schema
class GraphState(TypedDict):
    topic: str
    research: List[str]
    answer: str

# 2. Graph class
class DeepResearchGraph:
    def __init__(self):
        self.graph = StateGraph(GraphState)
        self._build_graph()

    def _build_graph(self):
        self.graph.add_node("research_agent", research_agent)
        self.graph.add_node("answer_drafter_agent", answer_drafter_agent)

        self.graph.set_entry_point("research_agent")
        self.graph.add_edge("research_agent", "answer_drafter_agent")

        self.graph.set_finish_point("answer_drafter_agent")

    def build(self):
        return self.graph.compile()
