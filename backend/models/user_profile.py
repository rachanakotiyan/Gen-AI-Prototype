from pydantic import BaseModel
from typing import Optional, List

class UserProfile(BaseModel):
    user_id: str
    user_type: Optional[str] = None       # student / salaried / investor / trader
    experience_level: Optional[str] = None # beginner / intermediate / advanced
    goals: Optional[List[str]] = []
    risk_level: Optional[str] = None       # low / medium / high
    interests: Optional[List[str]] = []
    age_group: Optional[str] = None        # 18-25 / 26-35 / 35+
    persona: Optional[str] = None          # beginner_investor / active_trader / wealth_builder
