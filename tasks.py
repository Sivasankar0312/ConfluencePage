from fastapi import BackgroundTasks
from api import fetch_confluence_page
from llm_processing import process_content

async def process_confluence_page(page_id: str):
    """Background task to fetch and process Confluence page asynchronously."""
    raw_content = fetch_confluence_page(page_id)
    summary = process_content(raw_content)
    print(f"Processed Page {page_id}: {summary}")
