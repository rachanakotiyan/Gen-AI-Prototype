# Architecture & Component Diagram

## Component Hierarchy

```
App
├── Header
│   ├── Title (💰 Financial Concierge AI)
│   └── Session Badge (if user_id exists)
│
├── Main Layout (70% / 30% split)
│   │
│   ├── Chat Section (70%)
│   │   └── ChatBox
│   │       ├── Messages Container
│   │       │   └── Message[] (repeated)
│   │       │       ├── User Message
│   │       │       └── AI Message
│   │       │
│   │       ├── Typing Indicator (when isLoading)
│   │       │
│   │       └── Input Section
│   │           ├── Textarea
│   │           └── Send Button
│   │
│   └── Sidebar Section (30%)
│       ├── ProfileCard
│       │   ├── User Type
│       │   ├── Risk Level
│       │   ├── Experience Level
│       │   └── Interests (tags)
│       │
│       ├── Recommendations
│       │   └── Recommendation Item[] (repeated)
│       │       ├── Service Name
│       │       ├── Reason
│       │       └── Learn More Link
│       │
│       └── Actions (Next Action CTA)
│           ├── Action Title
│           ├── Action Description
│           └── CTA Button
│
└── Footer
    └── Support text
```

---

## Data Flow

```
User Input
    ↓
ChatBox captures message
    ↓
App.handleSendMessage() called
    ↓
Add user message to chat display
    ↓
sendChatMessage(text, userId) called
    ↓
┌─────────────────────┐
│ API Service Layer   │
└─────────────────────┘
    ↓
┌──────────────┬──────────────┐
│              │              │
USE_MOCK_API   │   Real API   │
(default)      │  (if false)  │
↓              │   ↓
mockChatAPI()  │  fetch()
↓              │   ↓
│←─────────────┴──→│
│
└─ Returns standardized response
    ↓
App receives response with:
├── response (AI message)
├── user_id (save for next request)
├── profile (extract to state)
├── recommendations (extract to state)
└── next_action (extract to state)
    ↓
State updates trigger re-render
    ↓
All components update:
├── ChatBox shows new message
├── ProfileCard updates with profile data
├── Recommendations show recommendations
└── Actions shows next action CTA
    ↓
Complete!
```

---

## State Management Flow

```
App Component State:
├── messages[] ────→ ChatBox (display only)
├── userId ────────→ Sent to API on next message
├── isLoading ──────→ ChatBox (disable input, show typing)
├── profile ────────→ ProfileCard (display extracted profile)
├── recommendations → Recommendations (display list)
└── nextAction ────→ Actions (display CTA card)

State Updates:
1. User sends message
2. Add to messages[]
3. Set isLoading = true
4. API call begins
5. Response received
6. Extract data to profile/recommendations/nextAction
7. Add AI response to messages[]
8. Set isLoading = false
```

---

## File Structure

```
frontend/
├── public/
│   ├── index.html
│   ├── manifest.json
│   └── robots.txt
│
├── src/
│   ├── components/
│   │   ├── ChatBox.js ...................... Chat display + input
│   │   ├── Message.js ...................... Individual message
│   │   ├── ProfileCard.js .................. Profile display
│   │   ├── Recommendations.js .............. Recommendations list
│   │   └── Actions.js ...................... Next action CTA
│   │
│   ├── services/
│   │   ├── api_service.js .................. Main API layer
│   │   └── mock_api.js ..................... Mock responses
│   │
│   ├── styles/
│   │   └── Message.css ..................... Component styles
│   │
│   ├── App.js ........................ Main component + layout
│   ├── App.css ........................ Global + layout styles
│   ├── index.js ....................... React entry
│   ├── index.css ...................... Base styles
│   └── ...other CRA files...
│
├── package.json ..................... Dependencies
├── package-lock.json
├── .gitignore
│
├── QUICKSTART.md ..................... 60-second guide
├── FRONTEND_GUIDE.md ................ Full documentation
├── CONFIG.md ........................ Config options
└── BUILD_SUMMARY.md ................ This file
```

---

## API Contract Compliance

```
Request (sent by frontend):
POST /api/chat
{
  "user_id": "session-id" (or omitted on first call),
  "message": "user's text"
}

Response (received by frontend):
{
  "user_id": "session-id",           ← App captures and reuses
  "response": "AI message",          ← Shown in ChatBox
  "profile": {                       ← Shown in ProfileCard
    "user_type": "...",
    "risk_level": "...",
    "experience_level": "...",
    "interests": [...]
  },
  "recommendations": [               ← Shown in Recommendations
    {
      "service": "...",
      "reason": "...",
      "url": "..."
    }
  ],
  "next_action": {                   ← Shown in Actions
    "action_title": "...",
    "action_description": "...",
    "cta_text": "...",
    "cta_url": "..."
  }
}
```

---

## Request/Response Lifecycle

```
┌────────────────────────────────────────────────┐
│ User types "Tell me about dividends"            │
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ ChatBox sends message via App.handleSendMessage│
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ User message added to UI immediately           │
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ sendChatMessage("Tell me...", userId)          │
│ ├─ If USE_MOCK_API: mockChatAPI()             │
│ └─ If real: fetch() to backend               │
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ Typing indicator shown                         │
│ Input disabled                                 │
│ isLoading = true                               │
└─────────────────────┬──────────────────────────┘
                      ↓
       [800-2000ms delay or API latency]
                      ↓
┌────────────────────────────────────────────────┐
│ Response received:                              │
│ {                                              │
│   user_id: "123",                              │
│   response: "Great question about dividends..",│
│   profile: {...},                              │
│   recommendations: [...],                      │
│   next_action: {...}                           │
│ }                                              │
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ App updates state:                              │
│ - userId saved (reuse in next request)          │
│ - profile state updated                        │
│ - recommendations state updated                │
│ - nextAction state updated                     │
│ - AI message added to chat                     │
│ - isLoading = false (typing indicator hidden)  │
│ - Input re-enabled                             │
└─────────────────────┬──────────────────────────┘
                      ↓
┌────────────────────────────────────────────────┐
│ UI updates automatically:                       │
│ ✓ Message appears in chat                      │
│ ✓ ProfileCard shows "intermediate, medium..."  │
│ ✓ Recommendations display with links           │
│ ✓ Next action CTA shows                        │
│ ✓ Chat scrolls to bottom                       │
└────────────────────────────────────────────────┘
```

---

## Mock API Mode

```
When USE_MOCK_API = true:

User Input
    ↓
sendChatMessage()
    ↓
mockChatAPI(payload)
    ↓
├─ Waits 800-2000ms
├─ Returns response from predefined array
│  ├─ Response 1: Student profile, ET Prime recommendation
│  ├─ Response 2: Tech stock focus, Seeking Alpha recommendation
│  └─ Response 3: ETF focus, Community join action
├─ Each call cycles through responses
└─ Same format as real API

Perfect for:
✓ Development without backend
✓ UI/UX testing
✓ Testing error states
✓ Demo/screenshots
✓ Onboarding new team members
```

---

## Real API Mode

```
When USE_MOCK_API = false:

User Input
    ↓
sendChatMessage()
    ↓
fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user_id?, message })
})
    ↓
Backend processes request
    ↓
Backend returns JSON matching contract
    ↓
Frontend processes response
    ↓
UI updates with real AI response

Requirements:
- Backend listening on http://localhost:5000
- Endpoint: POST /api/chat
- Response format matches API contract
- CORS headers configured (if backend on different port)
```

---

## CSS Architecture

```
app.css (500+ lines)
├── Root CSS Variables (colors, spacing, typography)
│   ├── Color gradients
│   ├── Neutral palette (dark theme)
│   ├── Accent colors (purple, blue, pink, green)
│   ├── Shadows & effects
│   ├── Spacing scale (xs, sm, md, lg, xl, 2xl)
│   └── Border radius scale
│
├── Global Styles
│   ├── Universal reset
│   ├── Font family
│   └── Body background
│
├── App Layout (flexbox)
│   ├── Header styling
│   ├── Main 70/30 split
│   ├── Sidebar styling
│   └── Footer styling
│
├── Chat Components
│   ├── ChatBox container
│   ├── Messages display
│   ├── Message styling (user vs AI)
│   ├── Input textarea
│   ├── Send button
│   └── Typing indicator animation
│
├── Cards
│   ├── Card base style (glassmorphism)
│   ├── ProfileCard specific
│   ├── Recommendations specific
│   └── Actions/CTA card specific
│
├── Animations
│   ├── slideIn (messages)
│   ├── float (empty state)
│   ├── typing (indicator)
│   └── Hover effects
│
└── Responsive Media Queries
    ├── Desktop (1024px+)
    ├── Tablet (768-1023px)
    ├── Mobile (480-767px)
    └── Small Mobile (<480px)
```

---

## Complete Development Workflow

```
1. Initial Setup
   ├── npm install
   ├── npm start
   └── Check http://localhost:3000

2. Test with Mock API (Default)
   ├── Send test messages
   ├── Verify UI updates
   ├── Check console for errors
   └── Test responsive (F12 → toggle device)

3. Customize (Optional)
   ├── Edit CSS colors
   ├── Adjust layout proportions
   ├── Update mock responses
   └── Test changes (auto-reload)

4. Backend Implementation
   ├── Build backend endpoints
   ├── Implement AI logic
   └── Format responses to spec

5. Integration Testing
   ├── Set USE_MOCK_API = false
   ├── Start backend: python main.py
   ├── Test with real API
   └── Debug any issues

6. Production
   ├── npm run build
   ├── Deploy build/ folder
   ├── Point frontend to backend URL
   └── Test in production
```

---

This architecture is **flexible, scalable, and production-ready**!
