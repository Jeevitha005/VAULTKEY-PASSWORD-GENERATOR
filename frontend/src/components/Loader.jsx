export default function Loader({ label = "Loading" }) {
  return (
    <div className="flex items-center justify-center gap-3 py-6 text-sm text-vault-950/60 dark:text-slate-400">
      <span
        className="h-5 w-5 animate-spin rounded-full border-2 border-accent-violet/30 border-t-accent-violet"
        aria-hidden="true"
      />
      {label}
    </div>
  );
}
