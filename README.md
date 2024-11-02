# Backend Engineering Task: Copilot Credit Usage API

A FastAPI repository for calculating the credit usage of a billing period for OW Copilot service.

## Getting Started

1. Open a terminal window and [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Choose your preferred method to setup and run the application:
    - [Run with venv](#1-run-with-venv)
    - [Run with Docker](#2-run-with-docker)
3. Visit `http://127.0.0.1:8000/docs` in your browser to view the API documentation. (replace `8000` with your port number if you changed it)

## Setup

### 1. Run with venv

#### 1.1 Prerequisite
- Python 3.12+

### 1.2. Setup

1. In the terminal window, navigate to the root directory of this repository and create a virtual environment:
```
python3 -m venv venv
```

2. Activate the virtual environment with:
```
source venv/bin/activate
```

3. Install dependencies from requirements.txt file:
```
pip install -r requirements.txt
```

### 1.3. Running the Application

Location of command execution: `backend/`

| Command | Description |
|-----------|-----------|
| `fastapi run app/main.py` | Run the backend application in development mode with port 8000 |
| `fastapi run app/main.py --port={PORT}` | Run the backend application in production mode with port {PORT} |
| `fastapi dev app/main.py` | Run the backend application in development mode with port 8000 |
| `fastapi dev app/main.py --port={PORT}` | Run the backend application in production mode with port {PORT} |
| `pytest` | Run tests |


### 2. Run With Docker

#### 2.1 Prerequisite
- Docker Engine

### 2.2. Setup

1. In the terminal window, navigate to the root directory of this repository.

2. (Optional) If you need to change the port of the application, copy `.env.example` to `.env` and update it with your own values.

2. Run this docker command to build docker image(s):
```
docker compose build
```

### 2.3. Running the Application

Location of command execution: Root directory of this repository

| Command | Description |
|-----------|-----------|
| `docker compose up` | Run the container(s) |
| `docker compose up -d` | Run container(s) in detached mode |
| `docker compose down` | Stop the container(s) |
| `docker exec ow-test-backend python -m pytest` | Run tests in docker backend container |


## Task Details

### Thought Process

#### 1. Requirement Analysis

##### 1.1. Potentially Ambiguous Requirements and Assumptions

##### 1.2. Decision on a List of Features within Time Limit

#### 2. Choice of Language / Framework / Libraries


### Possible Improvements


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details