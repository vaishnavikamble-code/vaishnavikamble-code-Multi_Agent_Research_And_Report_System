from langgraph.graph import StateGraph, END

from graph.state import ResearchState
from agents.planner import planner
from agents.researcher import researcher
from agents.critic import critic
from agents.reflector import reflector
from agents.writer import writer


workflow = StateGraph(ResearchState)

workflow.add_node("planner", planner)
workflow.add_node("researcher", researcher)
workflow.add_node("critic", critic)
workflow.add_node("reflector", reflector)
workflow.add_node("writer", writer)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "critic")
workflow.add_edge("critic", "reflector")
workflow.add_edge("critic", "writer")
workflow.add_edge("writer", END)

graph = workflow.compile()