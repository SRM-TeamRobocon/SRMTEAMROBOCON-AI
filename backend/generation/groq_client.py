import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

_api_key = (os.getenv("groq_api_key"))
_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

_client = Groq(api_key=_api_key) if _api_key else None


def generate_response(prompt: str) -> str:
    """
    Generate a response from Groq using a chat completion.
    """
    if _client is None:
        return "Groq API key is not configured on the backend."

    completion = _client.chat.completions.create(
        model=_model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful RAG assistant. Answer only from the provided context.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content or ""


if __name__ == "__main__":
    print(generate_response("Say hello in one short sentence."))
