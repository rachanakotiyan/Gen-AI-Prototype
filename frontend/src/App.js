import { useState, useCallback } from "react";
import ChatBox from "./components/ChatBox";
import ProfileCard from "./components/ProfileCard";
import Recommendations from "./components/Recommendations";
import Actions from "./components/Actions";
import { sendChatMessage, getAPIStatus } from "./services/api_service";
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
  const [actions, setActions] = useState([]);

  const apiStatus = getAPIStatus();

  const handleSendMessage = useCallback(
    async (messageText) => {
      if (!messageText.trim() || isLoading) return;

      try {
        // Add user message to chat immediately
        const userMessage = {
          text: messageText,
          sender: "user",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, userMessage]);
        setIsLoading(true);

        // Send to API
        const response = await sendChatMessage(messageText, userId);

        // Persist user_id from first response for session continuity
        if (!userId && response.user_id) {
          setUserId(response.user_id);
        }

        // Add AI reply to chat — field is "reply" (new schema) or "response" (old schema)
        const aiMessage = {
          text: response.reply || response.response || "No response received.",
          sender: "ai",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, aiMessage]);

        // Update sidebar panels with structured data
        if (response.profile) {
          setProfile(response.profile);
        }

        if (response.recommendations) {
          // ensure "title" exists even if backend returned "service" (old schema)
          const mappedRecs = response.recommendations.map((r) => ({
            ...r,
            title: r.title || r.service,
          }));
          setRecommendations(mappedRecs);
        }

        if (response.actions) {
          setActions(response.actions);
        } else if (response.next_action) {
          // fallback for old schema
          const fallbackActions = [];
          if (response.next_action.action_title) {
            fallbackActions.push(`${response.next_action.action_title}: ${response.next_action.action_description || ""}`);
          }
          setActions(fallbackActions);
        }
      } catch (error) {
        console.error("Error sending message:", error);

        const errorMessage = {
          text: "Sorry, I encountered an error reaching the server. Please try again.",
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
            <span
              className={`api-badge ${apiStatus.usingMock ? "mock" : "live"}`}
            >
              {apiStatus.usingMock ? "🟡 Mock" : "🟢 Live"}
            </span>
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
            <Actions actions={actions} />
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