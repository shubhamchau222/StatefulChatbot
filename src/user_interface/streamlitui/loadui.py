import os
import sys
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

import streamlit as st 
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from src.user_interface.uiconfig import config
import sys



class LoadStreamlitUI:
    def __init__(self):
        self.config = config()
        self.user_controls = {}
    
    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), 
                           layout="wide",
                           page_icon="🧊")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            use_case_options = self.config.get_usecase_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                #select the model from the list
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_model"] = st.selectbox("Select Model", groq_model_options)
                #ask to enter the API Key as well 
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter your Groq API Key", type="password")

                #Validate the API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", use_case_options)

            if self.user_controls["selected_usecase"] == 'Chatbot with Tool':

                #ask for Tavily API key
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]= st.session_state["TAVILY_API_KEY"] = st.text_input("Enter your Tavily API Key", type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILTY API key to proceed. Don't have? refer : https://tavily.com/")
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
        return self.user_controls


## UI testing code
# if __name__ == "__main__":
#     a= LoadStreamlitUI()
#     a.load_streamlit_ui()
#     print(a.config.get_page_title())

       
