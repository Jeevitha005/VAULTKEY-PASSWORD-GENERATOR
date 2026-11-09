import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { FiRefreshCw, FiZap } from "react-icons/fi";
import { getRandomTip } from "../utils/tips";

export default function TipBanner() {
  const [tip, setTip] = useState(getRandomTip);

  return (
    <div className="glass-panel flex items-center justify-between gap-4 px-5 py-3 text-sm">
      <div className="flex items-center gap-3 text-vault-950/80 dark:text-slate-300">
        <FiZap className="shrink-0 text-accent-violet" />
        <AnimatePresence mode="wait">
          <motion.span
            key={tip}
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            transition={{ duration: 0.2 }}
          >
            {tip}
          </motion.span>
        </AnimatePresence>
      </div>
      <button
        type="button"
        onClick={() => setTip(getRandomTip())}
        aria-label="Show another tip"
        className="shrink-0 rounded-full p-2 text-vault-950/50 dark:text-slate-400 hover:bg-vault-950/5 dark:hover:bg-white/10"
      >
        <FiRefreshCw />
      </button>
    </div>
  );
}
