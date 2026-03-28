import React from "react";

function Message({ text, sender }) {
  return (
    <div style={{ textAlign: sender === "user" ? "right" : "left" }}>
      <span>{text}</span>
    </div>
  );
}

export default Message;