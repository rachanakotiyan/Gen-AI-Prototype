import React from "react";

/**
 * Message Component
 * Displays individual messages in the chat (user or AI)
 */
const Message = ({ text, sender, timestamp }) => {
  const isUser = sender === "user";

  return (
    <div className={`message-wrapper ${isUser ? "user" : "ai"}`}>
      <div className={`message ${isUser ? "user-message" : "ai-message"}`}>
        <p className="message-text">{text}</p>
        {timestamp && (
          <span className="message-time">
            {new Date(timestamp).toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            })}
          </span>
        )}
      </div>
    </div>
  );
};

export default Message;