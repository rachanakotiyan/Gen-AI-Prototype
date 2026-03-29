import React from "react";

/**
 * Recommendations Component
 * Displays list of recommendations
 * Matches backend response: [{ title, reason }]
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
              {/* Backend sends "title" (not "service") */}
              <h4 className="recommendation-service">{rec.title}</h4>
            </div>
            <p className="recommendation-reason">{rec.reason}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Recommendations;