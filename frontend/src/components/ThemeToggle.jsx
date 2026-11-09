import { motion } from "framer-motion";
import { FiMoon, FiSun } from "react-icons/fi";

export default function ThemeToggle({ theme, onToggle }) {
  const isDark = theme === "dark";

  return (
    <button
      type="button"
      onClick={onToggle}
      aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
      className="relative flex h-10 w-10 items-center justify-center rounded-full
        bg-vault-950/5 dark:bg-white/5 border border-vault-950/10 dark:border-white/10
        transition-colors hover:bg-vault-950/10 dark:hover:bg-white/10"
    >
      <motion.span
        key={theme}
        initial={{ rotate: -90, opacity: 0 }}
        animate={{ rotate: 0, opacity: 1 }}
        transition={{ duration: 0.25 }}
        className="text-lg text-vault-950 dark:text-slate-100"
      >
        {isDark ? <FiSun /> : <FiMoon />}
      </motion.span>
    </button>
  );
}
