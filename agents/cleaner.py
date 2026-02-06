def clean_duplication(text: str) -> str:
    """
    Removes duplicated lines and repeated paragraphs
    while preserving original order.
    """

    seen_lines = set()
    cleaned_lines = []

    for line in text.splitlines():
        normalized = line.strip().lower()

        # Skip empty duplicates
        if normalized == "":
            cleaned_lines.append(line)
            continue

        # Add line only if not seen before
        if normalized not in seen_lines:
            seen_lines.add(normalized)
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
