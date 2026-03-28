/**
 * API Service Layer
 * Handles communication with the backend API
 * Supports toggle between mock and real API
 */

import mockChatAPI from "./mock_api";

// Toggle this to switch between mock and real API
const USE_MOCK_API = true;
const API_BASE_URL = "http://localhost:5000"; // Backend URL

/**
 * Send a chat message to the API
 * @param {string} message - User's message
 * @param {string} userId - User ID (optional, managed by component)
 * @returns {Promise<Object>} - API response
 */
export const sendChatMessage = async (message, userId = null) => {
  const payload = {
    message,
    ...(userId && { user_id: userId }),
  };

  if (USE_MOCK_API) {
    return await mockChatAPI(payload);
  }

  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("API call failed:", error);
    throw error;
  }
};

/**
 * Get API status (useful for debugging)
 */
export const getAPIStatus = () => ({
  usingMock: USE_MOCK_API,
  apiUrl: USE_MOCK_API ? "MOCK API" : API_BASE_URL,
});

export default { sendChatMessage, getAPIStatus };
