from config import llm

def reflector(state):

    review = state["review"]

    prompt = f"""
    Based on this critic review:

    {review}

    Generate a better search query.

    Return only the query.
    """

    response = llm.invoke(prompt)

    return {
        "current_section": response.content.strip()
    }