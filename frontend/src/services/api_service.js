/**
 * API Service Layer
 * Handles communication with the backend API
 * Toggle USE_MOCK to switch between mock and real API
 */

import mockChatAPI from "./mock_api";
import realChatAPI from "../api/real_api";

// Set to false to use the live backend
const USE_MOCK = false;

/**
 * Send a chat message to the API
 * @param {string} message - User's message
 * @param {string|null} userId - Session user ID
 * @returns {Promise<Object>} - API response
 */
export const sendChatMessage = async (message, userId = null) => {
  const payload = {
    message,
    user_id: userId || undefined,
  };

  if (USE_MOCK) {
    return await mockChatAPI(payload);
  }

  return await realChatAPI(payload);
};

/**
 * Get API status (useful for debugging)
 */
export const getAPIStatus = () => ({
  usingMock: USE_MOCK,
  apiUrl: USE_MOCK
    ? "MOCK API"
    : process.env.REACT_APP_API_URL || "https://gen-ai-prototype-production.up.railway.app",
});

const apiService = { sendChatMessage, getAPIStatus };
export default apiService;
