export default function LengthSlider({ length, minLength, maxLength, onChange }) {
  return (
    <div>
      <div className="mb-2 flex items-center justify-between text-sm font-medium">
        <label htmlFor="length-slider">Password length</label>
        <span className="rounded-lg bg-accent-violet/10 px-2 py-0.5 font-mono text-accent-violet">
          {length}
        </span>
      </div>
      <input
        id="length-slider"
        type="range"
        min={minLength}
        max={maxLength}
        value={length}
        onChange={(event) => onChange(Number(event.target.value))}
        className="h-2 w-full cursor-pointer appearance-none rounded-full bg-vault-950/10 dark:bg-white/10
          accent-accent-violet"
      />
      <div className="mt-1 flex justify-between text-xs text-vault-950/40 dark:text-slate-500">
        <span>{minLength}</span>
        <span>{maxLength}</span>
      </div>
    </div>
  );
}
