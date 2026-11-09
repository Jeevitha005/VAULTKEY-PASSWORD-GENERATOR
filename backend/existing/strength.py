"""Score password strength using entropy and simple pattern heuristics."""

import math
import re
import string

COMMON_PATTERNS = ("1234", "abcd", "password", "qwerty", "0000", "letmein")


def calculate_entropy(password):
    """Estimate entropy in bits based on the character pool the password draws from."""
    pool_size = 0
    if any(char in string.ascii_lowercase for char in password):
        pool_size += 26
    if any(char in string.ascii_uppercase for char in password):
        pool_size += 26
    if any(char in string.digits for char in password):
        pool_size += 10
    if any(char in string.punctuation for char in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def has_common_pattern(password):
    """Check the password against a small list of predictable substrings."""
    lowered = password.lower()
    return any(pattern in lowered for pattern in COMMON_PATTERNS)


def has_repeated_characters(password, max_repeat=3):
    """Detect runs of the same character repeated max_repeat or more times."""
    pattern = r"(.)\1{" + str(max_repeat - 1) + r",}"
    return re.search(pattern, password) is not None


def check_strength(password):
    """Return a strength label of Weak, Medium, or Strong for the given password."""
    if not password:
        return "Weak"

    entropy = calculate_entropy(password)

    if has_common_pattern(password) or has_repeated_characters(password):
        entropy -= 20

    if entropy < 40:
        return "Weak"
    if entropy < 70:
        return "Medium"
    return "Strong"


def strength_report(password):
    """Return a dict with entropy, label, and length for display or logging."""
    return {
        "password_length": len(password),
        "entropy_bits": round(calculate_entropy(password), 2),
        "strength": check_strength(password),
    }
