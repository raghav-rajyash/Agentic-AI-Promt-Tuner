from gemini_client import ask_gemini

def generate_prompt(context, user_input):
    prompt = f"""
    You are an expert prompt engineer.

    Using the context below, create a complete AI prompt
    with:
    - Role
    - Task
    - Constraints
    - Output format

    Context:
    {context}

    User Input:
    {user_input}
    """

    return ask_gemini(prompt)
