# ✅ Frontend Verification Checklist

Use this checklist to verify everything is working correctly.

## 📥 Installation & Setup

- [ ] Navigated to `frontend/` directory
- [ ] Ran `npm install` successfully
- [ ] No installation errors in console
- [ ] `node_modules/` folder created

## 🚀 Development Server

- [ ] Ran `npm start` successfully  
- [ ] Dev server started on http://localhost:3000
- [ ] Browser opened automatically
- [ ] No "Failed to compile" errors
- [ ] Console shows no errors (F12)

## 🎨 UI/UX Verification

### Layout
- [ ] Header visible at top
- [ ] Chat on left side (~70% width)
- [ ] Sidebar on right side (~30% width)
- [ ] Footer visible at bottom
- [ ] Proper spacing/padding throughout

### Chat Window
- [ ] Chat area displays correctly
- [ ] Empty state shows with icon and text
- [ ] Input textarea visible
- [ ] Send button visible and clickable
- [ ] Colors load correctly (dark theme)

### Styling
- [ ] Dark theme applied (not default white)
- [ ] Gradient accents visible (purple, blue, pink, green)
- [ ] Cards have glassmorphism effect
- [ ] Text is readable (good contrast)
- [ ] No layout overflow or wrapping issues

## 💬 Mock API Testing

- [ ] Type a test message ("Tell me about stocks")
- [ ] Message appears in chat aligned right
- [ ] Typing indicator appears (three dots animation)
- [ ] Input field disabled during loading
- [ ] Response appears after delay (800-2000ms)
- [ ] Response appears aligned to left
- [ ] Typing indicator disappears
- [ ] Input field re-enabled
- [ ] Can type new message

### Message Verification  
- [ ] User message styled with gradient background
- [ ] AI message styled with blue tinted background
- [ ] Messages show timestamps
- [ ] Messages auto-scroll to bottom
- [ ] Chat scrollbar appears if many messages

### Sidebar Updates
- [ ] After first response, ProfileCard shows data:
  - [ ] User Type displays (e.g., "student")
  - [ ] Risk Level displays (e.g., "low")
  - [ ] Experience Level displays (e.g., "beginner")
  - [ ] Interests show as tags (e.g., "#stocks", "#AI")
- [ ] Recommendations display:
  - [ ] Service name shows (e.g., "ET Prime")
  - [ ] Reason text visible
  - [ ] "Learn More →" link clickable
  - [ ] External link icon appears
- [ ] Next Action card shows:
  - [ ] Action title visible (e.g., "Learn Basics")
  - [ ] Description text visible
  - [ ] CTA button visible and styled
  - [ ] Button is clickable

## 🔄 Multi-Message Flow

- [ ] Send 2-3 messages
- [ ] All messages appear in chat in order
- [ ] Chat auto-scrolls to latest message
- [ ] Sidebar updates with each response
- [ ] No duplicate messages
- [ ] Timestamps are different for each message

## 📱 Responsive Design

### On Desktop (1024px+)
- [ ] 70/30 layout maintained
- [ ] Everything readable and proportional

### Tablet View (768-1023px)
- [ ] Use DevTools to toggle "Responsive Design Mode"
- [ ] Chat stacks on top
- [ ] Sidebar stacks below
- [ ] Both sections full-width
- [ ] No horizontal scroll

### Mobile View (480-767px)
- [ ] All elements stack vertically
- [ ] Text is readable (not too small)
- [ ] Buttons are clickable (large enough)
- [ ] No overflow or cut-off content

### Small Mobile (<480px)
- [ ] Extreme padding reduced
- [ ] Text scaled appropriately
- [ ] Still fully usable

## ⚙️ Configuration

- [ ] Open `src/services/api_service.js`
- [ ] Verify line 7: `const USE_MOCK_API = true;` (mock mode)
- [ ] Verify line 8: `const API_BASE_URL = "http://localhost:5000";`
- [ ] Both values are visible and correct

## 🎨 Theme Customization (Optional)

- [ ] Open `src/App.css`
- [ ] Locate CSS variables (lines 8-30):
  - [ ] `--primary-gradient` defined
  - [ ] `--accent-purple` defined
  - [ ] `--accent-blue` defined
  - [ ] `--accent-pink` defined
  - [ ] `--accent-green` defined
- [ ] Can see color values (#XXXXXX format)

## 🧪 Error Handling

Try these error scenarios:

- [ ] Click send with empty message
  - [ ] Nothing happens (input validated)
- [ ] Try before mock response returns
  - [ ] Button shows "Thinking..."
  - [ ] Input disabled
  - [ ] Can't spam send
- [ ] Check browser console
  - [ ] No red error messages
  - [ ] No network failures (unless backend intentionally down)

## 📊 Component Files Exist

- [ ] `src/App.js` exists and has content
- [ ] `src/App.css` exists and is substantial
- [ ] `src/components/ChatBox.js` exists
- [ ] `src/components/Message.js` exists
- [ ] `src/components/ProfileCard.js` exists
- [ ] `src/components/Recommendations.js` exists
- [ ] `src/components/Actions.js` exists
- [ ] `src/services/api_service.js` exists
- [ ] `src/services/mock_api.js` exists
- [ ] `src/styles/Message.css` exists

## 📚 Documentation Files Exist

- [ ] `QUICKSTART.md` exists and readable
- [ ] `FRONTEND_GUIDE.md` exists and readable
- [ ] `CONFIG.md` exists and readable
- [ ] `BUILD_SUMMARY.md` exists and readable
- [ ] `ARCHITECTURE.md` exists and readable

## 🚀 Production Ready Checks

- [ ] No console errors or warnings
- [ ] All features work as designed
- [ ] Mock API responses display correctly
- [ ] All UI elements visible and functional
- [ ] Responsive on all screen sizes
- [ ] Performance acceptable (no lag)
- [ ] Code is clean and readable
- [ ] Comments present in code

## 🔌 Real Backend Integration (When Ready)

When you build the backend:

- [ ] Backend runs on `http://localhost:5000`
- [ ] Backend has `POST /api/chat` endpoint
- [ ] Backend returns proper JSON format
- [ ] Change `USE_MOCK_API = false` in `api_service.js`
- [ ] Restart frontend: `npm start`
- [ ] Test with real backend
- [ ] Verify profile extraction works
- [ ] Verify recommendations display
- [ ] Verify next action shows

## 🌐 Network/CORS (Real Backend)

- [ ] Open DevTools Network tab (F12)
- [ ] Send a message
- [ ] Check Network tab for API request
- [ ] Should see POST to `/api/chat`
- [ ] Status should be 200 (success)
- [ ] Response body should be valid JSON
- [ ] No CORS errors in console

## ✨ Final Verification

- [ ] All critical features working
- [ ] UI looks professional and modern
- [ ] No broken features
- [ ] Ready to show stakeholders
- [ ] Ready for backend integration
- [ ] Ready for production deployment

---

## Troubleshooting Reference

| Issue | Solution |
|-------|----------|
| "npm: command not found" | Install Node.js from nodejs.org |
| Module not found errors | Run `npm install` again |
| Port 3000 already in use | Close other app using port 3000 |
| Styling looks broken | Clear cache (Ctrl+Shift+Delete) & restart |
| API not connecting | Check `USE_MOCK_API` setting, restart server |
| Mobile view looks odd | Check Device Pixel Ratio in DevTools |
| Messages not appearing | Check browser console for JS errors |

---

**If all items are checked, your frontend is production-ready! ✅**
