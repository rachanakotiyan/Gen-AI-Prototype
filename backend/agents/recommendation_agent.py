# ET Services catalog — mock this for hackathon, looks real enough
ET_SERVICES = {
    "ET Prime": {
        "description": "Ad-free premium articles, expert analysis, exclusive reports",
        "best_for": ["beginner_investor", "student_learner", "wealth_builder"],
        "url": "https://economictimes.indiatimes.com/prime"
    },
    "ET Markets": {
        "description": "Live stock prices, portfolio tracker, market analysis tools",
        "best_for": ["active_trader", "beginner_investor"],
        "url": "https://economictimes.indiatimes.com/markets"
    },
    "ET Money": {
        "description": "Mutual fund investments, SIP planner, tax filing",
        "best_for": ["beginner_investor", "student_learner", "wealth_builder"],
        "url": "https://www.etmoney.com"
    },
    "ET Markets Global": {
        "description": "Track US markets, global indices, international stocks",
        "best_for": ["active_trader", "wealth_builder"],
        "url": "https://economictimes.indiatimes.com/markets/global-markets"
    },
    "ET Wealth": {
        "description": "Personal finance advice, wealth management strategies",
        "best_for": ["wealth_builder", "beginner_investor"],
        "url": "https://economictimes.indiatimes.com/wealth"
    },
    "ET Events": {
        "description": "Finance summits, investor meets, expert webinars",
        "best_for": ["active_trader", "wealth_builder", "student_learner"],
        "url": "https://economictimes.indiatimes.com/events"
    },
    "ET Market Watch": {
        "description": "Real-time alerts, watchlists, technical charts",
        "best_for": ["active_trader"],
        "url": "https://economictimes.indiatimes.com/markets/stocks/stock-market"
    }
}

async def run_recommendation_agent(profile: dict, intent: dict) -> list:
    persona = profile.get("persona", "beginner_investor") or "beginner_investor"
    experience = profile.get("experience_level", "beginner") or "beginner"
    interests = profile.get("interests", []) or []
    
    recommendations = []
    
    for service_name, service_data in ET_SERVICES.items():
        score = 0
        reason = ""
        
        # Persona match
        if persona in service_data["best_for"]:
            score += 3
        
        # Experience-based boost
        if experience == "beginner" and service_name in ["ET Prime", "ET Money"]:
            score += 2
            reason = "Perfect starting point for new investors"
        elif experience == "advanced" and service_name in ["ET Markets Global", "ET Market Watch"]:
            score += 2
            reason = "Advanced tools for experienced investors"
        
        # Interest match
        if "mutual_funds" in interests and service_name == "ET Money":
            score += 2
            reason = "Directly matches your interest in mutual funds"
        if "stocks" in interests and service_name in ["ET Markets", "ET Market Watch"]:
            score += 2
            reason = "Live market data for stock investors"
        
        # Intent boost
        if intent.get("primary_intent") == "learn_investing" and service_name == "ET Prime":
            score += 2
            reason = "Best resource for learning investing concepts"
        if intent.get("primary_intent") == "get_market_data" and service_name == "ET Markets":
            score += 2
            reason = "Real-time data you need right now"
        
        if score > 0:
            recommendations.append({
                "service": service_name,
                "score": score,
                "reason": reason or f"Recommended for {persona.replace('_', ' ')}",
                "url": service_data["url"],
                "description": service_data["description"]
            })
    
    # Sort by score, return top 3
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:3]
