# WebSocket Calculator

A WebSocket-based calculator implementation with a FastAPI server, async Python client, and web interface.

## 🏗️ Architecture

**Server**: FastAPI application with WebSocket endpoint at `/ws` for arithmetic operations (add, subtract, multiply, divide)

**Client**: Async Python CLI for server interaction

**UI**: HTML/JavaScript frontend with Tailwind CSS

**DevOps**: Dockerized services with Docker Compose and GitHub Actions CI/CD

## 📋 Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

## 🚀 Setup

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Running the Project

### Server

Start the WebSocket server:

```bash
make server
# or
uvicorn server.main:app --reload --host 0.0.0.0 --port 8000
```

Server available at `ws://localhost:8000/ws`

<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/df94e455-6f47-46e2-8a52-05454e1a4335" />

### Client (CLI)

Single operation:

```bash
python client/main.py --operation add --a 5 --b 10
```

Demo mode (continuous random operations):

```bash
python client/main.py
# or
make client
```

<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/0f6669c2-972d-4227-ba98-33c56b99c10f" />

### Web UI

Open `ui/index.html` directly in your browser, or serve it:

```bash
cd ui && python -m http.server 8080
```

Visit `http://localhost:8080`

<img width="1200" height="1008" alt="image" src="https://github.com/user-attachments/assets/56823adb-6225-49cf-80b3-0aee50b66511" />

### 🐳 Docker

**Development (Server + Client)**:

```bash
docker-compose up --build
```

**Development (Server + UI)**:

```bash
docker compose -f docker-compose.ui.yaml up --build
```

Access UI at `http://localhost:8080`

**Production (Pre-built images)**:

```bash
export DOCKERHUB_USERNAME=abubakar00
docker compose -f docker-compose.prod.yaml up -d
```

## 🧪 Testing

```bash
make test
# or
pytest
```

<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/c693ae3c-ebb4-4e73-a8dc-cb453a9da6ec" />

## 🔄 CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push to `main`:

- Linting with flake8, black, and isort
- Testing with pytest
- Docker image builds

## 📁 Project Structure

```
ws_project/
├── server/              # FastAPI server
├── client/              # Async Python client
├── ui/                  # HTML/JS frontend
├── tests/               # Test suite
├── docker/              # Dockerfiles
├── .github/             # CI/CD workflows
├── requirements.txt
├── Makefile
└── README.md
```