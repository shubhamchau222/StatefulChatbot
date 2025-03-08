import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.state.state import graphstate
from langgraph.graph import START, END, StateGraph

class BasicChatbotNodes:
    def __init__(self, model):
        self.llm = model
    
    def process(self, state: graphstate):
        return {"messages":
                self.llm.invoke(state["messages"])}
      


