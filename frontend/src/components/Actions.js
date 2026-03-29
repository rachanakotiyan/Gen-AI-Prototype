import React from "react";

/**
 * Actions Component
 * Displays suggested next actions as a list
 * Matches backend response: actions = ["string", "string", ...]
 */
const Actions = ({ actions = [] }) => {
  if (!actions || actions.length === 0) {
    return (
      <div className="action-card card">
        <h3 className="card-title">🎯 Next Steps</h3>
        <p className="empty-state">
          Chat with me to discover your next actions
        </p>
      </div>
    );
  }

  return (
    <div className="action-card card">
      <h3 className="card-title">🎯 Next Steps</h3>
      <ul className="action-list">
        {actions.map((action, idx) => (
          <li key={idx} className="action-list-item">
            <span className="action-bullet">→</span>
            <span className="action-text">{action}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Actions;