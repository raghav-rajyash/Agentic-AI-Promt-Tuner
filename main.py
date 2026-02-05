# --------- IMPORTS ---------
from agents.detector import detect_input
from agents.context import build_context
from agents.generator import generate_prompt
from agents.optimizer import optimize_prompt
from agents.qa import qa_check


# --------- CORE PIPELINE FUNCTION ---------
def prompt_tuner(user_input):
    status = detect_input(user_input)
    context = build_context(user_input, status)
    draft = generate_prompt(context, user_input)
    improved = optimize_prompt(draft)
    final_prompt = qa_check(improved)
    return final_prompt


# --------- ENTRY POINT (WRITE THIS AT THE BOTTOM) ---------
if __name__ == "__main__":

    print("\n--- TEST 1: Empty Input ---\n")
    print(prompt_tuner(""))

    print("\n--- TEST 2: Partial Input ---\n")
    print(prompt_tuner("write email"))

    print("\n--- TEST 3: Complete Input ---\n")
    print(prompt_tuner("Write a professional resignation email to my manager"))
