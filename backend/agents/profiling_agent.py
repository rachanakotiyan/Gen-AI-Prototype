from services.openai_service import call_llm
import json

PROFILING_PROMPT = """
You are a financial profiling agent for Economic Times (ET), India's top financial media platform.

Your job: Extract a structured user profile from the conversation.

Extract ONLY what's clearly stated or strongly implied. Use null for unknown fields.

Return ONLY valid JSON:
{
  "user_type": "student | salaried | business_owner | investor | trader | null",
  "experience_level": "beginner | intermediate | advanced | null",
  "goals": ["list of financial goals mentioned"],
  "risk_level": "low | medium | high | null",
  "interests": ["stocks | mutual_funds | crypto | real_estate | insurance | tax | etc"],
  "age_group": "18-25 | 26-35 | 35+ | null",
  "persona": "beginner_investor | active_trader | wealth_builder | student_learner | null"
}

Persona rules:
- beginner_investor: new to investing, wants to start
- active_trader: trades regularly, wants market data/tools
- wealth_builder: HNI or senior, wants wealth management
- student_learner: student wanting to learn finance
"""

async def run_profiling_agent(conversation: str) -> dict:
    result = await call_llm(PROFILING_PROMPT, conversation, json_mode=True)
    try:
        return json.loads(result)
    except:
        return {}
