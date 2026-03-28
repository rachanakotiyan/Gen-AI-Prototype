import { useState, useCallback } from "react";
import ChatBox from "./components/ChatBox";
import ProfileCard from "./components/ProfileCard";
import Recommendations from "./components/Recommendations";
import Actions from "./components/Actions";
import { sendChatMessage } from "./services/api_service";
import "./App.css";

/**
 * Main App Component
 * AI-powered financial concierge chat interface with structured data display
 */
function App() {
  const [messages, setMessages] = useState([]);
  const [userId, setUserId] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [profile, setProfile] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [nextAction, setNextAction] = useState(null);

  const handleSendMessage = useCallback(
    async (messageText) => {
      if (!messageText.trim() || isLoading) return;

      try {
        // Add user message to chat
        const userMessage = {
          text: messageText,
          sender: "user",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, userMessage]);
        setIsLoading(true);

        // Send to API
        const response = await sendChatMessage(messageText, userId);

        // Save user_id from first response
        if (!userId && response.user_id) {
          setUserId(response.user_id);
        }

        // Add AI response to chat
        const aiMessage = {
          text: response.response,
          sender: "ai",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, aiMessage]);

        // Update structured data
        if (response.profile) {
          setProfile(response.profile);
        }
        if (response.recommendations) {
          setRecommendations(response.recommendations);
        }
        if (response.next_action) {
          setNextAction(response.next_action);
        }
      } catch (error) {
        console.error("Error sending message:", error);

        // Add error message
        const errorMessage = {
          text: "Sorry, I encountered an error. Please try again.",
          sender: "ai",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMessage]);
      } finally {
        setIsLoading(false);
      }
    },
    [userId, isLoading]
  );

  return (
    <div className="app-container">
      {/* Header */}
      <header className="app-header">
        <div className="header-content">
          <div className="header-title">
            <h1>💰 Financial Concierge AI</h1>
            <p>Your personalized financial advisor</p>
          </div>
          <div className="header-badge">
            {userId && <span className="session-badge">Session Active</span>}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="app-main">
        {/* Chat Section (70%) */}
        <section className="chat-section">
          <ChatBox
            messages={messages}
            onSend={handleSendMessage}
            isLoading={isLoading}
          />
        </section>

        {/* Sidebar Section (30%) */}
        <aside className="sidebar-section">
          <div className="sidebar-content">
            <ProfileCard profile={profile} />
            <Recommendations recommendations={recommendations} />
            <Actions nextAction={nextAction} />
          </div>
        </aside>
      </main>

      {/* Footer */}
      <footer className="app-footer">
        <p>
          💡 Powered by AI | All recommendations are for educational purposes
        </p>
      </footer>
    </div>
  );
}

export default App;