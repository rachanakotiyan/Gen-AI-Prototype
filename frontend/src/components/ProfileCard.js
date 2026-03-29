import React from "react";

/**
 * ProfileCard Component
 * Displays extracted user profile information
 * Matches backend response: { type, risk, interests }
 */
const ProfileCard = ({ profile }) => {
  if (!profile) {
    return (
      <div className="profile-card card">
        <h3 className="card-title">👤 Your Profile</h3>
        <p className="empty-state">
          Chat with me to create your personalized profile
        </p>
      </div>
    );
  }

  // Backend sends: profile.type, profile.risk, profile.interests (new scheme)
  // or user_type, risk_level (old scheme deployed)
  const type = profile.type || profile.user_type || "Unknown";
  const risk = profile.risk || profile.risk_level || "Unknown";
  const interests = profile.interests || [];

  const getUserTypeIcon = (t) => {
    const icons = {
      student: "🎓",
      professional: "💼",
      entrepreneur: "🚀",
      investor: "📈",
    };
    return icons[t] || "👤";
  };

  const getRiskIcon = (r) => {
    const icons = {
      low: "🛡️",
      medium: "⚖️",
      high: "⚡",
    };
    return icons[r] || "❓";
  };

  return (
    <div className="profile-card card">
      <h3 className="card-title">👤 Your Profile</h3>

      <div className="profile-item">
        <span className="profile-label">
          {getUserTypeIcon(type)} User Type
        </span>
        <span className="profile-value">{type}</span>
      </div>

      <div className="profile-item">
        <span className="profile-label">
          {getRiskIcon(risk)} Risk Level
        </span>
        <span className="profile-value">{risk}</span>
      </div>

      {interests && interests.length > 0 && (
        <div className="profile-interests">
          <span className="profile-label">💡 Interests</span>
          <div className="interests-tags">
            {interests.map((interest, idx) => (
              <span key={idx} className="interest-tag">
                #{interest}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfileCard;