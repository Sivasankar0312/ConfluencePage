import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/process-page/"

# Streamlit UI
st.title("📚 LLM-Powered Confluence Summarizer")

# Input field for Book ID / Page ID
page_id = st.text_input("Enter Confluence Page ID / Book ID", "")

if st.button("Get Summary"):
    if page_id:
        with st.spinner("Fetching and Processing..."):
            try:
                response = requests.post(f"{FASTAPI_URL}{page_id}")
                if response.status_code == 200:
                    result = response.json()
                    st.success("Summary Generated Successfully! 🎉")
                    st.write("### 📄 Summary:")
                    st.write(result["summary"])
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Request failed: {str(e)}")
    else:
        st.warning("Please enter a valid Book ID / Page ID!")
