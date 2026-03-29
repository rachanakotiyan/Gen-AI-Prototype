/**
 * Real API Service
 * Connects to the live backend or falls back to env variable
 */

const BASE_URL = process.env.REACT_APP_API_URL || "https://gen-ai-prototype-production.up.railway.app";

/**
 * Send a chat message to the real backend
 * @param {{ message: string, user_id: string|null }} payload
 * @returns {Promise<Object>} - API response
 */
const realChatAPI = async (payload) => {
  try {
    console.log(`[INFO] API Request to: ${BASE_URL}/api/chat`);
    
    const response = await fetch(`${BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      const errorMessage = errorData.detail || `API error: ${response.status} ${response.statusText}`;
      console.error(`[ERROR] API Error [${response.status}]:`, errorMessage);
      throw new Error(errorMessage);
    }

    const data = await response.json();
    console.log("[OK] API Response received successfully");
    return data;
  } catch (error) {
    console.error("[ERROR] API Request failed:", error.message);
    throw error;
  }
};

export default realChatAPI;
