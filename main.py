from fastapi import FastAPI, HTTPException
from api import fetch_confluence_page
from llm_processing import process_content
# from tasks import process_confluence_page

app = FastAPI(title="LLM Confluence Automation")

@app.get("/")
async def root():
    return {"message": "Welcome to LLM-powered Confluence Automation"}

# @app.post("/process-page/{page_id}")
# async def process_page(page_id: str):
#     """Fetches a Confluence page and processes it with LLM."""
#     try:
#         raw_content = fetch_confluence_page(page_id)
#         processed_data = process_content(raw_content)
#         return {"page_id": page_id, "summary": processed_data}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
