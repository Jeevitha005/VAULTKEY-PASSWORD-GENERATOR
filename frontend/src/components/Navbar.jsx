import { FiShield } from "react-icons/fi";
import ThemeToggle from "./ThemeToggle";

const TABS = [
  { id: "generator", label: "Generator" },
  { id: "history", label: "History" },
];

export default function Navbar({ activeTab, onTabChange, theme, onToggleTheme }) {
  return (
    <header className="sticky top-0 z-20 border-b border-white/10 bg-white/60 dark:bg-vault-950/60 backdrop-blur-xl">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
        <div className="flex items-center gap-2 font-display text-lg font-semibold">
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-accent-violet to-accent-cyan text-white shadow-glow-violet">
            <FiShield />
          </span>
          Vaultkey
        </div>

        <nav className="flex items-center gap-1 rounded-2xl bg-vault-950/5 dark:bg-white/5 p-1">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              type="button"
              onClick={() => onTabChange(tab.id)}
              className={`rounded-xl px-4 py-2 text-sm font-medium transition-colors ${
                activeTab === tab.id
                  ? "bg-white dark:bg-vault-800 shadow-sm text-vault-950 dark:text-white"
                  : "text-vault-950/60 dark:text-slate-400 hover:text-vault-950 dark:hover:text-white"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>

        <ThemeToggle theme={theme} onToggle={onToggleTheme} />
      </div>
    </header>
  );
}
