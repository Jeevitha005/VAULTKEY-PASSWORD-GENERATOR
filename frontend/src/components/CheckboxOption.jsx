export default function CheckboxOption({ label, checked, onChange }) {
  return (
    <label className="flex cursor-pointer items-center justify-between gap-3 rounded-xl px-1 py-2 text-sm">
      <span className="text-vault-950/80 dark:text-slate-300">{label}</span>
      <span className="relative inline-flex h-6 w-11 shrink-0 items-center">
        <input
          type="checkbox"
          checked={checked}
          onChange={(event) => onChange(event.target.checked)}
          className="peer sr-only"
        />
        <span
          className="h-6 w-11 rounded-full bg-vault-950/15 dark:bg-white/15 transition-colors
            peer-checked:bg-gradient-to-r peer-checked:from-accent-violet peer-checked:to-accent-cyan"
        />
        <span
          className="absolute left-0.5 h-5 w-5 rounded-full bg-white shadow transition-transform
            peer-checked:translate-x-5"
        />
      </span>
    </label>
  );
}
