from fastapi import FastAPI
from pydantic import BaseModel

from graph.workflow import graph
from utils.pdf_generator import generate_pdf

app = FastAPI()

class Request(BaseModel):
    topic: str
    
@app.post("/generate-report")
def generate(request: Request):

    topic = request.topic

    # Initial state for LangGraph
    initial_state = {
        "topic": topic,
        "outline": [],
        "current_section": "",
        "research": "",
        "review": "",
        "report": ""
    }

    # Run full graph
    result = graph.invoke(initial_state)

    report = result["report"]

    # Generate PDF
    pdf_path = generate_pdf(report, "reports/report.pdf")

    return {
        "topic": topic,
        "report": report,
        "pdf_path": pdf_path
    }