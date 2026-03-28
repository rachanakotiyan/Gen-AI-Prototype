from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path
import os
import json

load_dotenv()
# load_dotenv(Path(__file__).parent.parent / ".env")
print("KEY EXISTS:", "GOOGLE_API_KEY" in os.environ)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


async def call_llm(system_prompt: str, user_message: str, json_mode: bool = False) -> str:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )

    if json_mode:
        response = model.generate_content(
            user_message,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                temperature=0.3
            )
        )
    else:
        response = model.generate_content(
            user_message,
            generation_config=genai.GenerationConfig(
                temperature=0.3
            )
        )

    return response.text