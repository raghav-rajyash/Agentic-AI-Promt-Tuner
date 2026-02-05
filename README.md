🧠 Agentic AI Prompt Tuner (Gemini API)

An Agentic AI system that intelligently generates, expands, optimizes, or validates prompts based on the quality of user input.
Built using multi-agent architecture and powered by Google Gemini API.

🚀 Project Overview

Most AI systems assume the user always provides a good prompt.
This project solves that problem by introducing agentic decision-making.

What this system does:

✅ Generates a complete prompt if the user provides no input

✅ Expands and clarifies vague or partial prompts

✅ Optimizes well-defined prompts into production-ready prompts

✅ Prevents hallucination by asking clarifying questions when needed

The system dynamically decides what action to take, instead of following a fixed flow.

🧠 Why Agentic AI?

This is not a single LLM call.

The system uses multiple specialized agents, each responsible for a specific task, working together as a pipeline.

Each agent has autonomy, a defined role, and communicates through structured outputs.

🧩 Agent Architecture
Agents Used
Agent	Responsibility
Input Detection Agent	Classifies input as Empty / Partial / Complete
Context Builder Agent	Infers intent, audience, tone, and format
Prompt Generation Agent	Builds a structured, high-quality prompt
Prompt Optimizer Agent	Refines clarity, structure, and constraints
QA & Safety Agent	Ensures completeness, safety, and reusability
🔁 Agent Workflow
User Input
   ↓
Input Detection Agent
   ↓
Context Builder Agent
   ↓
Prompt Generation Agent
   ↓
Prompt Optimization Agent
   ↓
QA & Safety Agent
   ↓
Final Tuned Prompt

🛠️ Tech Stack

Language: Python

LLM: Google Gemini API

Architecture: Multi-Agent (Agentic AI)

SDK: google-genai

Environment: Virtualenv

📂 Project Structure
prompt_tuner/
│
├── agents/
│   ├── detector.py        # Input classification
│   ├── context.py         # Context & intent inference
│   ├── generator.py       # Prompt creation
│   ├── optimizer.py       # Prompt refinement
│   └── qa.py              # Safety & validation
│
├── gemini_client.py       # Gemini API wrapper
├── main.py                # Agent orchestration
├── test_gemini.py         # API connectivity test
└── README.md
