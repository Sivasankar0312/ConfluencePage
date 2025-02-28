from langchain.prompts import PromptTemplate
from bs4 import BeautifulSoup
from langchain_anthropic import ChatAnthropic
import getpass
import os


llm = ChatAnthropic(model='claude-3-opus-20240229',api_key='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')

def process_content(html_content):
    text_content = html_content
    prompt_template = PromptTemplate.from_template("Summarize the following content and extract key insights:\n{text}"  
    )
    prompt = prompt_template.invoke({"text":text_content})
    response = llm.invoke(prompt)
    return response.content


