# Multi-Agent Research System

A Python research automation system that uses a LangGraph-based multi-agent workflow to plan a research outline, collect web data, review content, and write a final report.

## Project Overview

This system composes several agents into a directed state graph pipeline:
- `planner` generates a structured research outline from a topic.
- `researcher` performs web searches for each outline section.
- `critic` reviews draft content for hallucinations and missing elements.
- `reflector` can generate an improved query from critic feedback.
- `writer` produces a polished final report.

The output is rendered as text and saved to a PDF using `utils/pdf_generator.py`.

## Key Components

- `main.py`
  - CLI entrypoint.
  - Prompts for a research topic, runs the graph, prints the report, and saves `reports/report.pdf`.

- `api/main.py` and `api/api.py`
  - FastAPI backend for generating reports via POST `/generate-report`.
  - Accepts a JSON payload with `topic` and returns the report text and PDF path.

- `config.py`
  - Loads environment variables and configures the `ChatGroq` LLM client.
  - Expects `GROQ_API_KEY` in the environment.

- `graph/workflow.py`
  - Defines the LangGraph `StateGraph` pipeline and the order of agent execution.

- `graph/state.py`
  - Typed dictionary for the shared research state.

- `agents/`
  - Contains the agent functions used by the workflow.
  - `section_manager.py` currently exists as a placeholder for section control logic.

- `tools/web_search.py`
  - Integrates Tavily search via `TavilyClient`.
  - Expects `TAVILY_API_KEY` in the environment.

- `utils/pdf_generator.py`
  - Converts report text into a simple PDF using ReportLab.

- `frontend/app.py`
  - Flask app placeholder with a root route returning a simple message.

## Installation

```powershell
python -m pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file with:

```text
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Run CLI

```powershell
python main.py
```

### Run API

```powershell
python -m api.main
```

Then POST to `http://127.0.0.1:8000/generate-report` with JSON:

```json
{
  "topic": "Your research topic"
}
```

## Notes

- The `frontend` app is a lightweight Flask placeholder and does not currently implement a full UI.
- `agents/section_manager.py` is present as a future extension point for section-specific workflow control.
- The `graph/workflow.py` pipeline currently flows: `planner -> researcher -> critic -> {reflector, writer}` and then ends.

## Dependencies

Captured from `requirements.txt`:
- `langgraph`
- `langchain`
- `langchain-openai`
- `langchain-community`
- `tavily-python`
- `fastapi`
- `uvicorn`
- `streamlit`
- `python-docx`
- `reportlab`
- `pydantic`
- `python-dotenv`
=======
## Multi -Agent-Research And Report System
>>>>>>> c39595195d91b56f278e050566ae1a2983e178b6
