from gemini_client import ask_gemini

def evaluate_output(user_input, final_output):
    eval_prompt = f"""
You are an AI evaluator.

Evaluate the AI output based on the following criteria:
1. Relevance to the user input
2. Completeness
3. Clarity
4. Safety
5. Structure & formatting

Give a score from 0 to 100 for each criterion.
Then calculate an overall_accuracy percentage.

Return ONLY valid JSON.

User Input:
{user_input}

AI Output:
{final_output}
"""
    return ask_gemini(eval_prompt)
