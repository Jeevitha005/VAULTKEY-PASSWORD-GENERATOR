const TIPS = [
  "A 16-character password with symbols can take centuries to brute-force.",
  "Never reuse the same password across different accounts.",
  "Password managers make long, unique passwords painless to use.",
  "Enable two-factor authentication anywhere it's offered.",
  "Passphrases of random words can be both strong and memorable.",
  "Avoid dictionary words, birthdays, and keyboard patterns like 'qwerty'.",
  "Excluding similar characters (l, 1, O, 0) helps when typing passwords manually.",
  "Longer beats more complex: length adds more entropy than symbols alone.",
  "Rotate credentials immediately after any service reports a data breach.",
  "Store recovery codes somewhere separate from your main password vault.",
];

/** Return a random security tip string. */
export function getRandomTip() {
  return TIPS[Math.floor(Math.random() * TIPS.length)];
}
