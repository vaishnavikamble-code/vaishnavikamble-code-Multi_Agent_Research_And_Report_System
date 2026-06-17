from config import llm
import ast

def planner(topic):

    prompt = f"""
    Create a structured research outline for:

    {topic}

    Return ONLY a Python list like:
    ["Introduction", "Applications", "Benefits"]
    """

    response = llm.invoke(prompt)

    outline = ast.literal_eval(response.content)

    return {
        "outline": outline
    }