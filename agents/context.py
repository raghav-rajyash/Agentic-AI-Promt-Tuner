from gemini_client import ask_gemini

def build_context(prompt, status):
    if status == "EMPTY":
        return {
            "intent": "general assistance",
            "tone": "helpful",
            "audience": "beginner",
            "format": "structured"
        }

    system_prompt = f"""
    Analyze the input and infer:
    - Intent
    - Audience
    - Tone
    - Output format

    Input:
    {prompt}
    """

    return ask_gemini(system_prompt)
