import { useState } from "react";
import ChatBox from "./components/ChatBox";
import Message from "./components/Message";
import ProfileCard from "./components/ProfileCard";
import Recommendations from "./components/Recommendations";
import Actions from "./components/Actions";

function App() {
  const [messages, setMessages] = useState([]);
  const [data, setData] = useState(null);

  const handleSend = async (msg) => {
    // show user message
    setMessages((prev) => [...prev, { text: msg, sender: "user" }]);

    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          session_id: "abc123",
          message: msg,
        }),
      });

      const response = await res.json();

      // show bot reply
      setMessages((prev) => [
        ...prev,
        { text: response.reply, sender: "bot" },
      ]);

      // update structured UI
      setData({
        profile: `${response.profile.role} (${response.profile.experience_level})`,
        recommendations: response.recommendations.map(r => r.name),
        actions: ["Explore now", "Learn more"],
      });

    } catch (error) {
      console.error("API Error:", error);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "20px" }}>
      <h1>ET AI Concierge 💡</h1>

      {/* Chat messages */}
      <div style={{ minHeight: "300px" }}>
        {messages.map((m, i) => (
          <Message key={i} text={m.text} sender={m.sender} />
        ))}
      </div>

      {/* Chat input */}
      <ChatBox onSend={handleSend} />

      {/* Structured Output */}
      {data && (
        <div>
          <ProfileCard profile={data.profile} />
          <Recommendations items={data.recommendations} />
          <Actions items={data.actions} />
        </div>
      )}
    </div>
  );
}

export default App;