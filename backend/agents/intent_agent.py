from services.openai_service import call_llm
import json

INTENT_PROMPT = """
You are an intent detection agent for Economic Times (ET).

Analyze the user's latest message and detect their PRIMARY intent.

Return ONLY valid JSON:
{
  "primary_intent": "learn_investing | get_market_data | find_products | get_news | compare_options | start_investing | manage_wealth | understand_tax | find_events | general_query",
  "urgency": "high | medium | low",
  "topic": "stocks | mutual_funds | crypto | insurance | tax | real_estate | economy | general",
  "is_ready_to_act": true or false
}

is_ready_to_act = true if user seems ready to sign up, subscribe, or take a concrete step.
"""

async def run_intent_agent(user_message: str) -> dict:
    result = await call_llm(INTENT_PROMPT, user_message, json_mode=True)
    try:
        return json.loads(result)
    except:
        return {"primary_intent": "general_query", "urgency": "low", "topic": "general", "is_ready_to_act": False}
