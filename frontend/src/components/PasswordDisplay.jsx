import { useState } from "react";
import { motion } from "framer-motion";
import { FiCheck, FiCopy, FiRefreshCw } from "react-icons/fi";
import { copyToClipboard } from "../utils/clipboard";
import toast from "react-hot-toast";

/**
 * Renders the generated password as individual "keycap" tiles that flip in,
 * evoking a terminal or physical keyboard — the page's signature element.
 */
export default function PasswordDisplay({ password, isLoading, onRegenerate }) {
  const [justCopied, setJustCopied] = useState(false);

  async function handleCopy() {
    if (!password) return;
    const success = await copyToClipboard(password);
    if (success) {
      setJustCopied(true);
      toast.success("Password copied to clipboard");
      setTimeout(() => setJustCopied(false), 1500);
    } else {
      toast.error("Couldn't copy automatically — select and copy manually.");
    }
  }

  return (
    <div className="glass-panel flex flex-col items-center gap-5 p-6 sm:p-8">
      <div
        className="flex w-full flex-wrap items-center justify-center gap-1.5 rounded-2xl
          bg-vault-950/[0.04] dark:bg-black/30 px-4 py-6 font-mono text-xl sm:text-2xl"
        style={{ perspective: "600px" }}
        aria-live="polite"
      >
        {password ? (
          password.split("").map((char, index) => (
            <motion.span
              key={`${password}-${index}`}
              initial={{ rotateX: 90, opacity: 0 }}
              animate={{ rotateX: 0, opacity: 1 }}
              transition={{ duration: 0.35, delay: index * 0.015 }}
              className="flex h-10 w-8 items-center justify-center rounded-lg
                bg-white dark:bg-vault-800 shadow-sm text-vault-950 dark:text-slate-100"
            >
              {char}
            </motion.span>
          ))
        ) : (
          <span className="text-vault-950/40 dark:text-slate-500">
            Press &ldquo;Generate&rdquo; to create a password
          </span>
        )}
      </div>

      <div className="flex w-full flex-col gap-3 sm:flex-row">
        <button
          type="button"
          onClick={onRegenerate}
          disabled={isLoading}
          className="btn-primary flex-1"
        >
          <FiRefreshCw className={isLoading ? "animate-spin" : ""} />
          {password ? "Generate again" : "Generate password"}
        </button>

        <button
          type="button"
          onClick={handleCopy}
          disabled={!password}
          className="btn-secondary flex-1 sm:flex-none"
        >
          {justCopied ? <FiCheck className="text-strength-strong" /> : <FiCopy />}
          {justCopied ? "Copied" : "Copy"}
        </button>
      </div>

      <p className="text-xs text-vault-950/40 dark:text-slate-500">
        Shortcuts: <kbd className="rounded bg-vault-950/5 dark:bg-white/10 px-1.5 py-0.5">G</kbd> generate,{" "}
        <kbd className="rounded bg-vault-950/5 dark:bg-white/10 px-1.5 py-0.5">C</kbd> copy
      </p>
    </div>
  );
}
