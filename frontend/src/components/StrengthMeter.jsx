import { motion } from "framer-motion";

const STRENGTH_STYLES = {
  Weak: { color: "bg-strength-weak", text: "text-strength-weak" },
  Medium: { color: "bg-strength-medium", text: "text-strength-medium" },
  Strong: { color: "bg-strength-strong", text: "text-strength-strong" },
};

export default function StrengthMeter({ strength, score, entropyBits, crackTime }) {
  if (!strength) return null;

  const style = STRENGTH_STYLES[strength] ?? STRENGTH_STYLES.Weak;

  return (
    <div className="glass-panel flex flex-col gap-3 p-5">
      <div className="flex items-center justify-between text-sm font-medium">
        <span className={style.text}>{strength}</span>
        <span className="text-vault-950/50 dark:text-slate-400">{entropyBits.toFixed(1)} bits of entropy</span>
      </div>

      <div className="h-2.5 w-full overflow-hidden rounded-full bg-vault-950/10 dark:bg-white/10">
        <motion.div
          className={`h-full rounded-full ${style.color}`}
          initial={{ width: 0 }}
          animate={{ width: `${score}%` }}
          transition={{ duration: 0.6, ease: "easeOut" }}
        />
      </div>

      <p className="text-xs text-vault-950/50 dark:text-slate-400">
        Estimated time to crack offline: <span className="font-medium">{crackTime}</span>
      </p>
    </div>
  );
}
