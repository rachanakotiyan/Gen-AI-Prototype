import google.generativeai as genai
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

async def call_llm(system_prompt: str, user_message: str, json_mode: bool = False) -> str:
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_prompt
    )

    generation_config = genai.GenerationConfig(
        temperature=0.3,
        **({"response_mime_type": "application/json"} if json_mode else {})
    )

    # Run blocking SDK call in a thread so it doesn't block the event loop
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: model.generate_content(user_message, generation_config=generation_config)
    )

    return response.text