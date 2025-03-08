import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.state.state import graphstate

class ChatbotWithToolNodes:
    def __init__(self, model):
        self.llm = model
    
    def peocess(self, state: graphstate):
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])
        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"
        return {"messages": [llm_response, tools_response]}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: graphstate):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node