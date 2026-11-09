/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        display: ["'Space Grotesk'", "sans-serif"],
        body: ["'Inter'", "sans-serif"],
        mono: ["'JetBrains Mono'", "monospace"],
      },
      colors: {
        vault: {
          950: "#0b0620",
          900: "#120b2e",
          800: "#1c1240",
          700: "#2a1b5c",
        },
        accent: {
          violet: "#7c5cff",
          cyan: "#22d3ee",
        },
        strength: {
          weak: "#ef4444",
          medium: "#f59e0b",
          strong: "#10b981",
        },
      },
      backgroundImage: {
        "vault-gradient":
          "radial-gradient(circle at 15% 0%, rgba(124,92,255,0.25), transparent 45%), radial-gradient(circle at 85% 100%, rgba(34,211,238,0.18), transparent 50%)",
        "vault-gradient-light":
          "radial-gradient(circle at 15% 0%, rgba(124,92,255,0.14), transparent 45%), radial-gradient(circle at 85% 100%, rgba(34,211,238,0.12), transparent 50%)",
      },
      boxShadow: {
        glass: "0 8px 32px 0 rgba(11, 6, 32, 0.35)",
        "glow-violet": "0 0 24px 0 rgba(124, 92, 255, 0.35)",
      },
      keyframes: {
        "tile-flip": {
          "0%": { transform: "rotateX(90deg)", opacity: "0" },
          "100%": { transform: "rotateX(0deg)", opacity: "1" },
        },
        "bar-fill": {
          "0%": { width: "0%" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
      },
      animation: {
        "tile-flip": "tile-flip 0.4s ease-out backwards",
        shimmer: "shimmer 2.5s linear infinite",
      },
    },
  },
  plugins: [],
};
