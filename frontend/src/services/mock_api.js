/**
 * Mock API Service
 * Returns sample data matching the API contract for testing and development
 */

const mockResponses = [
  {
    user_id: "user_demo_001",
    response: "Great question! Based on your interest in AI and stocks, I'd recommend starting with dividend aristocrats. These are companies that have increased dividends for 25+ consecutive years, making them relatively stable for beginner investors.",
    profile: {
      user_type: "student",
      risk_level: "low",
      experience_level: "beginner",
      interests: ["stocks", "AI", "dividends"]
    },
    recommendations: [
      {
        service: "ET Prime",
        reason: "Comprehensive guide on dividend investing with AI-powered market analysis",
        url: "https://economictimes.indiatimes.com/etprime"
      },
      {
        service: "Investopedia Academy",
        reason: "Free courses on fundamentals perfect for beginners",
        url: "https://academy.investopedia.com"
      }
    ],
    next_action: {
      action_title: "Learn Dividend Basics",
      action_description: "Complete the beginner's guide to dividend investing in 10 minutes",
      cta_text: "Start Learning →",
      cta_url: "https://example.com/dividend-guide"
    }
  },
  {
    user_id: "user_demo_001",
    response: "I see you're interested in tech stocks too! Companies like Microsoft and Apple have strong fundamentals and accessibility for retail investors. Let me create a personalized watchlist for you based on your experience level.",
    profile: {
      user_type: "student",
      risk_level: "low",
      experience_level: "beginner",
      interests: ["stocks", "AI", "tech", "dividends"]
    },
    recommendations: [
      {
        service: "Seeking Alpha",
        reason: "Real-time stock analysis and AI-powered insights on tech companies",
        url: "https://seekingalpha.com"
      },
      {
        service: "Robinhood Learn",
        reason: "Interactive tutorials on building your first tech portfolio",
        url: "https://learn.robinhood.com"
      }
    ],
    next_action: {
      action_title: "Create Your First Portfolio",
      action_description: "Set up a diversified tech-focused portfolio with 5 stable blue-chip stocks",
      cta_text: "Build Portfolio →",
      cta_url: "https://example.com/portfolio-builder"
    }
  },
  {
    user_id: "user_demo_001",
    response: "Perfect! I've analyzed your preferences and risk tolerance. Here are my top recommendations for your financial journey. Start with the ETF guide to understand diversification, then explore AI-driven market research tools.",
    profile: {
      user_type: "student",
      risk_level: "low",
      experience_level: "beginner",
      interests: ["stocks", "AI", "tech", "dividends", "ETFs"]
    },
    recommendations: [
      {
        service: "Vanguard Academy",
        reason: "Expert-led courses on ETFs and passive investing strategies",
        url: "https://www.vanguard.com"
      },
      {
        service: "FinTech Insider",
        reason: "Latest trends in AI-powered investment tools and robo-advisors",
        url: "https://fintech.example.com"
      },
      {
        service: "Interactive Brokers",
        reason: "Advanced tools for learning quantitative analysis with AI",
        url: "https://www.interactivebrokers.com"
      }
    ],
    next_action: {
      action_title: "Join the Community",
      action_description: "Connect with other beginner investors and get real-time market insights",
      cta_text: "Join →",
      cta_url: "https://example.com/community"
    }
  }
];

let responseIndex = 0;

/**
 * Simulate API call with delay
 * @param {Object} payload - { user_id, message }
 * @returns {Promise<Object>} - API response matching the contract
 */
export const mockChatAPI = async (payload) => {
  // Simulate network delay (1-2 seconds)
  await new Promise((resolve) =>
    setTimeout(resolve, 800 + Math.random() * 1200)
  );

  // Cycle through mock responses
  const response = mockResponses[responseIndex % mockResponses.length];
  responseIndex++;

  return response;
};

export default mockChatAPI;
