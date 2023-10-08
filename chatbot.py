import openai
import os
import argparse
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import YouTubeSearchTool
from langchain.tools import Tool
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.utilities import SerpAPIWrapper
load_dotenv()
import ast
tool = YouTubeSearchTool()

openai.api_key = os.getenv('OPENAI_API_KEY')

os.environ['SERPAPI_API_KEY'] = '7691bfed46fa11be59d73c819e2742fafa603f6446936ed91bace599e1f30d1b'
tool_names = ["serpapi"]
tools = load_tools(tool_names)
youtube_url = ''

def get_message(message):

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role": "user", "content": message},]

    )
    response = response['choices'][0]['message']['content']
    return response



def LLMPromptTemplate(Question,choice):
    llm = OpenAI(temperature = .8)
    if choice == 2:
        urls = (tool.run(f"{Question}, 1"))
        list_ = ast.literal_eval(urls)
        youtube_url = ''.join(list_)
        # for i in range(len(list_)):
        #     youtube_url.append(f'www.youtube.com{list_[i]}')
        return f'www.youtube.com{youtube_url}'
    else:
        agent = initialize_agent(tools, llm)
        return agent.run(Question)

