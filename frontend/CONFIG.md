# Frontend Configuration Guide

## Quick API Toggle

There are two ways to switch between Mock and Real API:

### Option 1: Edit Service File (Simple)

Edit `src/services/api_service.js` line 7:

```javascript
// MOCK MODE - For development/testing
const USE_MOCK_API = true;

// REAL MODE - Connect to backend
const USE_MOCK_API = false;
const API_BASE_URL = "http://localhost:5000";
```

### Option 2: Create Environment File (Recommended)

1. Create `.env` in `frontend/` directory:

```
REACT_APP_USE_MOCK_API=true
REACT_APP_API_URL=http://localhost:5000
```

2. Update `src/services/api_service.js`:

```javascript
const USE_MOCK_API = process.env.REACT_APP_USE_MOCK_API === 'true';
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
```

3. Restart dev server:

```bash
npm start
```

## Environment Variables Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `REACT_APP_USE_MOCK_API` | `true` | Use mock API (true) or real backend (false) |
| `REACT_APP_API_URL` | `http://localhost:5000` | Backend API base URL |

## Backend Configuration

Your Python backend should listen on:

```
http://localhost:5000
```

With endpoint:

```
POST /api/chat
Content-Type: application/json

{
  "user_id": "optional-string",
  "message": "user input text"
}
```

## Development vs Production

### Development (Mock Mode)

```bash
# Use mock API for quick testing
npm start
```

Access at: `http://localhost:3000`

Features:
- No backend needed
- 3 sample responses cycle
- 800-2000ms simulated delay
- Perfect for frontend development

### Production (Real API)

```bash
# Switch to real API
# Edit .env or api_service.js

# Ensure backend is running
cd ../backend
python main.py

# Start frontend
npm start
```

## CORS Configuration

If you get CORS errors, configure your backend to allow frontend origin:

```python
# backend/main.py
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {"origins": ["http://localhost:3000"]}
})
```

## Testing Checklist

- [ ] npm start works without errors
- [ ] Chat interface loads
- [ ] Can type and send messages
- [ ] Mock responses display correctly
- [ ] Profile card updates
- [ ] Recommendations display with links
- [ ] Action card shows CTA button
- [ ] Sidebar updates after each message
- [ ] Responsive on mobile (use Chrome DevTools)

## Troubleshooting

**"API call failed" error?**
- Check `USE_MOCK_API` setting
- Verify backend is running
- Check backend URL is correct
- Open Network tab in DevTools to see actual requests

**Styling looks broken?**
- Clear browser cache
- Restart dev server: `npm start`
- Check CSS file loaded in Network tab

**Messages not saving?**
- Check browser console for errors (F12)
- Verify user_id is being captured
- Check API response format matches contract
