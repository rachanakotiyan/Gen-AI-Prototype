import React, { useState, useEffect, useRef } from "react";
import Message from "./Message";

/**
 * ChatBox Component
 * Main chat window with message display and input
 */
const ChatBox = ({ messages, onSend, isLoading }) => {
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim() || isLoading) return;
    onSend(input);
    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-box">
      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="chat-empty">
            <div className="chat-empty-icon">💬</div>
            <h2>Start Your Financial Journey</h2>
            <p>
              Ask me anything about investing, saving, or building wealth. I'll
              provide personalized recommendations based on your profile.
            </p>
          </div>
        ) : (
          messages.map((msg, idx) => (
            <Message
              key={idx}
              text={msg.text}
              sender={msg.sender}
              timestamp={msg.timestamp}
            />
          ))
        )}

        {isLoading && (
          <div className="message-wrapper ai">
            <div className="message ai-message typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-section">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask about investments, savings, portfolio tips... (Shift+Enter for new line)"
          disabled={isLoading}
          className="chat-input"
          rows="3"
        />
        <button
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
          className="send-button"
        >
          {isLoading ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
};

export default ChatBox;