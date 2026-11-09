# Vaultkey — Password Generator

A full-stack web application built on top of an existing CLI password
generator. The original Python modules (`generator.py`, `validator.py`,
`strength.py`, `history.py`, `utils.py`, `config.py`) are reused **completely
unmodified** — the FastAPI backend imports and calls them directly rather
than reimplementing any of their logic.

## Features

- Cryptographically secure password generation (`secrets` module under the hood)
- Adjustable length, character sets (uppercase / lowercase / numbers / symbols)
- Exclude similar/ambiguous characters (`l`, `1`, `O`, `0`)
- Real-time strength meter — entropy (bits), strength label, animated bar
- Estimated crack time
- Copy to clipboard, one-click "Generate again"
- Password history, backed by SQLite, with copy-per-row
- Export history as TXT or CSV (server-generated) or JSON (client-side snapshot)
- Clear history
- Reset settings to defaults
- Keyboard shortcuts (`G` generate, `C` copy)
- Settings persisted in `localStorage`
- Dark mode / light mode
- Fully responsive, glassmorphism UI with animated transitions

## Screenshots

_Add screenshots of the Generator and History tabs here once you've run the
app locally — e.g. `docs/screenshot-generator.png`, `docs/screenshot-history.png`._

## Project structure

```
password-generator-web/
├── backend/
│   ├── app.py                # FastAPI app: middleware, routers, startup
│   ├── database.py            # SQLAlchemy engine/session
│   ├── routes/                # API route handlers
│   ├── services/              # Business logic, bridges to legacy modules
│   ├── models/                # SQLAlchemy ORM models
│   ├── schemas/                # Pydantic request/response schemas
│   ├── existing/               # <-- Original CLI project, untouched
│   │   ├── generator.py
│   │   ├── validator.py
│   │   ├── strength.py
│   │   ├── history.py
│   │   ├── utils.py
│   │   ├── config.py
│   │   ├── main.py            # Original CLI entrypoint (still runnable)
│   │   ├── data/config.json
│   │   └── tests/             # Original unit tests, untouched
│   ├── static/exports/         # Generated TXT/CSV exports land here
│   ├── tests/                  # New API-level tests
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── Dockerfile
│   └── .env.example
│
├── docker-compose.yml
├── LICENSE
└── README.md
```

## How the backend reuses the existing code

`backend/services/legacy_bridge.py` adds `backend/existing/` to `sys.path` at
import time. Because the original modules already accept optional `path`
arguments (e.g. `save_to_history(password, strength, path=...)`,
`load_config(path=...)`), the service layer can point them at the right data
files without changing a single line inside `existing/`. The web app also
keeps its own normalized SQLite table (via SQLAlchemy) for the history/export
API, while the original CLI's CSV history file (`existing/data/history.csv`)
keeps being written to exactly as before — so the CLI (`existing/main.py`)
still works standalone if you run it directly.

## Getting started

### Prerequisites

- Python 3.12+
- Node.js 20+
- (Optional) Docker & Docker Compose

### 1. Run the backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app:app --reload --port 8000
```

The API is now running at `http://localhost:8000`, with interactive docs at
`http://localhost:8000/docs`.

Run backend tests:

```bash
pytest
```

### 2. Run the frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

The app is now running at `http://localhost:5173`.

Run frontend tests:

```bash
npm run test
```

### 3. (Optional) Run everything with Docker Compose

```bash
docker-compose up --build
```

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`

### 4. Run the original CLI (unchanged)

```bash
cd backend/existing
python main.py
```

## API documentation

Base URL: `http://localhost:8000/api`

| Method | Endpoint         | Description                                   |
|--------|------------------|------------------------------------------------|
| POST   | `/generate`      | Generate a password, save it to history        |
| POST   | `/strength`      | Score the strength of an arbitrary password     |
| GET    | `/history`       | List recent generated passwords                |
| DELETE | `/history`       | Clear all stored history                        |
| GET    | `/export/txt`    | Download history as a `.txt` file               |
| GET    | `/export/csv`    | Download history as a `.csv` file               |
| GET    | `/health`        | Liveness check                                  |

Full interactive documentation (via Swagger UI) is auto-generated by FastAPI
at `/docs`, and ReDoc at `/redoc`.

### Example: `POST /generate`

Request body:

```json
{
  "length": 16,
  "min_length": 6,
  "max_length": 64,
  "use_uppercase": true,
  "use_lowercase": true,
  "use_numbers": true,
  "use_symbols": true,
  "exclude_ambiguous": false
}
```

Response:

```json
{
  "id": 1,
  "password": "kX9!qT2vLp#7dR4m",
  "strength": "Strong",
  "entropy_bits": 92.4,
  "length": 16,
  "score": 72,
  "estimated_crack_time": "312.7 years",
  "created_at": "2026-08-01T12:34:56.000000"
}
```

## Tech stack

**Frontend:** React, Vite, Tailwind CSS, Framer Motion, React Icons, Axios, React Hot Toast
**Backend:** FastAPI, SQLAlchemy, SQLite, Pydantic
**Testing:** Pytest + httpx (backend), Vitest + Testing Library (frontend)

## Future enhancements

- User accounts so history is private per person, not per browser
- Passphrase generation mode (the legacy `generate_passphrase` function already
  exists in `existing/generator.py` and is ready to be wired up)
- Rate limiting on the public API
- PostgreSQL support for multi-instance deployments
- Browser extension for autofill

## License

MIT — see [LICENSE](./LICENSE).
