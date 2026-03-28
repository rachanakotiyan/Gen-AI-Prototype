# 🚀 QUICKSTART - Financial Concierge AI Frontend

## Get Running in 60 Seconds

### 1️⃣ Install Dependencies
```bash
cd frontend
npm install
```

### 2️⃣ Start Development Server
```bash
npm start
```

Opens: http://localhost:3000

### 3️⃣ Start Chatting!

Type in the chat box and press Enter. The mock API is enabled by default.

**Test messages:**
- "I want to start investing"
- "What's your take on AI stocks?"
- "Help me build a portfolio"

---

## 🔄 Switch to Real Backend

### When Backend is Ready:

1. Make sure backend is running:
```bash
cd backend
python main.py
```

2. Edit `frontend/src/services/api_service.js`:
```javascript
// Line 7
const USE_MOCK_API = false;  // Enable real API
const API_BASE_URL = "http://localhost:5000";  // Your backend
```

3. Refresh browser - now it's using your real API!

---

## 📁 Main Files

| File | Purpose |
|------|---------|
| `src/App.js` | Main layout & state management |
| `src/App.css` | Premium styling (glassmorphism) |
| `src/components/ChatBox.js` | Chat display + input |
| `src/components/Message.js` | Individual messages |
| `src/components/ProfileCard.js` | User profile display |
| `src/components/Recommendations.js` | Recommendations list |
| `src/components/Actions.js` | Next action CTA |
| `src/services/api_service.js` | Mock/Real API toggle |
| `src/services/mock_api.js` | Sample responses |

---

## 🎨 What You Get

✅ Chat interface (ChatGPT-style)
✅ Auto-scroll to latest message
✅ Loading/typing indicators
✅ User profile extraction
✅ Personalized recommendations
✅ Call-to-action cards
✅ Session management (user_id)
✅ Responsive design
✅ Modern glassmorphism UI
✅ Mock + Real API toggle

---

## 📊 Example Flow

1. User: "I'm a student interested in stocks"
2. AI responds with message
3. App extracts profile data:
   - User type: student
   - Risk level: low
   - Interests: stocks, dividends, ETFs
4. Sidebar updates with:
   - Profile card showing extracted data
   - Personalized recommendations
   - Suggested next action

---

## 🔌 API Integration

### Request Format
```json
{
  "user_id": "optional-session-id",
  "message": "user's message text"
}
```

### Response Format
```json
{
  "user_id": "session-id",
  "response": "AI's reply",
  "profile": {
    "user_type": "student",
    "risk_level": "low",
    "experience_level": "beginner",
    "interests": ["stocks", "AI"]
  },
  "recommendations": [
    {
      "service": "ET Prime",
      "reason": "Why recommended",
      "url": "https://..."
    }
  ],
  "next_action": {
    "action_title": "Learn Basics",
    "action_description": "Get started",
    "cta_text": "Start →",
    "cta_url": "https://..."
  }
}
```

---

## 🛠 Common Tasks

### Change Colors
Edit `src/App.css` CSS variables (lines 8-30)

### Adjust Layout (Chat % vs Sidebar %)
Edit `src/App.css`:
```css
.chat-section { flex: 0 0 70%; }  /* Change 70 */
.sidebar-section { flex: 0 0 30%; } /* Change 30 */
```

### Test on Mobile
Press F12 → Toggle device toolbar (mobile view)

### Build for Production
```bash
npm run build
```
Creates optimized build in `build/` folder

---

## ✨ Highlights

- **70/30 Layout**: Chat on left, cards on right
- **Gorgeous UI**: Dark theme with gradient accents
- **Mobile-First**: Responsive down to 320px width
- **Smooth Animations**: Sliding messages, floating buttons
- **Session State**: Remembers user_id automatically
- **Error Handling**: Shows friendly error messages

---

## 📚 Full Documentation

- [FRONTEND_GUIDE.md](./FRONTEND_GUIDE.md) - Complete guide
- [CONFIG.md](./CONFIG.md) - Configuration options
- [API_CONTRACT.md](../API_CONTRACT.md) - API specification

---

## 🐛 Stuck?

1. **Check console** (F12 → Console tab)
2. **Check Network** (F12 → Network tab) → Look for failed requests
3. **Restart server**: Ctrl+C in terminal, then `npm start`
4. **Clear cache**: Ctrl+Shift+Delete

---

## 🎯 Next Steps

1. ✅ Run `npm install && npm start`
2. ✅ Test with mock data
3. ✅ Verify UI looks good
4. ✅ When backend ready, flip `USE_MOCK_API = false`
5. ✅ Test with real API
6. ✅ Deploy!

---

**Happy coding! 🚀**
