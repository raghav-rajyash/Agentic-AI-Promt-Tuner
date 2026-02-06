from agents.detector import detect_input
from agents.context import build_context
from agents.generator import generate_prompt
from agents.optimizer import optimize_prompt
from agents.qa import qa_check
from agents.evaluator import evaluate_output
from agents.cleaner import clean_duplication




def prompt_tuner(user_input):
    status = detect_input(user_input)
    context = build_context(user_input, status)
    draft = generate_prompt(context, user_input)
    improved = optimize_prompt(draft)
    final_prompt = qa_check(improved)
    cleaned_prompt = clean_duplication(final_prompt)
    evaluation = evaluate_output(user_input, cleaned_prompt)
    return cleaned_prompt, evaluation




if __name__ == "__main__":

    print("\n--- TEST 1: Empty Input ---\n")
    output, accuracy = prompt_tuner("")
    print("FINAL OUTPUT:\n", output)
    print("\nACCURACY:\n", accuracy)

    print("\n--- TEST 2: Partial Input ---\n")
    output, accuracy = prompt_tuner("write email")
    print("FINAL OUTPUT:\n", output)
    print("\nACCURACY:\n", accuracy)

    print("\n--- TEST 3: Complete Input ---\n")
    output, accuracy = prompt_tuner(
        "Write a professional resignation email to my manager"
    )
    print("FINAL OUTPUT:\n", output)
    print("\nACCURACY:\n", accuracy)

