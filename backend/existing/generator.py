"""Generate cryptographically secure passwords from configurable character pools."""

import secrets
import string

from validator import validate_character_options, validate_length

AMBIGUOUS_CHARACTERS = "Il1O0"


def build_character_pool(use_uppercase, use_lowercase, use_numbers, use_symbols,
                          exclude_ambiguous=False):
    """Combine the requested character sets into a single pool string."""
    validate_character_options(use_uppercase, use_lowercase, use_numbers, use_symbols)

    pool = ""
    if use_uppercase:
        pool += string.ascii_uppercase
    if use_lowercase:
        pool += string.ascii_lowercase
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if exclude_ambiguous:
        pool = "".join(char for char in pool if char not in AMBIGUOUS_CHARACTERS)

    return pool


def generate_password(length, min_length=6, max_length=64, use_uppercase=True,
                       use_lowercase=True, use_numbers=True, use_symbols=True,
                       exclude_ambiguous=False):
    """Generate a random password meeting the given length and character rules."""
    validate_length(length, min_length, max_length)
    pool = build_character_pool(use_uppercase, use_lowercase, use_numbers,
                                 use_symbols, exclude_ambiguous)

    password_chars = [secrets.choice(pool) for _ in range(length)]
    _ensure_required_sets(password_chars, pool, use_uppercase, use_lowercase,
                           use_numbers, use_symbols)

    return "".join(password_chars)


def _ensure_required_sets(password_chars, pool, use_uppercase, use_lowercase,
                           use_numbers, use_symbols):
    """Guarantee at least one character from every enabled set is present."""
    required_sets = []
    if use_uppercase:
        required_sets.append(string.ascii_uppercase)
    if use_lowercase:
        required_sets.append(string.ascii_lowercase)
    if use_numbers:
        required_sets.append(string.digits)
    if use_symbols:
        required_sets.append(string.punctuation)

    for char_set in required_sets:
        available = [char for char in char_set if char in pool]
        if available and not any(char in char_set for char in password_chars):
            replace_index = secrets.randbelow(len(password_chars))
            password_chars[replace_index] = secrets.choice(available)


def generate_passphrase(word_count=4, separator="-", word_list=None):
    """Generate a simple passphrase from a word list, useful for memorable secrets."""
    if word_list is None:
        word_list = _default_word_list()

    words = [secrets.choice(word_list) for _ in range(word_count)]
    return separator.join(words)


def _default_word_list():
    return [
        "orbit", "cedar", "quartz", "meadow", "flint", "harbor", "signal",
        "canvas", "ember", "willow", "granite", "prairie", "coral", "lantern",
    ]
