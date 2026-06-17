import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

#print("API KEY =", os.getenv("GROQ_API_KEY"))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)