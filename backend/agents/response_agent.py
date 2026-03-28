from services.openai_service import call_llm

RESPONSE_PROMPT = """
You are the friendly face of ET (Economic Times) AI Concierge — India's smartest financial assistant.

Your job: Write a warm, helpful, concise reply (3-4 sentences MAX) that:
1. Acknowledges what the user said
2. Shows you understand their financial situation
3. Briefly explains the top recommendation
4. Ends with an encouraging call to action

Tone: Friendly, confident, like a knowledgeable friend — NOT corporate or robotic.
Language: Simple English. No jargon unless the user is advanced.
Length: 3-4 sentences only.
"""

async def run_response_agent(user_message: str, profile: dict, recommendations: list, action: dict) -> str:
    context = f"""
User said: "{user_message}"
Their profile: {profile}
Top recommendations: {[r['service'] for r in recommendations[:2]]}
Suggested action: {action.get('action_title', '')} — {action.get('action_description', '')}
"""
    return await call_llm(RESPONSE_PROMPT, context)
