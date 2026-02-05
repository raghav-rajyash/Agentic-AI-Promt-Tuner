from gemini_client import ask_gemini

def optimize_prompt(prompt):
    improve_prompt = f"""
    Improve clarity, precision, and effectiveness
    of the following prompt without changing intent:

    {prompt}
    """

    return ask_gemini(improve_prompt)
