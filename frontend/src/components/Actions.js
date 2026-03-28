import React from "react";

/**
 * Actions Component
 * Displays the suggested next action as a prominent CTA card
 */
const Actions = ({ nextAction = null }) => {
  if (!nextAction) {
    return (
      <div className="action-card card">
        <h3 className="card-title">🎯 Next Steps</h3>
        <p className="empty-state">
          Chat with me to discover your next action
        </p>
      </div>
    );
  }

  const {
    action_title = "Get Started",
    action_description = "",
    cta_text = "Take Action",
    cta_url = "#",
  } = nextAction;

  return (
    <div className="action-card card cta-card">
      <h3 className="card-title">🎯 Next Steps</h3>
      <div className="action-content">
        <h4 className="action-title">{action_title}</h4>
        <p className="action-description">{action_description}</p>
        <a href={cta_url} target="_blank" rel="noopener noreferrer" className="cta-button">
          {cta_text}
        </a>
      </div>
    </div>
  );
};

export default Actions;