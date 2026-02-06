from google import genai
from google.genai.errors import ClientError
import os

MODEL_NAME = "models/gemma-3-4b-it"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def ask_gemini(prompt: str) -> str:
    """
    Gemini API wrapper with graceful quota handling.
    No retries on RESOURCE_EXHAUSTED to avoid retry loops.
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text

    except ClientError as e:
        if "RESOURCE_EXHAUSTED" in str(e):
            return (
                "⚠️ Gemini free-tier quota exhausted.\n\n"
                "The system is temporarily unable to generate responses. "
                "Please wait a few minutes or try again later."
            )
        else:
            raise e

