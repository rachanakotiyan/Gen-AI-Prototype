import google.generativeai as genai
from dotenv import load_dotenv
import asyncio
import os
import time

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Simple result cache for repeated prompts (per process)
OPENAI_CACHE_TTL = 90  # seconds
OPENAI_CACHE_MAX = 1000
_openai_cache = {}

def _cache_cleanup():
    now = time.time()
    keys = list(_openai_cache.keys())
    for key in keys:
        if _openai_cache[key][1] < now:
            _openai_cache.pop(key, None)

async def call_llm(system_prompt: str, user_message: str, json_mode: bool = False) -> str:
    cache_key = (system_prompt, user_message, json_mode)
    _cache_cleanup()
    if cache_key in _openai_cache:
        return _openai_cache[cache_key][0]

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
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

    result_text = response.text
    if len(_openai_cache) >= OPENAI_CACHE_MAX:
        # drop oldest entry to avoid unbounded growth
        oldest_key = min(_openai_cache.keys(), key=lambda k: _openai_cache[k][1])
        _openai_cache.pop(oldest_key, None)

    _openai_cache[cache_key] = (result_text, time.time() + OPENAI_CACHE_TTL)

    return result_text