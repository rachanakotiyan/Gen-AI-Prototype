/**
 * Real API Service
 * Connects to the live backend at Railway
 */

const BASE_URL = "https://gen-ai-prototype-production.up.railway.app";

/**
 * Send a chat message to the real backend
 * @param {{ message: string, user_id: string|null }} payload
 * @returns {Promise<Object>} - API response
 */
const realChatAPI = async (payload) => {
  const response = await fetch(`${BASE_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }

  return await response.json();
};

export default realChatAPI;
