def detect_input(prompt):
    if not prompt or prompt.strip() == "":
        return "EMPTY"
    elif len(prompt.split()) < 5:
        return "PARTIAL"
    else:
        return "COMPLETE"
