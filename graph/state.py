from typing import TypedDict, List

class ResearchState(TypedDict):
    topic: str
    outline: List[str]
    current_section: str
    research: str
    review: str
    report: str
    retry_count: int