# Multi-Agent Research System

A Python research automation system powered by a multi-agent LangGraph workflow that plans a research outline, collects web data, reviews draft content, and generates a final report as a PDF.

## Project Layout

- `main.py` - CLI entrypoint for running the research workflow and generating `reports/report.pdf`.
- `config.py` - Environment and LLM client configuration.
- `api/` - FastAPI application and route definitions.
  - `api/main.py` - API server startup entrypoint.
  - `api/api.py` - `/generate-report` endpoint implementation.
- `agents/` - Agent modules used by the research workflow.
  - `planner.py`, `researcher.py`, `critic.py`, `reflector.py`, `writer.py`, `section_manager.py`
- `graph/` - Workflow orchestration and shared state.
  - `workflow.py` - LangGraph state graph definition.
  - `state.py` - Typed state model for the workflow.
- `tools/` - External tooling integrations.
  - `web_search.py` - Search integration via Tavily.
- `utils/` - Utility helpers.
  - `pdf_generator.py` - Creates a PDF from report text.
- `frontend/` - Placeholder frontend application.
- `reports/` - Generated report output directory.

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- LangGraph
- LangChain
- Tavily search integration
- ReportLab
- Streamlit (optional frontend support)
- python-dotenv
- pydantic

## Architecture

This repository uses a directed multi-agent workflow to assemble a research report:

1. `planner` generates a structured research outline from the input topic.
2. `researcher` gathers supporting information by searching for each outline section.
3. `critic` reviews and flags potential issues in the draft report.
4. `reflector` can improve the query or content based on critic feedback.
5. `writer` produces the final written report.

The final report is rendered as text and then exported to PDF via `utils/pdf_generator.py`.

## Installation

```powershell
python -m pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the repository root with values for the expected keys:

```text
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Run the CLI

```powershell
python main.py
```

This prompts for a research topic, executes the agent workflow, prints the report, and saves the PDF to `reports/report.pdf`.

### Run the API

```powershell
python -m api.main
```

Send a POST request to:

```text
http://127.0.0.1:8000/generate-report
```

Example request body:

```json
{
  "topic": "Your research topic"
}
```

The API returns the generated report text and the path to the saved PDF.

## Frontend

`frontend/app.py` is currently a placeholder application and does not yet provide a complete web UI.

## Notes

- Do not commit `.env` or any secret keys to version control.
- Keep generated files such as `reports/report.pdf` and Python cache artifacts out of source control.
- The current API route is `/generate-report`, not `/ask`.

## Recommended `.gitignore`

```text
.env
__pycache__/
*.pyc
reports/
vector_store/
api/__pycache__/
frontend/__pycache__/
src/__pycache__/
```

