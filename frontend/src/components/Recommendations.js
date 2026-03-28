import React from "react";

/**
 * Recommendations Component
 * Displays list of recommendations with service, reason, and clickable URLs
 */
const Recommendations = ({ recommendations = [] }) => {
  if (!recommendations || recommendations.length === 0) {
    return (
      <div className="recommendations-card card">
        <h3 className="card-title">💡 Recommendations</h3>
        <p className="empty-state">
          Chat with me to receive personalized recommendations
        </p>
      </div>
    );
  }

  return (
    <div className="recommendations-card card">
      <h3 className="card-title">💡 Recommendations</h3>
      <div className="recommendations-list">
        {recommendations.map((rec, idx) => (
          <div key={idx} className="recommendation-item">
            <div className="recommendation-header">
              <h4 className="recommendation-service">{rec.service}</h4>
              <a
                href={rec.url}
                target="_blank"
                rel="noopener noreferrer"
                className="recommendation-link-btn"
                title="Open in new tab"
              >
                ↗
              </a>
            </div>
            <p className="recommendation-reason">{rec.reason}</p>
            <a
              href={rec.url}
              target="_blank"
              rel="noopener noreferrer"
              className="recommendation-link"
            >
              Learn More →
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Recommendations;