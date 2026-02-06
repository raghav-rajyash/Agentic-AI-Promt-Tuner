import streamlit as st
from main import prompt_tuner

st.set_page_config(
    page_title="Agentic AI Prompt Tuner",
    layout="wide"
)

st.title("🧠 Agentic AI Prompt Tuner")
st.markdown(
    "An intelligent multi-agent system that **generates, expands, optimizes, "
    "and evaluates prompts** based on input quality."
)

st.divider()

# -------- USER INPUT --------
user_input = st.text_area(
    "Enter your prompt (leave empty to test auto-generation):",
    height=150,
    placeholder="e.g. write email / Write a professional resignation email to my manager"
)

generate_btn = st.button("🚀 Generate Prompt")

# -------- OUTPUT --------
if generate_btn:
    with st.spinner("Running agentic pipeline..."):
        final_output, accuracy = prompt_tuner(user_input)

    st.subheader("✅ Final Tuned Prompt")
    st.code(final_output, language="markdown")

    st.subheader("📊 Accuracy Evaluation")
    st.json(accuracy)

    st.success("Prompt generated successfully!")
