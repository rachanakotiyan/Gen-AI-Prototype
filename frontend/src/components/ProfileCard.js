import React from "react";

/**
 * ProfileCard Component
 * Displays extracted user profile information
 */
const ProfileCard = ({ profile }) => {
  if (!profile) {
    return (
      <div className="profile-card">
        <h3 className="card-title">👤 Your Profile</h3>
        <p className="empty-state">
          Chat with me to create your personalized profile
        </p>
      </div>
    );
  }

  const {
    user_type = "Unknown",
    risk_level = "Unknown",
    experience_level = "Unknown",
    interests = [],
  } = profile;

  const getUserTypeIcon = (type) => {
    const icons = {
      student: "🎓",
      professional: "💼",
      entrepreneur: "🚀",
      investor: "📈",
    };
    return icons[type] || "👤";
  };

  const getRiskIcon = (risk) => {
    const icons = {
      low: "🛡️",
      medium: "⚖️",
      high: "⚡",
    };
    return icons[risk] || "❓";
  };

  const getExperienceIcon = (level) => {
    const icons = {
      beginner: "🌱",
      intermediate: "📚",
      advanced: "🎯",
    };
    return icons[level] || "❓";
  };

  return (
    <div className="profile-card card">
      <h3 className="card-title">👤 Your Profile</h3>

      <div className="profile-item">
        <span className="profile-label">
          {getUserTypeIcon(user_type)} User Type
        </span>
        <span className="profile-value">{user_type}</span>
      </div>

      <div className="profile-item">
        <span className="profile-label">
          {getRiskIcon(risk_level)} Risk Level
        </span>
        <span className="profile-value">{risk_level}</span>
      </div>

      <div className="profile-item">
        <span className="profile-label">
          {getExperienceIcon(experience_level)} Experience
        </span>
        <span className="profile-value">{experience_level}</span>
      </div>

      {interests && interests.length > 0 && (
        <div className="profile-interests">
          <span className="profile-label">💡 Interests</span>
          <div className="interests-tags">
            {interests.map((interest, idx) => (
              <tag key={idx} className="interest-tag">
                #{interest}
              </tag>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfileCard;