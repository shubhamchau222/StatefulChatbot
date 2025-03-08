import os 

# Add the src directory to the Python path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from langgraph.graph import StateGraph, START,END
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.state.state import graphstate
from src.nodes.basic_chatbot_nodes import BasicChatbotNodes
from src.nodes.chabot_with_tool_nodes import ChatbotWithToolNodes
from src.tools.search_tool import get_tools, create_tool_node


class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder =StateGraph(graphstate)
    
    def basic_chabot_build(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chabot_node = BasicChatbotNodes(self.model)
        self.graph_builder.add_node("chatbot", self.basic_chabot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
       
    def chatbot_with_tool_build(self):
        """
        Builds a chatbot graph with a tool node using LangGraph.
        This method initializes a chatbot node using the `ChatbotWithToolNodes`"
        """
        tools:list= get_tools()
        tool_node = create_tool_node(tools)
        llm= self.model

        # Define chatbot node
        obj_chatbot_with_node = ChatbotWithToolNodes(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chabot_build()

        if usecase == "Chatbot with Tool":
            self.chatbot_with_tool_build()

        return self.graph_builder.compile()

