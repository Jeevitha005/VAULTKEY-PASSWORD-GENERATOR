# Password Generator

A command-line password generator built in Python. Generates cryptographically
secure passwords, checks password strength, keeps a history of generated
passwords, and exports them to TXT or CSV.

## Features

- Secure password generation using the `secrets` module (not `random`)
- Configurable length, and toggles for uppercase, lowercase, numbers, and symbols
- Password strength checker (Weak / Medium / Strong) based on entropy
- Input validation with clear error messages
- Password history saved locally with timestamps
- Export history to TXT or CSV
- Copy generated passwords to clipboard
- Generation statistics (total generated, average length)
- Error and event logging
- Configurable defaults via `data/config.json`
- Unit tests for generation, validation, and strength checking

## Installation

```bash
git clone https://github.com/<your-username>/password-generator.git
cd password-generator
pip install -r requirements.txt
```

Clipboard copying requires `pyperclip`. On Linux you may also need `xclip` or
`xsel` installed (`sudo apt install xclip`).

## Usage

Run the CLI:

```bash
python main.py
```

You'll see a menu:

```
==== Password Generator ====
1. Generate Password
2. Check Password Strength
3. View Password History
4. Export Passwords
5. Settings
6. Exit
```

Follow the prompts to generate a password, check an existing one, review
history, or export saved passwords.

### Running tests

```bash
python -m unittest discover tests
```

## Folder Structure

```
password_generator/
├── main.py            # CLI entry point and menu logic
├── generator.py        # Core password generation
├── validator.py         # Input validation
├── strength.py         # Password strength scoring
├── history.py          # History storage, stats, export
├── config.py           # Settings load/save
├── utils.py            # Logging and clipboard helpers
├── tests/               # Unit tests
├── data/
│   └── config.json     # Default settings
├── requirements.txt
├── .gitignore
└── README.md
```

## Screenshots

_Add screenshots of the CLI menu and a sample generation run here._

## Future Improvements

- Add a simple web or GUI front end
- Support passphrase generation with dictionary word lists
- Add password breach checking via the HaveIBeenPwned API
- Encrypt the local history file instead of storing plain text

## License

MIT
