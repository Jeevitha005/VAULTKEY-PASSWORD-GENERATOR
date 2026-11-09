import { useEffect, useState } from "react";

/**
 * Persist a piece of state to localStorage under the given key.
 * Falls back gracefully to the initial value if localStorage is unavailable.
 */
export default function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key);
      return stored !== null ? JSON.parse(stored) : initialValue;
    } catch {
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Storage unavailable (e.g. private browsing) — fail silently.
    }
  }, [key, value]);

  return [value, setValue];
}
