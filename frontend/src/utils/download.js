/**
 * Trigger a browser download for a same-origin/remote URL (e.g. a backend
 * export endpoint) by momentarily creating and clicking an anchor tag.
 * @param {string} url
 * @param {string} [filename]
 */
export function downloadFromUrl(url, filename) {
  const anchor = document.createElement("a");
  anchor.href = url;
  if (filename) anchor.download = filename;
  anchor.rel = "noopener";
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
}

/**
 * Download arbitrary client-side data as a JSON file (e.g. a snapshot of the
 * currently loaded history), without a round trip to the server.
 * @param {unknown} data
 * @param {string} filename
 */
export function downloadJson(data, filename) {
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  downloadFromUrl(url, filename);
  URL.revokeObjectURL(url);
}
