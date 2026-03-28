from services.openai_service import call_llm
import json

ACTION_PROMPT = """
You are the Action Agent for ET (Economic Times) AI Concierge.

Based on the user profile, intent, and top recommendation — decide the SINGLE BEST next action for this user.

Return ONLY valid JSON:
{
  "action_type": "subscribe_et_prime | explore_et_markets | start_sip_on_et_money | register_for_event | read_article | use_portfolio_tracker | consult_advisor",
  "action_title": "Short action title (max 8 words)",
  "action_description": "One sentence explaining what to do and why",
  "cta_text": "Button text (e.g., Start Free Trial, Explore Now)",
  "cta_url": "relevant ET URL",
  "priority": "high | medium"
}
"""

async def run_action_agent(profile: dict, intent: dict, top_recommendation: dict) -> dict:
    context = f"""
User Profile: {json.dumps(profile)}
User Intent: {json.dumps(intent)}
Top Recommendation: {json.dumps(top_recommendation)}
"""
    result = await call_llm(ACTION_PROMPT, context, json_mode=True)
    try:
        return json.loads(result)
    except:
        return {
            "action_type": "explore_et_markets",
            "action_title": "Start Your Investment Journey",
            "action_description": "Explore ET Markets to track stocks and understand the market.",
            "cta_text": "Explore ET Markets",
            "cta_url": "https://economictimes.indiatimes.com/markets",
            "priority": "high"
        }
