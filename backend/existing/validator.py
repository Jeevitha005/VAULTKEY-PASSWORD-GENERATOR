"""Validate user input for password length and character-set options."""


class ValidationError(Exception):
    """Raised when user input fails a validation rule."""


def validate_length(length, min_length, max_length):
    """Ensure the requested password length is a sane integer within bounds."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise ValidationError("Password length must be a whole number.")

    if length < min_length:
        raise ValidationError(f"Password length must be at least {min_length}.")

    if length > max_length:
        raise ValidationError(f"Password length must not exceed {max_length}.")

    return length


def validate_character_options(use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Ensure at least one character set is enabled."""
    if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
        raise ValidationError("At least one character type must be selected.")

    return True


def parse_length_input(raw_value):
    """Convert raw CLI text into an integer, raising ValidationError on failure."""
    try:
        return int(raw_value.strip())
    except (AttributeError, ValueError):
        raise ValidationError("Length must be a number, e.g. 12.")


def parse_yes_no(raw_value, default=True):
    """Convert a yes/no style prompt answer into a boolean."""
    if raw_value is None or raw_value.strip() == "":
        return default

    answer = raw_value.strip().lower()
    if answer in ("y", "yes"):
        return True
    if answer in ("n", "no"):
        return False

    raise ValidationError("Please answer with y/n.")
