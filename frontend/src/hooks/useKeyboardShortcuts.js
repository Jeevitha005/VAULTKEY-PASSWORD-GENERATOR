import { useEffect } from "react";

/**
 * Bind single-key keyboard shortcuts to handlers.
 * @param {Record<string, () => void>} shortcuts - e.g. { g: generate, c: copy }
 * @param {boolean} enabled - disable shortcuts (e.g. while a text field is focused)
 */
export default function useKeyboardShortcuts(shortcuts, enabled = true) {
  useEffect(() => {
    if (!enabled) return undefined;

    function handleKeyDown(event) {
      const target = event.target;
      const isTyping =
        target instanceof HTMLElement &&
        (target.tagName === "INPUT" || target.tagName === "TEXTAREA" || target.isContentEditable);

      if (isTyping) return;

      const key = event.key.toLowerCase();
      const handler = shortcuts[key];
      if (handler) {
        event.preventDefault();
        handler();
      }
    }

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [shortcuts, enabled]);
}
