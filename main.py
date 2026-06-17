
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graph.workflow import graph
from utils.pdf_generator import generate_pdf

topic = input("Enter Research Topic: ")

initial_state = {
    "topic": topic,
    "outline": [],
    "current_section": "",
    "research": "",
    "review": "",
    "report": ""
}

result = graph.invoke(initial_state)

final_report = result["report"]

print("\nFinal Report:\n")
print(final_report)

pdf_path = generate_pdf(final_report, "reports/report.pdf")

print("\nPDF saved at:", pdf_path)