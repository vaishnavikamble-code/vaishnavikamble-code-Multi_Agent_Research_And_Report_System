from config import llm

def writer(state):

    topic = state["topic"]
    outline = state.get("outline", [])
    research = state.get("research", "")
    review = state.get("review", "")

    # 🔥 LIMIT SIZE (CRITICAL FIX)
    research = research[:2500]
    review = review[:1000]

    prompt = f"""
    You are a professional report writer.

    Topic: {topic}

    Outline:
    {outline}

    Research:
    {research}

    Review Notes:
    {review}

    Write a clean structured final report.
    Keep it concise and well formatted.
    """

    response = llm.invoke(prompt)

    return {
        "report": response.content
    }