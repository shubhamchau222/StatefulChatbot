import os
import sys
from langchain_groq import ChatGroq
import streamlit as st

class GroqLLMS:
    def __init__(self, user_controls_input):
        """
        This class will validate the API key & Return the Required Groq Model as per user request
        Args:
            user_controls_input (dict): User Controls
        """
        self.user_controls= user_controls_input

    def get_groq_model(self):
        try:
            api_key= self.user_controls["GROQ_API_KEY"]
            model_name= self.user_controls["selected_model"]
            if not api_key and os.environ["GROQ_API_KEY"]:
                st.error("Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ", icon="🚨")
            llm = ChatGroq(model=model_name, api_key= api_key)
        except Exception as e:
            st.error("Error in fetching the model " +str(e))
        return llm
                   

       



