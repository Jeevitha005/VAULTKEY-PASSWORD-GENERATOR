import { FiRotateCcw } from "react-icons/fi";
import CheckboxOption from "./CheckboxOption";
import LengthSlider from "./LengthSlider";

export default function OptionsPanel({ options, onChange, onReset }) {
  function updateOption(key, value) {
    onChange({ ...options, [key]: value });
  }

  return (
    <div className="glass-panel flex flex-col gap-5 p-5 sm:p-6">
      <div className="flex items-center justify-between">
        <h2 className="font-display text-sm font-semibold uppercase tracking-wide text-vault-950/60 dark:text-slate-400">
          Options
        </h2>
        <button
          type="button"
          onClick={onReset}
          className="flex items-center gap-1.5 text-xs font-medium text-vault-950/50 dark:text-slate-400 hover:text-accent-violet"
        >
          <FiRotateCcw /> Reset
        </button>
      </div>

      <LengthSlider
        length={options.length}
        minLength={options.min_length}
        maxLength={options.max_length}
        onChange={(value) => updateOption("length", value)}
      />

      <div className="grid grid-cols-1 gap-1 sm:grid-cols-2">
        <CheckboxOption
          label="Uppercase (A-Z)"
          checked={options.use_uppercase}
          onChange={(value) => updateOption("use_uppercase", value)}
        />
        <CheckboxOption
          label="Lowercase (a-z)"
          checked={options.use_lowercase}
          onChange={(value) => updateOption("use_lowercase", value)}
        />
        <CheckboxOption
          label="Numbers (0-9)"
          checked={options.use_numbers}
          onChange={(value) => updateOption("use_numbers", value)}
        />
        <CheckboxOption
          label="Symbols (!@#$)"
          checked={options.use_symbols}
          onChange={(value) => updateOption("use_symbols", value)}
        />
        <CheckboxOption
          label="Exclude similar characters (l, 1, O, 0)"
          checked={options.exclude_ambiguous}
          onChange={(value) => updateOption("exclude_ambiguous", value)}
        />
      </div>
    </div>
  );
}
