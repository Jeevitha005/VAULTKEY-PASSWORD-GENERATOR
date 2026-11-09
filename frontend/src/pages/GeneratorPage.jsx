import { useCallback, useEffect, useState } from "react";
import toast from "react-hot-toast";
import OptionsPanel from "../components/OptionsPanel";
import PasswordDisplay from "../components/PasswordDisplay";
import StrengthMeter from "../components/StrengthMeter";
import TipBanner from "../components/TipBanner";
import useLocalStorage from "../hooks/useLocalStorage";
import useKeyboardShortcuts from "../hooks/useKeyboardShortcuts";
import { copyToClipboard } from "../utils/clipboard";
import { generatePassword } from "../services/passwordService";

const DEFAULT_OPTIONS = {
  length: 16,
  min_length: 6,
  max_length: 64,
  use_uppercase: true,
  use_lowercase: true,
  use_numbers: true,
  use_symbols: true,
  exclude_ambiguous: false,
};

export default function GeneratorPage() {
  const [options, setOptions] = useLocalStorage("vaultkey-settings", DEFAULT_OPTIONS);
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerate = useCallback(async () => {
    setIsLoading(true);
    try {
      const data = await generatePassword(options);
      setResult(data);
    } catch (error) {
      toast.error(error.message || "Failed to generate a password.");
    } finally {
      setIsLoading(false);
    }
  }, [options]);

  useEffect(() => {
    handleGenerate();
    // Generate one password on first load only; subsequent option changes
    // wait for an explicit "Generate again" click or keyboard shortcut.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useKeyboardShortcuts({
    g: handleGenerate,
    c: () => {
      if (result?.password) copyToClipboard(result.password).then((ok) => {
        if (ok) toast.success("Password copied to clipboard");
      });
    },
  });

  function handleReset() {
    setOptions(DEFAULT_OPTIONS);
    toast.success("Settings reset to defaults");
  }

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="font-display text-2xl font-bold sm:text-3xl">Generate a secure password</h1>
        <p className="mt-1 text-sm text-vault-950/50 dark:text-slate-400">
          Powered by the original CLI generator &mdash; now with instant strength analysis.
        </p>
      </div>

      <TipBanner />

      <PasswordDisplay password={result?.password} isLoading={isLoading} onRegenerate={handleGenerate} />

      {result && (
        <StrengthMeter
          strength={result.strength}
          score={result.score}
          entropyBits={result.entropy_bits}
          crackTime={result.estimated_crack_time}
        />
      )}

      <OptionsPanel options={options} onChange={setOptions} onReset={handleReset} />
    </div>
  );
}
