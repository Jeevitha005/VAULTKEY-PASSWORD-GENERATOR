import { useState } from "react";
import { FiCheck, FiCopy } from "react-icons/fi";
import { copyToClipboard } from "../utils/clipboard";
import toast from "react-hot-toast";

const BADGE_STYLES = {
  Weak: "bg-strength-weak/10 text-strength-weak",
  Medium: "bg-strength-medium/10 text-strength-medium",
  Strong: "bg-strength-strong/10 text-strength-strong",
};

export default function HistoryItem({ entry }) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    const success = await copyToClipboard(entry.password);
    if (success) {
      setCopied(true);
      toast.success("Copied from history");
      setTimeout(() => setCopied(false), 1200);
    }
  }

  const timestamp = new Date(entry.created_at).toLocaleString();

  return (
    <div className="flex items-center justify-between gap-3 rounded-xl px-3 py-3 hover:bg-vault-950/[0.03] dark:hover:bg-white/[0.04]">
      <div className="min-w-0 flex-1">
        <p className="truncate font-mono text-sm text-vault-950 dark:text-slate-100">{entry.password}</p>
        <p className="mt-0.5 text-xs text-vault-950/40 dark:text-slate-500">{timestamp}</p>
      </div>

      <span className={`shrink-0 rounded-full px-2.5 py-1 text-xs font-medium ${BADGE_STYLES[entry.strength] ?? ""}`}>
        {entry.strength}
      </span>

      <button
        type="button"
        onClick={handleCopy}
        aria-label="Copy password"
        className="shrink-0 rounded-full p-2 text-vault-950/40 dark:text-slate-400 hover:bg-vault-950/5 dark:hover:bg-white/10"
      >
        {copied ? <FiCheck className="text-strength-strong" /> : <FiCopy />}
      </button>
    </div>
  );
}
