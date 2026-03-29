# Gen-AI-Prototype

## Project Overview

This is a prototype for an AI-powered financial concierge chat application designed for Economic Times (ET). The application provides personalized financial advice, market insights, and service recommendations through an intelligent chat interface that dynamically profiles users and suggests relevant ET products and services.

The system uses advanced AI agents to analyze user intent, build user profiles, generate contextual recommendations, and suggest actionable next steps, all powered by Google's Generative AI (Gemini) and a modern React frontend.

## Features

- **Intelligent Chat Interface**: Conversational AI that understands financial queries and provides contextual responses
- **Dynamic User Profiling**: Automatically builds and updates user profiles based on conversation history, including:
  - User persona (beginner investor, active trader, wealth builder, etc.)
  - Risk tolerance levels
  - Experience levels
  - Interest areas (stocks, mutual funds, crypto, insurance, tax, etc.)
- **Personalized Recommendations**: Suggests relevant ET services and products based on user profile and intent
- **Actionable CTAs**: Provides clear next-step actions to guide users toward concrete financial decisions
- **Real-time Response**: Fast, responsive chat experience with typing indicators and smooth animations
- **Modern UI**: Glassmorphism design with dark theme, responsive layout, and premium feel

## Tech Stack

### Backend
- **Framework**: FastAPI (Python async web framework)
- **AI/ML**: Google Generative AI (Gemini) for natural language processing and intent detection
- **Database**: MongoDB with Motor (async Python driver) for user profiles and chat history
- **Architecture**: Modular agent-based system with separate agents for:
  - Intent detection
  - User profiling
  - Recommendation generation
  - Response synthesis

### Frontend
- **Framework**: React 19 with modern hooks and functional components
- **Styling**: Custom CSS with glassmorphism effects, CSS variables, and responsive design
- **State Management**: React useState and useCallback for component state
- **API Integration**: Flexible service layer supporting both mock and real API endpoints

### Infrastructure
- **Deployment**: Container-ready with CORS support
- **Development**: Hot reload for both frontend and backend
- **Testing**: Jest and React Testing Library for frontend tests

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- MongoDB (local or cloud instance)
- Google AI API key (for Gemini integration)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file with your MongoDB connection string and Google AI API key
   - Example:
     ```
     MONGODB_URL=mongodb://localhost:27017/et_concierge
     GOOGLE_AI_API_KEY=your_api_key_here
     ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   The application will open at `http://localhost:3000`

### Configuration

- **API Endpoint**: Update `src/services/api_service.js` to point to your backend URL
- **Mock Mode**: Set `USE_MOCK_API = true` in `api_service.js` for development without backend
- **Database**: Ensure MongoDB is running and accessible

### Running Tests

Frontend tests:
```bash
cd frontend
npm test
```

Backend tests (if implemented):
```bash
cd backend
pytest
```

## API Contract

See [API_CONTRACT.md](API_CONTRACT.md) for detailed API specifications including request/response formats for chat and profile endpoints.

## Architecture

The application follows a modular architecture with:
- **Agent-based Backend**: Specialized AI agents handle different aspects of conversation processing
- **Component-based Frontend**: Reusable React components for chat, profiles, and recommendations
- **Service Layer**: Abstraction for API calls with mock/real mode switching
- **Responsive Design**: Mobile-first approach with desktop optimizations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is proprietary to Economic Times. All rights reserved.