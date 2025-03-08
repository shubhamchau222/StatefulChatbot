from configparser import ConfigParser
import sys
import os

# config_filepath= os.path.join(".","src", "user_interface", "uiconfigfile.ini")
config_filepath = os.path.join(os.path.dirname(__file__), "uiconfigfile.ini")
print("config_filepath >> ",config_filepath)

class config:
    """To read the default config file, contains the page title, model providers and model lists
    we can use Yaml file as well for configurations"""
    def __init__(self, config_file=config_filepath):
        self.config= ConfigParser()
        self.config.read(config_file)
    
    def get_llm_options(self):
        return self.config['DEFAULT']["LLM_OPTIONS"].split(", ")
    
    def get_groq_model_options(self):
        return self.config['DEFAULT']["GROQ_MODEL_OPTIONS"].split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")