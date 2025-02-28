import requests
from bs4 import BeautifulSoup
import base64
from llm_processing import process_content
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
import getpass
import os

EMAIL = "sssivasankar73@gmail.com"  
API_TOKEN = "ATATT3xFfGF0hd2AxlBfkmZcn9Xsp7Wti0Eb6ZIvqEnuGcokQTa2NSOmwE8t-KVaW5lygH_rfwIOd9w0ft2BEDlokDpQjH-ORhh5hkPy1w5UaU5ISBk7DPFtzL3iG4UiidkFtbnL6EiTCTVK_muS20YNT79MlU8oIhFzps-9xkOcsCPcjvkBx9Y=55A8608D"  # Generate from Atlassian API tokens page
CONFLUENCE_BASE_URL = "https://sssivasankar73.atlassian.net"

# PAGE_ID = "393217"  

def fetch_confluence_page(page_id):
    """Fetches Confluence page content using REST API"""
    url = f"{CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}?expand=body.storage"
    auth = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()  # Encode credentials
    
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        page_data = response.json()
        raw_html = page_data["body"]["storage"]["value"]  # Get HTML content
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup.get_text()  
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

from fastapi import FastAPI, HTTPException


app = FastAPI(title="LLM Confluence Automation")

@app.get("/")
async def root():
    return {"message": "Welcome to LLM-powered Confluence Automation"}

@app.post("/process-page/{page_id}")
async def process_page(page_id: str):
    """Fetches a Confluence page and processes it with LLM."""
    try:
        raw_content = fetch_confluence_page(page_id)
        processed_data = process_content(raw_content)
        print(processed_data)
        return {"page_id": page_id, "summary": processed_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


