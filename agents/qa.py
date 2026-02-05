from gemini_client import ask_gemini

def qa_check(prompt):
    qa_prompt = f"""
    Check the following prompt for completeness, safety, and reusability.

    If it is good, return ONLY the prompt as-is.
    If improvements are needed, return the improved prompt ONLY.
    Do NOT add explanations.

    Prompt:
    {prompt}
    """
    return ask_gemini(qa_prompt)
