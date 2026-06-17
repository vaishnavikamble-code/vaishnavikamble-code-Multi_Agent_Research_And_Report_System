"""Web search tool placeholder."""

from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search(query):
    
    if not query:
        return "No query provided"

    result = client.search(
        query=str(query),
        search_depth="advanced",
        max_results=5
    )

    return result["results"]