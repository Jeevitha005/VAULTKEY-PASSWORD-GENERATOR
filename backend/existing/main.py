"""Command-line interface for the password generator toolkit."""

import config
import history
import utils
from generator import generate_password
from strength import strength_report
from validator import ValidationError, parse_length_input, parse_yes_no

logger = utils.setup_logger()

MENU_TEXT = """
==== Password Generator ====
1. Generate Password
2. Check Password Strength
3. View Password History
4. Export Passwords
5. Settings
6. Exit
"""


def prompt_password_options(settings):
    """Collect password options from the user, falling back to config defaults."""
    length_input = input(f"Length [{settings['default_length']}]: ")
    length = settings["default_length"] if length_input.strip() == "" else parse_length_input(length_input)

    use_uppercase = parse_yes_no(input("Include uppercase? (y/n) [y]: "), settings["use_uppercase"])
    use_lowercase = parse_yes_no(input("Include lowercase? (y/n) [y]: "), settings["use_lowercase"])
    use_numbers = parse_yes_no(input("Include numbers? (y/n) [y]: "), settings["use_numbers"])
    use_symbols = parse_yes_no(input("Include symbols? (y/n) [y]: "), settings["use_symbols"])

    return {
        "length": length,
        "min_length": settings["min_length"],
        "max_length": settings["max_length"],
        "use_uppercase": use_uppercase,
        "use_lowercase": use_lowercase,
        "use_numbers": use_numbers,
        "use_symbols": use_symbols,
    }


def handle_generate(settings):
    """Generate a password, display it, and save it to history."""
    try:
        options = prompt_password_options(settings)
        password = generate_password(**options)
    except ValidationError as error:
        print(f"Invalid input: {error}")
        logger.error("Validation failed during generation: %s", error)
        return

    report = strength_report(password)
    history.save_to_history(password, report["strength"], settings["history_file"])
    logger.info("Password generated (length=%s, strength=%s)", len(password), report["strength"])

    print(f"\nGenerated password: {password}")
    print(f"Strength: {report['strength']} (entropy: {report['entropy_bits']} bits)")

    if utils.copy_to_clipboard(password):
        print("Copied to clipboard.")
    else:
        print("Clipboard unavailable (install 'pyperclip' to enable this feature).")


def handle_check_strength():
    """Prompt for an existing password and display its strength report."""
    password = input("Enter a password to check: ")
    if not password:
        print("No password entered.")
        return

    report = strength_report(password)
    print(f"Length: {report['password_length']}")
    print(f"Entropy: {report['entropy_bits']} bits")
    print(f"Strength: {report['strength']}")


def handle_view_history(settings):
    """Display saved password history and generation statistics."""
    entries = history.load_history(settings["history_file"])
    if not entries:
        print("No history found yet.")
        return

    for entry in entries[-10:]:
        print(f"{entry['timestamp']} | {entry['password']} | {entry['strength']}")

    stats = history.get_statistics(settings["history_file"])
    print(f"\nTotal generated: {stats['total_generated']}")
    print(f"Average length: {stats['average_length']}")


def handle_export(settings):
    """Export saved password history to TXT or CSV."""
    choice = input("Export as (1) TXT or (2) CSV? ")
    if choice == "1":
        count = history.export_to_txt("data/exported_passwords.txt", settings["history_file"])
        print(f"Exported {count} passwords to data/exported_passwords.txt")
    elif choice == "2":
        count = history.export_to_csv("data/exported_passwords.csv", settings["history_file"])
        print(f"Exported {count} passwords to data/exported_passwords.csv")
    else:
        print("Invalid choice.")


def handle_settings(settings):
    """View and update default generator settings."""
    print("\nCurrent settings:")
    for key, value in settings.items():
        print(f"  {key}: {value}")

    change = parse_yes_no(input("\nChange default length? (y/n) [n]: "), default=False)
    if change:
        try:
            new_length = parse_length_input(input("New default length: "))
            settings["default_length"] = new_length
            config.save_config(settings)
            print("Settings updated.")
        except ValidationError as error:
            print(f"Invalid input: {error}")


def main():
    """Run the interactive CLI menu loop."""
    settings = config.load_config()

    actions = {
        "1": lambda: handle_generate(settings),
        "2": handle_check_strength,
        "3": lambda: handle_view_history(settings),
        "4": lambda: handle_export(settings),
        "5": lambda: handle_settings(settings),
    }

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid option, please try again.")
            continue

        try:
            action()
        except Exception as error:
            logger.error("Unexpected error: %s", error)
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
