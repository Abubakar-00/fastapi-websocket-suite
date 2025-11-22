# WebSocket Client + Server Project

This project implements a WebSocket-based calculator with a FastAPI server, an async Python client, and a web UI.

## Architecture

- **Server**: FastAPI application exposing a WebSocket endpoint `/ws`. Handles arithmetic operations (add, subtract, multiply, divide).
- **Client**: Async Python CLI tool to interact with the server.
- **UI**: HTML/JS frontend using Tailwind CSS for a user-friendly interface.
- **DevOps**: Dockerized services managed by Docker Compose, with CI/CD via GitHub Actions.

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional, for containerized run)

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### 1. Server

Start the WebSocket server:
```bash
make server
# OR
uvicorn server.main:app --reload --host 0.0.0.0 --port 8000
```
The server will be available at `ws://localhost:8000/ws`.

<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/df94e455-6f47-46e2-8a52-05454e1a4335" />


### 2. Client (CLI)

Run a single operation:
```bash
python client/main.py --operation add --a 5 --b 10
```

Run the demo mode (continuous random operations):
```bash
python client/main.py
# OR
make client
```
<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/0f6669c2-972d-4227-ba98-33c56b99c10f" />

### 3. UI

Open `ui/index.html` in your web browser. You can do this directly or serve it via a simple HTTP server:
```bash
cd ui && python -m http.server 8080
```
Then visit `http://localhost:8080`.

<img width="1200" height="1008" alt="image" src="https://github.com/user-attachments/assets/56823adb-6225-49cf-80b3-0aee50b66511" />

### 4. Docker

#### Development (Server + Client)
Build and run the server and client (CLI) locally:
```bash
docker-compose up --build
```

#### Development (Server + UI)
Build and run the server and UI (Nginx) locally:
```bash
docker compose -f docker-compose.ui.yaml up --build
```
Access the UI at `http://localhost:8080`.

#### Production (Pre-built Images)
Run the full stack using images pulled from Docker Hub (no build required):
```bash
export DOCKERHUB_USERNAME=abubakar00
docker compose -f docker-compose.prod.yaml up -d
```
Ensure you have set the `DOCKERHUB_USERNAME` environment variable to match the image repository.

## Testing

Run the test suite:
```bash
make test
# OR
pytest
```
<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/c693ae3c-ebb4-4e73-a8dc-cb453a9da6ec" />

## CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs on every push to `main`. It performs:
- Linting (flake8, black, isort)
- Testing (pytest)
- Docker image builds

## Project Structure

```
ws_project/
├── server/         # FastAPI server code
├── client/         # Async Python client code
├── ui/             # HTML/JS frontend
├── tests/          # Pytest suite
├── docker/         # Dockerfiles
├── .github/        # CI/CD workflows
├── requirements.txt
├── Makefile
└── README.md
```
