POST /api/chat
Request:
{
"session_id": "abc123",
"message": "I want to start investing"
}

Response:
{
"reply": "Great! Are you looking at stocks or mutual funds?",
"profile": {
"role": "investor",
"experience_level": "beginner",
"interests": ["investing"]
},
"recommendations": [
{
"name": "ET Markets",
"reason": "Track your investments in real time",
"url": "[https://etmarkets.com](https://etmarkets.com/)"
}
]
}

GET /api/profile/:session_id
Response:
{
"session_id": "abc123",
"profile": { ... },
"chat_history": [ ... ]
}