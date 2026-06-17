from config import llm

def critic(state):

    report = state.get("report", "")

    # 🔥 LIMIT SIZE (VERY IMPORTANT)
    report = report[:3000]

    prompt = f"""
    You are a strict reviewer.

    Review the following report for:
    - hallucinations
    - factual issues
    - missing sections

    Report:
    {report}

    Return only improvements or "OK".
    """

    response = llm.invoke(prompt)

    return {
        "review": response.content
    }