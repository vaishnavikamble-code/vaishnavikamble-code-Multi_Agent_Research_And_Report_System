# agents/section_manager.py

def section_manager(state):

    index = state["section_index"]

    if index >= len(state["outline"]):
        return {}

    return {
        "current_section": state["outline"][index]
    }