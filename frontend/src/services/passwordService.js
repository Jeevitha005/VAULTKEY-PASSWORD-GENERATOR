import api from "./api";

/**
 * Request a new password from the backend generator.
 * @param {object} options - length, character-set toggles, exclude_ambiguous
 */
export async function generatePassword(options) {
  const { data } = await api.post("/generate", options);
  return data;
}

/**
 * Score the strength of an arbitrary password without saving it to history.
 * @param {string} password
 */
export async function checkStrength(password) {
  const { data } = await api.post("/strength", { password });
  return data;
}

/**
 * Fetch the most recent generated passwords.
 * @param {number} limit
 */
export async function fetchHistory(limit = 50) {
  const { data } = await api.get("/history", { params: { limit } });
  return data;
}

/** Delete every stored history record. */
export async function clearHistory() {
  const { data } = await api.delete("/history");
  return data;
}

/** Build the direct download URL for exporting history as a .txt file. */
export function getExportTxtUrl() {
  return `${api.defaults.baseURL}/export/txt`;
}

/** Build the direct download URL for exporting history as a .csv file. */
export function getExportCsvUrl() {
  return `${api.defaults.baseURL}/export/csv`;
}
