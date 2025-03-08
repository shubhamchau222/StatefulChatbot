from langgraph.graph import StateGraph
from typing import Literal, TypedDict, List, Annotated, Optional
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage


class graphstate(TypedDict):
    """ 
    Represents the state of the graph, any new message will be added to the messages list 
    """
    messages: Annotated[list, add_messages]
    # current_step: Literal["requirements", "user_stories", "po_feedback", "generated_code", "review_feedback"]
    # requirements: str
    # user_stories: str
    # po_feedback: str
    # generated_code: str
    # review_feedback: str
    # decision: Optional[bool]