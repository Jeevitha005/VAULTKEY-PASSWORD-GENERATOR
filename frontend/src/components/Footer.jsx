export default function Footer() {
  return (
    <footer className="mx-auto max-w-5xl px-6 py-10 text-center text-sm text-vault-950/50 dark:text-slate-500">
      <p>
        Built with the original Password Generator CLI logic, wrapped in a FastAPI + React interface.
      </p>
      <p className="mt-1">&copy; {new Date().getFullYear()} Vaultkey. All secrets stay on your machine.</p>
    </footer>
  );
}
