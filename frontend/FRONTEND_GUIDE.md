# Financial Concierge AI - React Frontend

A modern, premium React frontend for an AI-powered financial concierge application featuring a ChatGPT-like interface with real-time user profiling, personalized recommendations, and suggested actions.

## 🎨 Features

- **Modern Chat Interface**: ChatGPT-style messaging with smooth animations and auto-scroll
- **Dynamic User Profiling**: Real-time profile extraction from API responses
- **Personalized Recommendations**: Display curated recommendations with links
- **Call-to-Action Cards**: Prominent next action suggestions
- **Mock & Real API Toggle**: Easy switching between mock data and live backend
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Glassmorphism UI**: Premium, sleek design with gradient accents
- **Session Management**: Persistent user ID across conversations
- **Loading States**: Visual feedback with typing indicators

## 📁 Project Structure

```
src/
├── components/
│   ├── ChatBox.js           # Main chat interface with message display & input
│   ├── Message.js           # Individual message component
│   ├── ProfileCard.js       # User profile display
│   ├── Recommendations.js   # Recommendations list
│   └── Actions.js           # Next action CTA card
├── services/
│   ├── api_service.js       # API service layer (mock/real toggle)
│   └── mock_api.js          # Mock API data for development
├── styles/
│   └── Message.css          # Component-specific styles
├── App.js                   # Main app component with layout
├── App.css                  # Global styles & layout
└── index.js                 # React entry point
```

## 🚀 Quick Start

### 1. Setup

```bash
cd frontend
npm install
```

### 2. Development Server

```bash
npm start
```

The app will open at `http://localhost:3000`

### 3. Toggle Mock/Real API

Edit `src/services/api_service.js`:

```javascript
// Line 7 - Set to false to use real backend
const USE_MOCK_API = true;  // Set to false for real API
const API_BASE_URL = "http://localhost:5000";
```

## 📋 API Contract

The backend must return responses in this format:

```javascript
{
  "user_id": "string",
  "response": "AI message text",
  "profile": {
    "user_type": "student|professional|entrepreneur|investor",
    "risk_level": "low|medium|high",
    "experience_level": "beginner|intermediate|advanced",
    "interests": ["topic1", "topic2"]
  },
  "recommendations": [
    {
      "service": "Service Name",
      "reason": "Why this is recommended",
      "url": "https://..."
    }
  ],
  "next_action": {
    "action_title": "Action Title",
    "action_description": "Description of action",
    "cta_text": "Button Text",
    "cta_url": "https://..."
  }
}
```

## 🎭 Mock API

The mock API (`src/services/mock_api.js`) provides 3 sample responses that cycle through. Each response simulates a 800-2000ms delay. Perfect for testing UI before backend is ready.

### Using Mock Data

Mock data is enabled by default. Simply start the app:

```bash
npm start
```

Test the chat by typing messages like:
- "Tell me about investing"
- "I'm interested in stocks and AI"
- "What should I learn first?"

## 🔧 Connecting Real Backend

### Step 1: Update API Service

Edit `src/services/api_service.js`:

```javascript
const USE_MOCK_API = false;  // Enable real API
const API_BASE_URL = "http://localhost:5000";  // Your backend URL
```

### Step 2: Ensure Backend is Running

Start your Python backend:

```bash
cd backend
python main.py
```

### Step 3: Test the Connection

The app will automatically use real API calls. Each message will:
1. Send text to `/api/chat`
2. Include `user_id` from first response
3. Display structured data in sidebar

## 🎨 Customization

### Colors & Theme

Edit the CSS variables in `src/App.css`:

```css
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --accent-purple: #a78bfa;
  --accent-blue: #60a5fa;
  --accent-pink: #f472b6;
  --accent-green: #34d399;
  /* ... more variables ... */
}
```

### Layout Proportions

Default: 70% chat + 30% sidebar. Edit in `src/App.css`:

```css
.chat-section {
  flex: 0 0 70%;  /* Adjust percentage here */
}

.sidebar-section {
  flex: 0 0 30%;  /* Adjust percentage here */
}
```

### Font & Typography

Change the font family in CSS variables:

```css
--font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu;
```

## 📱 Responsive Breakpoints

- **Desktop**: 1024px and above (full 70/30 layout)
- **Tablet**: 769px to 1023px (stacked full-width)
- **Mobile**: 480px to 768px (stacked, optimized)
- **Small Mobile**: Below 480px (compact)

## 🔌 Environment Variables

The app uses a single file for configuration:

**`src/services/api_service.js`**:
- `USE_MOCK_API`: Toggle between mock and real API
- `API_BASE_URL`: Backend URL

No `.env` file needed - modify directly in the service file.

## 🧪 Testing the Chat

### With Mock API

1. Type: "I want to learn about investing"
2. AI responds with profile + recommendations
3. Sidebar updates with user profile
4. Next action card appears

### With Real Backend

1. Ensure backend is running on port 5000
2. Type a message
3. Response appears in chat
4. Profile/recommendations update in real-time

## 🛠 Debugging

### Chrome DevTools

1. Open DevTools (F12)
2. Network tab: Monitor API requests
3. Console tab: Check for errors
4. Application tab: View session storage

### Common Issues

**API not connecting?**
- Check `USE_MOCK_API` is false
- Verify backend URL in `api_service.js`
- Check CORS headers in backend
- Ensure backend is running

**Styling looks off?**
- Clear cache: `Ctrl+Shift+Delete`
- Restart dev server: `Ctrl+C` then `npm start`
- Check if CSS variables loaded correctly

**Messages not displaying?**
- Open Network tab, verify API response format
- Check component data structure matches contract
- Verify `sender` field is "user" or "ai"

## 📊 Component API

### ChatBox

```jsx
<ChatBox 
  messages={[]}
  onSend={(text) => {}}
  isLoading={false}
/>
```

### Message

```jsx
<Message 
  text="Message text"
  sender="user" // or "ai"
  timestamp={Date}
/>
```

### ProfileCard

```jsx
<ProfileCard 
  profile={{
    user_type: "student",
    risk_level: "low",
    experience_level: "beginner",
    interests: ["stocks", "AI"]
  }}
/>
```

### Recommendations

```jsx
<Recommendations 
  recommendations={[
    {
      service: "ET Prime",
      reason: "Why recommended",
      url: "https://..."
    }
  ]}
/>
```

### Actions

```jsx
<Actions 
  nextAction={{
    action_title: "Learn Basics",
    action_description: "Read this guide",
    cta_text: "Start →",
    cta_url: "https://..."
  }}
/>
```

## 🚀 Production Build

```bash
npm run build
```

Creates optimized production build in `frontend/build/` folder.

Deploy to:
- GitHub Pages
- Vercel
- Netlify
- AWS S3
- Docker container

## 📚 Resources

- [React Hooks Documentation](https://react.dev/reference/react)
- [CSS Grid & Flexbox Guide](https://css-tricks.com/)
- [API Contract](../API_CONTRACT.md)

## 📝 License

MIT

---

**Built for Financial Concierge AI | Premium React Frontend**
