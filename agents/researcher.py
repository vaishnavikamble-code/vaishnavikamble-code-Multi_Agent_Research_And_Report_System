from tools.web_search import search

def researcher(state):

    topic = state["topic"]
    sections = state["outline"]

    all_research = ""

    for section in sections:

        if not section:
            continue

        query = f"{topic} {section}"

        data = search(query)

        all_research += f"\n\n## {section}\n{data}"

    return {"research": all_research}